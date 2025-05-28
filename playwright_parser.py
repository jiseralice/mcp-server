import re
import json

def parse_playwright_mcp_server(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Browser Automation", # Pre-defined based on context
        "repository_url": "https://github.com/microsoft/playwright-mcp", # Given
        "language": None,
        "tags": ["Playwright", "Browser Automation", "Microsoft"] # General tags
    }

    # Extract Name
    # Look for a line that starts with "Playwright MCP" likely as a title.
    # The fetched text might have markdown links or formatting.
    # "Playwright MCP\n\n   A Model Context Protocol (MCP) server that provides browser automation"
    name_match = re.search(r"Playwright MCP\n\n\s*A Model Context Protocol \(MCP\) server", text, re.IGNORECASE)
    if name_match:
        server_info["name"] = "Playwright MCP Server"
    else:
        # Fallback: Try to get from a prominent header if the specific sentence isn't found
        # The text output shows "[60]microsoft / [61]playwright-mcp Public" and then "Playwright MCP server"
        # Or, the title line "Playwright MCP"
        name_match_alt = re.search(r"^\s*Playwright MCP\s*$", text, re.MULTILINE | re.IGNORECASE)
        if name_match_alt:
             server_info["name"] = name_match_alt.group(0).strip()
        else:
            # Generic fallback if specific patterns fail
            repo_name_match = re.search(r"\[\d+\]microsoft / \[(?P<id>\d+)\](?P<name>playwright-mcp) Public", text)
            if repo_name_match and repo_name_match.group("name"):
                 server_info["name"] = repo_name_match.group("name").replace("-", " ").capitalize() + " Server" # e.g. Playwright mcp Server
            else:
                server_info["name"] = "Playwright MCP Server (Fallback Name)"


    # Extract Description
    # "A Model Context Protocol (MCP) server that provides browser automation
    # capabilities using [136]Playwright. This server enables LLMs to
    # interact with web pages through structured accessibility snapshots,
    # bypassing the need for screenshots or visually-tuned models."
    description_match = re.search(
        r"A Model Context Protocol \(MCP\) server that provides browser automation capabilities using.*?Playwright\.(.*?)(?=\n\nKey Features|\n\nRequirements|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )
    if description_match:
        desc_text = description_match.group(1).strip()
        # Clean up reference links like [136]
        desc_text = re.sub(r"\[\d+\]", "", desc_text)
        # Consolidate multiple lines/spaces
        server_info["description"] = ' '.join(desc_text.split()).strip()
    else:
        # Broader fallback for description
        intro_match = re.search(r"Playwright MCP\n\n(.*?)(?=\n\nKey Features|\n\nRequirements|\Z)", text, re.DOTALL | re.IGNORECASE)
        if intro_match:
            desc_text = intro_match.group(1).strip()
            desc_text = re.sub(r"\[\d+\]", "", desc_text)
            server_info["description"] = ' '.join(desc_text.split()).strip()
        else:
            server_info["description"] = "High-performance MCP server for browser automation using Playwright."


    # Extract Language
    # Look for "Languages" section: "Languages\n\n     * [163]TypeScript 91.7%"
    language_section_match = re.search(r"Languages\n\n(.*?)(?=\n\nFooter|\Z)", text, re.DOTALL)
    if language_section_match:
        lang_text = language_section_match.group(1)
        ts_match = re.search(r"TypeScript\s*([\d\.]+)%", lang_text)
        if ts_match:
            server_info["language"] = "TypeScript"
    
    if not server_info["language"]: # Fallback if specific regex fails
        if "TypeScript" in text or ".ts" in text: # General check
             server_info["language"] = "TypeScript"


    return [server_info] # Output is a list containing a single dictionary

if __name__ == "__main__":
    try:
        with open("playwright_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: playwright_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_playwright_mcp_server(text_content)
    
    output_filename = "playwright_mcp_server.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} server(s) and saved to {output_filename}")
