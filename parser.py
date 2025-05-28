import re
import json

def parse_mcp_servers(text):
    servers = []
    # Isolate the Server Implementations section
    # Adjusted regex for "Server Implementations" section detection based on observed text structure
    server_implementations_match = re.search(
        r"\nServer Implementations\n\n(.*?)(?=\nFrameworks\n|\nTips and Tricks\n|\nStar History\n|\Z)", 
        text, re.DOTALL | re.IGNORECASE
    )
    if not server_implementations_match:
        print("Could not find the 'Server Implementations' section using primary regex.")
        # Fallback: Try to find "Server Implementations" and capture broadly until a known next major section or EOF
        server_implementations_match = re.search(
            r"Server Implementations\n(.*?)(\n(Contributors|Frameworks|Tips and Tricks|Star History|About)\n|\Z)", # Added "About" as a potential end marker
            text, re.DOTALL | re.IGNORECASE
        )
        if not server_implementations_match:
            print("Could not find the 'Server Implementations' section using fallback regex.")
            return servers

    server_implementations_text = server_implementations_match.group(1)
    
    # Regex to identify categories. Categories appear like: "\n🔗 Aggregators\n\n   Description..."
    category_regex = r"\n([🔗🎨📂☁️👨‍💻🤖🖥️💬👤🗄️📊🚚🛠️🧮📟💰🎮🧠🗺️🎯📊🎥🔎🔒🌐🏃🎧🌎🔄🛠️].*?)\n\n(.*?)(?=\n[🔗🎨📂☁️👨‍💻🤖🖥️💬👤🗄️📊🚚🛠️🧮📟💰🎮🧠🗺️🎯📊🎥🔎🔒🌐🏃🎧🌎🔄🛠️].*?\n\n|\Z)"
    
    # New server_regex to match format like: * [RefNum]ServerNameText Icons - Description
    # Group 1: RefNum (digits), Group 2: ServerNameText, Group 3: Icons, Group 4: Description
    server_regex = r"\*\s*\[(\d+)\](.*?)\s+((?:(?:🎖️|🐍|📇|🏎️|🦀|#️⃣|☕|☁️|🏠|📟|🍎|🪟|🐧)\s*)*)\s*-\s*(.*)"

    # Step 2: Parse references to build a ref_num to URL map
    references_section_match = re.search(r"\nReferences\n\n(.*?)\n\nVisible links:", text, re.DOTALL | re.IGNORECASE)
    if not references_section_match:
        # Fallback for references section
        references_section_match = re.search(r"\nReferences\n\n(.*?)(\nFooter\n|\Z)", text, re.DOTALL | re.IGNORECASE)
    
    ref_to_url = {}
    if references_section_match:
        references_text = references_section_match.group(1)
        # Regex for reference lines: e.g., "   173. https://github.com/julien040/anyquery"
        ref_line_regex = r"^\s*(\d+)\.\s*(https?://\S+)"
        for ref_match in re.finditer(ref_line_regex, references_text, re.MULTILINE):
            ref_num = ref_match.group(1)
            url = ref_match.group(2).strip()
            ref_to_url[ref_num] = url
    else:
        # Keep this warning as it's relevant if References section is missing
        print("Warning: Could not find References section. URLs will be missing.")

    # category_count = 0 # Remove or comment out debug variable
    for category_match in re.finditer(category_regex, server_implementations_text, re.DOTALL):
        # category_count += 1 # Remove or comment out debug variable
        category_title_full = category_match.group(1).strip()
        category_name_match = re.search(r"[^ ]*?\s(.*)", category_title_full)
        category_title = category_name_match.group(1).strip() if category_name_match else category_title_full
        
        category_content = category_match.group(2)
        # Debug print for category
        # print(f"\n--- Matched Category: {category_title} ---")
        # print(category_content[:300])
        # print("--- End Category Content ---")
        current_category = category_title

        # server_count_in_category = 0 # Remove or comment out debug variable
        for line in category_content.splitlines():
            server_match = re.match(server_regex, line.strip())
            if not server_match:
                continue

            ref_num = server_match.group(1).strip()
            name_text = server_match.group(2).strip() # This is the ServerNameText
            icons_text = server_match.group(3).strip()
            description = server_match.group(4).strip()

            repo_url = ref_to_url.get(ref_num, "") # Get URL from map, default to empty if not found
            
            # If URL is directly in name_text for some entries (fallback or different format)
            # This part might need adjustment if some entries *do* have [Name](URL) format
            # For now, we prioritize the ref_to_url lookup.
            # The name would be just name_text.

            icons = re.findall(r"(🎖️|🐍|📇|🏎️|🦀|#️⃣|☕|☁️|🏠|📟|🍎|🪟|🐧)", icons_text)
            
            language_map = {
                '🐍': 'Python', '📇': 'TypeScript/JavaScript', '🏎️': 'Go',
                '🦀': 'Rust', '#️⃣': 'C#', '☕': 'Java'
            }
            language = None
            for icon in icons:
                if icon in language_map:
                    language = language_map[icon]
                    break
            
            servers.append({
                "name": name_text, # Using the text next to ref num as name
                "description": description,
                "category": current_category,
                "repository_url": repo_url,
                "language": language,
                "tags": icons
            })
            # server_count_in_category +=1 # Remove or comment out debug variable
        # Correctly indented print for server count in category (comment out for final)
        # print(f"Found {server_count_in_category} servers in '{category_title}'")
    
    # Correctly indented check for category count (comment out for final)
    # if category_count == 0:
    #     print("No categories were matched by the category_regex.")
    return servers

if __name__ == "__main__":
    with open("github_page.txt", "r", encoding="utf-8") as f:
        text_content = f.read()
    
    extracted_data = parse_mcp_servers(text_content)
        
    with open("mcp_servers.json", "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False)
    
    print(f"Extracted {len(extracted_data)} servers and saved to mcp_servers.json")
