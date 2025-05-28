import re
import json

def parse_browsermcp_server(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Browser Automation", # Pre-defined
        "repository_url": "https://github.com/BrowserMCP/mcp", # Given
        "language": None,
        "tags": ["Browser Automation", "Chrome Extension"] # General tags
    }

    # Extract Name
    # Look for the main title: "Browser MCP"
    # It appears like: "[108]Browser MCP banner\n\n                                 Browser MCP"
    # Or from the repo name: "[60]BrowserMCP / [61]mcp Public"
    name_match = re.search(r"Browser MCP banner\n\n\s*Browser MCP", text, re.IGNORECASE)
    if name_match:
        server_info["name"] = "Browser MCP"
    else:
        repo_name_match = re.search(r"\[\d+\]BrowserMCP / \[\d+\]mcp Public", text)
        if repo_name_match:
            server_info["name"] = "BrowserMCP" # Or "BrowserMCP Server"
        else:
            server_info["name"] = "BrowserMCP (Fallback Name)"

    # Extract Description
    # "Browser MCP is an MCP server + Chrome extension that allows you to
    # automate your browser using AI applications like VS Code, Claude,
    # Cursor, and Windsurf."
    # This is under an "About" heading.
    
    # Try to find the "About" section first, then the description within it.
    about_section_match = re.search(r"About\n\n(.*?)(?=\n\nFeatures|\n\nContributing|\Z)", text, re.DOTALL | re.IGNORECASE)
    if about_section_match:
        about_text = about_section_match.group(1).strip()
        # Clean up reference links like [109]
        desc_text = re.sub(r"\[\d+\]", "", about_text)
        # Consolidate multiple lines/spaces
        server_info["description"] = ' '.join(desc_text.split()).strip()
    else:
        # Fallback if "About" section is not clearly delimited
        # The intro line also gives a good description:
        # "Browser MCP is a Model Context Provider (MCP) server that allows AI
        # applications to control your browser"
        fallback_desc_match = re.search(r"Browser MCP is a Model Context Provider \(MCP\) server that allows AI applications to control your browser", text, re.IGNORECASE)
        if fallback_desc_match:
            server_info["description"] = fallback_desc_match.group(0).strip()
        else:
            server_info["description"] = "MCP server and Chrome extension for browser automation using AI applications."


    # Extract Language
    # Look for "Languages" section: "Languages\n\n     * [131]TypeScript 89.2%"
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
        with open("browsermcp_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: browsermcp_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_browsermcp_server(text_content)
    
    output_filename = "browsermcp_server.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} server(s) and saved to {output_filename}")
