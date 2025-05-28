import json
from collections import defaultdict
import re

def get_display_name(server):
    name_en = server.get("name") or server.get("name_en")
    name_zh = server.get("name_zh")
    
    if name_en and name_zh and name_en.lower() != name_zh.lower():
        # Heuristic to avoid "Repo Name / Repo Name" if name_zh was just the repo name
        if name_zh.replace(" ", "").replace("-", "").lower() == name_en.replace(" ", "").replace("-", "").lower():
            return name_en
        return f"{name_en} / {name_zh}"
    return name_en or name_zh or "Unnamed Server"

def get_category_key(server):
    # Prioritize English category, then Chinese, then default
    category_en = server.get("category_en")
    category_zh = server.get("category_zh")
    
    if category_en and category_en.strip():
        return category_en.strip()
    if category_zh and category_zh.strip():
        # Try to clean up common Chinese category prefixes/emojis for grouping key
        # This helps group "🌐 Browser Automation" and "Browser Automation" together if one is missing cat_en
        cleaned_zh_cat = re.sub(r"^[🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩]\s*", "", category_zh).strip()
        if cleaned_zh_cat:
            return cleaned_zh_cat # Use cleaned Chinese category if English one is missing/generic
        return category_zh.strip() # Fallback to original Chinese category
    return "Other Tools and Integrations" # Default category

def generate_markdown(servers_data):
    lang_icons = {
        'Python': '🐍', 'TypeScript': '📇', 'JavaScript': '📇', 
        'Go': '🏎️', 'Rust': '🦀', 'C#': '#️⃣', 'Java': '☕',
        # Add other languages if they appear
    }
    platform_icons = {
        'Cloud': '☁️', 'Local': '🏠', 'macOS': '🍎', 
        'Windows': '🪟', 'Linux': '🐧', 'Embedded': '📟'
    }

    # Group servers by category
    grouped_servers = defaultdict(list)
    for server in servers_data:
        category_key = get_category_key(server)
        grouped_servers[category_key].append(server)

    markdown_lines = ["# Consolidated MCP Servers List\n"]

    # Sort categories for consistent output, perhaps alphabetically or by a defined order
    # For now, using sorted keys
    for category_name in sorted(grouped_servers.keys()):
        markdown_lines.append(f"\n## {category_name}\n")
        
        for server in sorted(grouped_servers[category_name], key=lambda x: (x.get("name_en") or x.get("name") or "").lower()):
            display_name = get_display_name(server)
            
            icons_str = ""
            # Add language icons
            for lang in server.get("languages", []):
                if lang_icons.get(lang):
                    icons_str += f" {lang_icons[lang]}"
            
            # Add platform icons
            for plat in server.get("platforms", []):
                if platform_icons.get(plat):
                    icons_str += f" {platform_icons[plat]}"
            
            # Some tags might be raw emojis from parsing, try to map them too
            for tag in server.get("tags", []):
                if tag in lang_icons and lang_icons[tag] not in icons_str: # Avoid duplicate lang icons
                    icons_str += f" {lang_icons[tag]}"
                if tag in platform_icons and platform_icons[tag] not in icons_str: # Avoid duplicate plat icons
                    icons_str += f" {platform_icons[tag]}"


            markdown_lines.append(f"\n### {display_name}{icons_str.strip()}\n")

            if server.get("repository_url"):
                markdown_lines.append(f"- **Repository:** [{server['repository_url']}]({server['repository_url']})")
            else:
                markdown_lines.append("- **Repository:** URL not available")

            if server.get("description"):
                markdown_lines.append(f"- **Description:** {server['description']}")
            
            if server.get("description_zh") and server["description_zh"] != server.get("description"):
                markdown_lines.append(f"- **中文简介:** {server['description_zh']}")

            # Filter out already used icon tags from the main tag list for display
            display_tags = [
                tag for tag in server.get("tags", []) 
                if tag not in lang_icons and tag not in platform_icons and not re.match(r"^[🎖️🐍📇🏎️🦀#️⃣☕☁️🏠📟🍎🪟🐧]$", tag)
            ]
            if display_tags:
                markdown_lines.append(f"- **Tags:** {', '.join(sorted(list(set(display_tags))))}")
            
            markdown_lines.append("") # Add a blank line for spacing

    return "\n".join(markdown_lines)

if __name__ == "__main__":
    try:
        with open("consolidated_mcp_servers.json", "r", encoding="utf-8") as f:
            servers_data = json.load(f)
    except FileNotFoundError:
        print("Error: consolidated_mcp_servers.json not found.")
        exit(1)
    except json.JSONDecodeError:
        print("Error: consolidated_mcp_servers.json contains invalid JSON.")
        exit(1)
        
    markdown_content = generate_markdown(servers_data)
    
    try:
        with open("readme_content.md", "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print("Successfully generated readme_content.md")
    except IOError:
        print("Error: Could not write to readme_content.md")
        exit(1)
