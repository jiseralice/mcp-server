import re
import json

def parse_github_mcp_server(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Version Control", # Pre-defined based on context
        "repository_url": "https://github.com/github/github-mcp-server", # Given
        "language": None,
        "tags": ["GitHub", "Version Control", "API"] # General tags
    }

    # Extract Name
    # Look for the main title: "GitHub MCP Server"
    name_match = re.search(r"^\s*GitHub MCP Server\s*$", text, re.MULTILINE | re.IGNORECASE)
    if name_match:
        server_info["name"] = name_match.group(0).strip()
    else:
        # Fallback from the breadcrumb/repo name
        repo_name_match = re.search(r"\[\d+\]github / \[(?P<id>\d+)\](?P<name>github-mcp-server) Public", text)
        if repo_name_match and repo_name_match.group("name"):
            server_info["name"] = repo_name_match.group("name").replace("-", " ").capitalize() # e.g. Github mcp server
            if not "Server" in server_info["name"]:
                 server_info["name"] += " Server"
        else:
            server_info["name"] = "GitHub MCP Server (Fallback Name)"


    # Extract Description
    # "The GitHub MCP Server is a [143]Model Context Protocol (MCP) server
    # that provides seamless integration with GitHub APIs, enabling advanced
    # automation and interaction capabilities for developers and tools."
    description_match = re.search(
        r"The GitHub MCP Server is a .*?Model Context Protocol \(MCP\) server that provides seamless integration with GitHub APIs, enabling advanced automation and interaction capabilities for developers and tools\.",
        text,
        re.DOTALL | re.IGNORECASE
    )
    if description_match:
        desc_text = description_match.group(0).strip()
        # Clean up reference links like [143]
        desc_text = re.sub(r"\[\d+\]", "", desc_text)
        # Consolidate multiple lines/spaces
        server_info["description"] = ' '.join(desc_text.split()).strip()
    else:
        server_info["description"] = "Official GitHub MCP server for API integration and automation."


    # Extract Language
    # Look for "Languages" section: "Languages\n\n     * [187]Go 99.2%"
    language_section_match = re.search(r"Languages\n\n(.*?)(?=\n\nFooter|\Z)", text, re.DOTALL)
    if language_section_match:
        lang_text = language_section_match.group(1)
        # Try to find Go percentage specifically
        go_match = re.search(r"Go\s*([\d\.]+)%", lang_text)
        if go_match:
            server_info["language"] = "Go"
    
    if not server_info["language"]: # Fallback if specific regex fails
         if "Go " in text or ".go" in text or "go build" in text: # General check
             server_info["language"] = "Go"


    return [server_info] # Output is a list containing a single dictionary

if __name__ == "__main__":
    try:
        with open("github_com_mcp_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: github_com_mcp_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_github_mcp_server(text_content)
    
    output_filename = "github_mcp_server.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} server(s) and saved to {output_filename}")
