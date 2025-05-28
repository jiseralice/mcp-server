import re
import json

def parse_whatsapp_mcp_server(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Communication", # Pre-defined
        "repository_url": "https://github.com/lharries/whatsapp-mcp", # Given
        "language": [], # Can have multiple languages
        "tags": ["WhatsApp", "Communication", "Messaging"] # General tags
    }

    # Extract Name
    name_match = re.search(r"^\s*WhatsApp MCP Server\s*$", text, re.MULTILINE | re.IGNORECASE)
    if name_match:
        server_info["name"] = name_match.group(0).strip()
    else:
        # Fallback from the repo name
        repo_name_match = re.search(r"\[\d+\]lharries / \[(?P<id>\d+)\](?P<name>whatsapp-mcp) Public", text)
        if repo_name_match and repo_name_match.group("name"):
            server_info["name"] = repo_name_match.group("name").replace("-", " ").capitalize() + " Server"
        else:
            server_info["name"] = "WhatsApp MCP Server (Fallback Name)"

    # Extract Description
    # "This is a Model Context Protocol (MCP) server for WhatsApp.
    # With this you can search and read your personal Whatsapp messages..."
    description_match = re.search(
        r"This is a Model Context Protocol \(MCP\) server for WhatsApp\.(.*?)(?=\n\nHere's an example|\n\nInstallation|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )
    if description_match:
        desc_text = "This is a Model Context Protocol (MCP) server for WhatsApp." + description_match.group(1).strip()
        desc_text = re.sub(r"\[\d+\]", "", desc_text) # Clean up reference links
        server_info["description"] = ' '.join(desc_text.split()).strip()
    else:
        server_info["description"] = "MCP server for WhatsApp integration, allowing interaction with messages, contacts, and media."

    # Extract Languages
    language_section_match = re.search(r"Languages\n\n(.*?)(?=\n\nFooter|\Z)", text, re.DOTALL)
    if language_section_match:
        lang_text = language_section_match.group(1)
        go_match = re.search(r"Go\s*([\d\.]+)%", lang_text)
        if go_match:
            server_info["language"].append("Go")
        
        python_match = re.search(r"Python\s*([\d\.]+)%", lang_text)
        if python_match:
            server_info["language"].append("Python")
    
    # Fallback if specific regex fails or languages are mentioned elsewhere
    if not server_info["language"]:
        if "Go" in text and "Python" in text: # General check
             server_info["language"].extend(["Go", "Python"])
        elif "Go" in text:
            server_info["language"].append("Go")
        elif "Python" in text:
            server_info["language"].append("Python")
            
    if not server_info["language"]: # If still nothing, set to None or empty list based on preference
        server_info["language"] = None


    return [server_info]

if __name__ == "__main__":
    try:
        with open("whatsapp_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: whatsapp_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_whatsapp_mcp_server(text_content)
    
    output_filename = "whatsapp_mcp_server.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} server(s) and saved to {output_filename}")
