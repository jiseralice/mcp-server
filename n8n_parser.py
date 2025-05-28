import re
import json

def parse_n8n_mcp_node(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Workflow Automation", # Pre-defined
        "repository_url": "https://github.com/nerding-io/n8n-nodes-mcp", # Given
        "language": None,
        "tags": ["n8n", "MCP Client", "Workflow Automation", "Tooling"] # General tags
    }

    # Extract Name
    # Look for the main title: "n8n-nodes-mcp-client"
    name_match = re.search(r"^\s*n8n-nodes-mcp-client\s*$", text, re.MULTILINE | re.IGNORECASE)
    if name_match:
        server_info["name"] = name_match.group(0).strip()
    else:
        # Fallback from the repo name in breadcrumb
        repo_name_match = re.search(r"\[\d+\]nerding-io / \[(?P<id>\d+)\](?P<name>n8n-nodes-mcp) Public", text)
        if repo_name_match and repo_name_match.group("name"):
            # Construct name, assuming it's a client node
            raw_name = repo_name_match.group("name")
            if "client" not in raw_name.lower() and "node" not in raw_name.lower():
                server_info["name"] = raw_name + "-client" # Append client if not present
            else:
                server_info["name"] = raw_name
            server_info["name"] = server_info["name"].replace("-", " ").replace("nodes", "Nodes").replace("mcp", "MCP")

        else:
            server_info["name"] = "n8n-nodes-mcp-client (Fallback Name)"

    # Extract Description
    # "This is an n8n community node that lets you interact with Model Context Protocol (MCP) servers in your n8n workflows.
    # MCP is a protocol that enables AI models to interact with external tools and data sources in a standardized way.
    # This node allows you to connect to MCP servers, access resources, execute tools, and use prompts."
    description_match = re.search(
        r"This is an n8n community node that lets you interact with Model Context Protocol \(MCP\) servers in your n8n workflows\.(.*?)(?=\n\n\[\d+\]n8n is a|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )
    if description_match:
        # The first sentence is part of the match, add it and then the captured group.
        desc_text = "This is an n8n community node that lets you interact with Model Context Protocol (MCP) servers in your n8n workflows." + description_match.group(1).strip()
        desc_text = re.sub(r"\[\d+\]", "", desc_text) # Clean up reference links
        server_info["description"] = ' '.join(desc_text.split()).strip()
    else:
        server_info["description"] = "An n8n community node to interact with Model Context Protocol (MCP) servers."


    # Extract Language
    # Look for "Languages" section: "Languages\n\n     * [192]TypeScript 88.4%"
    language_section_match = re.search(r"Languages\n\n(.*?)(?=\n\nFooter|\Z)", text, re.DOTALL)
    if language_section_match:
        lang_text = language_section_match.group(1)
        ts_match = re.search(r"TypeScript\s*([\d\.]+)%", lang_text)
        if ts_match:
            server_info["language"] = "TypeScript"
    
    if not server_info["language"]: # Fallback if specific regex fails
         if "TypeScript" in text or "tsconfig.json" in text: # General check
             server_info["language"] = "TypeScript"


    return [server_info] # Output is a list containing a single dictionary

if __name__ == "__main__":
    try:
        with open("n8n_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: n8n_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_n8n_mcp_node(text_content)
    
    output_filename = "n8n_nodes_mcp.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} item(s) and saved to {output_filename}")
