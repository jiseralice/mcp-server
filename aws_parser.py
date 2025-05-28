import re
import json

def parse_aws_mcp_servers(text):
    servers = []
    
    # Isolate the "Available Servers" section
    main_section_start_match = re.search(r"Available Servers\n\n", text, re.IGNORECASE)
    if not main_section_start_match:
        print("Could not find the start of 'Available Servers' section.")
        return servers
    
    text_after_header = text[main_section_start_match.end():]
    
    # Skip the introductory sentence "This monorepo contains the following MCP servers:"
    intro_sentence_pattern = r"\s*This monorepo contains the following MCP servers:\s*"
    intro_sentence_match = re.match(intro_sentence_pattern, text_after_header, re.IGNORECASE)
    
    if intro_sentence_match:
        text_after_intro = text_after_header[intro_sentence_match.end():]
    else:
        # If the intro sentence isn't there, maybe the structure changed slightly.
        # We'll use the text_after_header directly but this might need monitoring.
        text_after_intro = text_after_header
        print("Warning: Introductory sentence for 'Available Servers' not found as expected.")

    # Now, find the actual end of the server list from text_after_intro
    end_of_servers_match = re.search(
        r"(?=\n\nUse Cases for the Servers|\n\nInstallation and Setup|\Z)", 
        text_after_intro, 
        re.DOTALL | re.IGNORECASE
    )
    
    if end_of_servers_match:
        available_servers_text = text_after_intro[:end_of_servers_match.start()]
    else:
        # This case should ideally not be reached if \Z works as a fallback.
        available_servers_text = text_after_intro 
        # print("Warning: Could not determine a clear end for 'Available Servers' section content.")

    # print("=== Available Servers Text (first 2000 chars) ===") # Commented out debug print
    # print(available_servers_text[:2000])
    # print("================================================")

    # Regex for individual server blocks
    # A server block typically looks like:
    # Server Name\n\n   [PyPI version]\n\n   Description line 1\n   Description line 2...\n\n   [Learn more] | [Documentation]
    # The server name is often followed by a link reference like [195] for PyPI
    # The description can be multi-line.
    # The "Learn more" link is key.

    # Server blocks are separated by two newlines or more, before the next server name.
    # Server names appear as titles. Example: "Core MCP Server\n\n   [195]PyPI version"
    # Or "AWS Documentation MCP Server\n\n   [198]PyPI version"
    
    # Let's try to split by what looks like a server title pattern
    # A server title is text, possibly with "MCP Server" in it, followed by a PyPI link ref.
    # This is tricky because the "titles" are not standard markdown Hx.
    # Instead, let's find "Learn more" links, as each server has one.
    # The structure is: Server Name ... Description ... [Learn more](URL)
    
    # Regex to find a server block: captures name, description, and learn_more_url
    # It looks for a "Learn more" link and works backwards/forwards.
    # This is complex. Let's try matching based on the "Learn more" link pattern
    # and the text preceding it.
    
    # Each server often starts with a name, then a "[xxx]PyPI version" link, description, then "Learn more" link
    # Example structure for one server:
    # Core MCP Server\n\n   [195]PyPI version\n\n   A server for managing ...\n\n   [196]Learn more | [197]Documentation
    
    # The regex will capture:
    # 1. Server Name (text before the [xxx]PyPI version)
    # 2. Description (text between PyPI version and "Learn more" link)
    # 3. Learn More URL (target of the "Learn more" link reference)
    
    # First, build the reference map for URLs
    ref_to_url = {}
    references_section_match = re.search(r"\nReferences\n\n(.*?)(?:\nFooter\n|\n\nVisible links:|\Z)", text, re.DOTALL | re.IGNORECASE)
    if references_section_match:
        references_text = references_section_match.group(1)
        ref_line_regex = r"^\s*(\d+)\.\s*(https?://\S+)"
        for ref_match in re.finditer(ref_line_regex, references_text, re.MULTILINE):
            ref_num = ref_match.group(1)
            url = ref_match.group(2).strip()
            ref_to_url[ref_num] = url
    else:
        print("Warning: Could not find References section. URLs for 'Learn more' might be missing.")

    # Regex for a server block
    server_block_regex = re.compile(
        r"^(.*?)\n\n\s*\[\d+\]PyPI version\n\n(.*?)\n\n\s*\[(\d+)\]Learn more.*?$",
        re.MULTILINE | re.DOTALL
    )
    # Explanation of server_block_regex:
    # ^(.*?)\n\n                                 # Group 1: Server Name (starts at beginning of a line, up to two newlines)
    # \s*\[\d+\]PyPI version\n\n               # Matches "[RefNum]PyPI version" and two newlines
    # (.*?)                                     # Group 2: Description (non-greedy match of anything)
    # \n\n\s*\[(\d+)\]Learn more.*?$            # Matches two newlines, then "[RefNum]Learn more", captures RefNum (Group 3)
                                                # and anything else until end of line. Uses MULTILINE for ^$ and DOTALL for .*?

    for match in server_block_regex.finditer(available_servers_text):
        name = match.group(1).strip()
        description_block = match.group(2).strip()
        learn_more_ref_num = match.group(3).strip()

        # Consolidate multi-line descriptions
        description = ' '.join(line.strip() for line in description_block.splitlines() if line.strip())
        
        repo_url = ref_to_url.get(learn_more_ref_num, "")

        # Most servers in this repo are Python based.
        language = "Python" 
        
        # Extract AWS service from name or description if possible (heuristic)
        aws_service = name.replace("MCP Server", "").replace("AWS", "").replace("Amazon", "").strip()
        if "Documentation" in name: aws_service = "AWS Documentation"
        if "Bedrock Knowledge Bases" in name: aws_service = "Amazon Bedrock Knowledge Bases"
        if "Kendra Index" in name: aws_service = "Amazon Kendra"
        if "CDK" in name: aws_service = "AWS CDK"
        if "Cost Analysis" in name: aws_service = "AWS Cost Analysis"
        if "Nova Canvas" in name: aws_service = "Amazon Nova Canvas"
        if "Diagram" in name: aws_service = "AWS Diagram (Python Diagrams)"
        if "CloudFormation" in name: aws_service = "AWS CloudFormation"
        if "Lambda" in name: aws_service = "AWS Lambda"
        if "SNS / SQS" in name: aws_service = "Amazon SNS/SQS"
        if "Terraform" in name: aws_service = "AWS Terraform"
        if "Frontend" in name: aws_service = "Frontend (React with AWS)"
        if "ElastiCache / MemoryDB for Valkey" in name: aws_service = "Amazon ElastiCache/MemoryDB (Valkey)"
        if "ElastiCache for Memcached" in name: aws_service = "Amazon ElastiCache (Memcached)"
        if "Location Service" in name: aws_service = "AWS Location Service"
        if "Git Repo Research" in name: aws_service = "Git/Amazon Bedrock"
        if "Code Documentation Generation" in name: aws_service = "Code Documentation Generation"
        if "Aurora Postgres" in name: aws_service = "Amazon Aurora (PostgreSQL)"
        if "Aurora MySql" in name: aws_service = "Amazon Aurora (MySQL)"
        if "MQ" in name: aws_service = "Amazon MQ"
        if "Synthetic Data" in name: aws_service = "Synthetic Data Generation"
        if "Aurora DSQL" in name: aws_service = "Amazon Aurora (DSQL)"
        if "DynamoDB" in name: aws_service = "Amazon DynamoDB"
        if "Neptune" in name: aws_service = "Amazon Neptune"
        if "DocumentDB" in name: aws_service = "Amazon DocumentDB"


        servers.append({
            "name": name,
            "description": description,
            "repository_url": repo_url,
            "language": language,
            "aws_service_integration": aws_service, # Specific detail
            "details_from_description": description_block # Keep raw block for more info
        })
        
    return servers

if __name__ == "__main__":
    # This script expects the fetched text to be in "aws_github_page.txt"
    try:
        with open("aws_github_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: aws_github_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_aws_mcp_servers(text_content)
    
    output_filename = "awslabs_mcp_servers.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} servers and saved to {output_filename}")
