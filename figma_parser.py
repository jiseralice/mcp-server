import re
import json

def parse_figma_mcp_server(text):
    server_info = {
        "name": None,
        "description": None,
        "category": "Design Tools", # Pre-defined
        "repository_url": "https://github.com/GLips/Figma-Context-MCP", # Given
        "language": None,
        "readme_languages": ["English"], # Default
        "tags": ["Figma", "Design Tools", "AI Coding Agent"] # General tags
    }

    # Extract Name
    # Look for the main title: "Framelink Figma MCP Server"
    name_match = re.search(r"^\s*Framelink Figma MCP Server\s*$", text, re.MULTILINE | re.IGNORECASE)
    if name_match:
        server_info["name"] = name_match.group(0).strip()
    else:
        # Fallback from the repo name in breadcrumb or other prominent mentions
        repo_name_match = re.search(r"\[\d+\]GLips / \[(?P<id>\d+)\](?P<name>Figma-Context-MCP) Public", text)
        if repo_name_match and repo_name_match.group("name"):
            raw_name = repo_name_match.group("name").replace("-", " ")
            # Attempt to make it title case or use a known name
            if "figma context mcp" in raw_name.lower():
                 server_info["name"] = "Figma Context MCP Server" # A common way it's referred to
            else:
                server_info["name"] = raw_name.capitalize() + " Server"
        else:
            server_info["name"] = "Figma Context MCP Server (Fallback Name)"

    # Extract Description
    # "Give your coding agent access to your Figma data. Implement designs in any framework in one-shot."
    # "Give Cursor and other AI-powered coding tools access to your Figma files with this Model Context Protocol server."
    
    # Try to capture the initial description lines under the main title
    desc_match = re.search(
        r"Framelink Figma MCP Server\s*\n.*?Available in:.*?\n\n(.*?)(?=\n\n\[\d+\]See quickstart instructions|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )
    if desc_match:
        desc_text = desc_match.group(1).strip()
        # Further clean up by removing potential multiple newlines and extra spaces from joined lines
        desc_text = ' '.join(line.strip() for line in desc_text.splitlines() if line.strip())
        desc_text = re.sub(r"\[\d+\]", "", desc_text) # Clean up reference links
        server_info["description"] = desc_text
    else:
        # Fallback description if the primary regex fails
        fallback_desc_match = re.search(r"MCP server to provide Figma layout information to AI coding agents like Cursor", text, re.IGNORECASE)
        if fallback_desc_match:
            server_info["description"] = fallback_desc_match.group(0).strip()
        else:
            server_info["description"] = "MCP server for integrating Figma design data with AI coding agents."


    # Extract Language
    language_section_match = re.search(r"Languages\n\n(.*?)(?=\n\nFooter|\Z)", text, re.DOTALL)
    if language_section_match:
        lang_text = language_section_match.group(1)
        ts_match = re.search(r"TypeScript\s*([\d\.]+)%", lang_text)
        if ts_match:
            server_info["language"] = "TypeScript"
    
    if not server_info["language"]: # Fallback
         if "TypeScript" in text or "tsconfig.json" in text:
             server_info["language"] = "TypeScript"

    # Extract README Languages
    # "🌐 Available in: [138]한국어 (Korean) | [139]日本語 (Japanese) | [140]中文 (Chinese)"
    readme_lang_match = re.search(r"Available in:\s*(.*?)\n", text)
    if readme_lang_match:
        lang_links_text = readme_lang_match.group(1)
        if "한국어 (Korean)" in lang_links_text or "README.ko.md" in text:
            if "Korean" not in server_info["readme_languages"]: server_info["readme_languages"].append("Korean")
        if "日本語 (Japanese)" in lang_links_text or "README.ja.md" in text:
            if "Japanese" not in server_info["readme_languages"]: server_info["readme_languages"].append("Japanese")
        if "中文 (Chinese)" in lang_links_text or "README.zh.md" in text: # Simplified Chinese
            if "Chinese (Simplified)" not in server_info["readme_languages"]: server_info["readme_languages"].append("Chinese (Simplified)")
        # Check for Traditional Chinese if a different file exists, e.g., README.zh_TW.md
        if "README.zh_TW.md" in text: # Example check, might need specific link text
            if "Chinese (Traditional)" not in server_info["readme_languages"]: server_info["readme_languages"].append("Chinese (Traditional)")


    return [server_info]

if __name__ == "__main__":
    try:
        with open("figma_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: figma_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_figma_mcp_server(text_content)
    
    output_filename = "figma_context_mcp.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} server(s) and saved to {output_filename}")
