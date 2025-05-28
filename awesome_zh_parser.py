import re
import json

def parse_awesome_mcp_zh(text):
    servers = []
    
    # Isolate the "MCP 服务器精选列表" (MCP Server List) section
    # It starts with "MCP 服务器精选列表" and seems to go until "更多 MCP Server 资源" or end of document
    server_list_match = re.search(
        r"MCP 服务器精选列表\n\n(.*?)(?=\n\n更多 MCP Server 资源|\n\nStar History|\Z)",
        text,
        re.DOTALL | re.IGNORECASE
    )
    
    if not server_list_match:
        print("Could not find the 'MCP 服务器精选列表' section.")
        return servers

    server_list_text = server_list_match.group(1)
    # print(f"=== Server List Text (first 1000 chars) ===\n{server_list_text[:1000]}\n===================================") # Original debug

    # Regex for categories (e.g., "🌐 浏览器自动化与网页交互")
    # Further refined newline and optional group handling.
    category_regex = re.compile(
        r"^\s*([🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩].*?)\s*(?:\n\n\s*\(.*?\)\n)?\s*名称\s*\|\s*中文介绍\s*\|\s*备注\s*\n-*\|-+\|-+\n(.*?)(?=\n\n\s*[🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩]|\Z)",
        re.MULTILINE | re.DOTALL
    )
    # Explanation of further revised category_regex:
    # ^\s*([🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩].*?)\s*       # Group 1: Category title (starts with emoji)
    # (?:\n\n\s*\(.*?\)\n)?                           # Optional: \n\n, then parenthetical line, then \n
    # \s*名称\s*\|\s*中文介绍\s*\|\s*备注\s*\n          # Table header (now allows optional spaces before it)
    # -*\|-+\|-+\n                                  # Table delimiter line
    # (.*?)                                         # Group 2: Table content (non-greedy)
    # (?=\n\n\s*[🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩]|\Z) # Lookahead for next category start (emoji with optional leading spaces) or EOF
    
    # Regex for server entries within the table (each line of the table)
    # Example: "[129]microsoft/playwright-mcp | 微软官方出品... | 官方实现，浏览器自动化强推..."
    # Need to handle reference links like [129]
    server_entry_regex = re.compile(r"\[(\d+)\](.*?)\s*\|\s*(.*?)\s*\|\s*(.*)")
    # Group 1: ref_num for link
    # Group 2: name_text (might include English name or be Chinese)
    # Group 3: chinese_description
    # Group 4: remarks_text

    # Find the start of the actual list of categories to skip preamble
    first_category_start_match = re.search(r"\n\n\s*[🌐💻🖥️🔄🗄️☁️🔍💬💰📁📊🛠️🧠🔒🌍🏃🏛️🧩]", server_list_text)
    if not first_category_start_match:
        print("Could not find the start of the first category in the server list.")
        return servers
    
    actual_list_content = server_list_text[first_category_start_match.start():]
    # print(f"=== Actual List Content (first 1000 chars) ===\n{actual_list_content[:1000]}\n===================================") # Comment out debug print
    
    category_matches = list(category_regex.finditer(actual_list_content)) # Apply to the cleaned text
    # print(f"Found {len(category_matches)} potential categories.") # Comment out debug print

    # First, build the reference map for URLs from the "References" section at the bottom
    ref_to_url = {}
    references_section_match = re.search(r"\nReferences\n\n(.*?)(?:\nFooter\n|\n\nVisible links:|\Z)", text, re.DOTALL | re.IGNORECASE)
    if references_section_match:
        references_text = references_section_match.group(1)
        ref_line_regex = r"^\s*(\d+)\.\s*(https?://\S+)" # e.g., "   129. https://github.com/microsoft/playwright-mcp"
        for ref_match in re.finditer(ref_line_regex, references_text, re.MULTILINE):
            ref_num = ref_match.group(1)
            url = ref_match.group(2).strip()
            ref_to_url[ref_num] = url
    else:
        print("Warning: Could not find References section. URLs will be missing.")

    language_map = {
        '🐍': 'Python', '📇': 'TypeScript/JavaScript', '🏎️': 'Go',
        '🦀': 'Rust', '#️⃣': 'C#', '☕': 'Java', '🚀': 'Go' # Adding another for Go
    }
    platform_map = {'☁️': 'Cloud', '🏠': 'Local', '🍎': 'macOS', '🪟': 'Windows', '🐧': 'Linux', '📟': 'Embedded'}

    for i, category_match in enumerate(category_matches):
        category_title_full = category_match.group(1).strip()
        # Clean up category title (remove potential leading characters like emoji if needed, or just use full)
        category_name = category_title_full # For now, use the full matched title.
        # print(f"\n--- Processing Category {i+1}: {category_name} ---") # Comment out debug print
        
        table_content = category_match.group(2)
        # print(f"Table content for category '{category_name}':\n{table_content[:300]}\n---")

        # processed_in_category = 0 # Ensure this is commented out if the usage below is commented out
        for line in table_content.splitlines():
            line = line.strip()
            if not line or line.startswith('-') or line.startswith('|'): # Skip empty or horizontal rule lines
                continue

            server_match = server_entry_regex.match(line)
            if server_match:
                ref_num = server_match.group(1).strip()
                name_text = server_match.group(2).strip() # This usually is the repo name like "microsoft/playwright-mcp"
                chinese_description = server_match.group(3).strip()
                remarks_text = server_match.group(4).strip()

                repo_url = ref_to_url.get(ref_num, "")
                
                # Attempt to derive English name if name_text is like "user/repo"
                english_name = name_text
                if '/' in name_text:
                    english_name = name_text.split('/')[-1].replace('-', ' ').replace('_', ' ').title()

                tags = []
                language = None
                platforms = []
                
                if '官方实现' in remarks_text: tags.append('Official Implementation')
                if '官方参考' in remarks_text: tags.append('Official Reference')
                if '社区标杆' in remarks_text: tags.append('Community Benchmark')
                if '社区实现' in remarks_text: tags.append('Community Implementation')


                for icon, lang_name in language_map.items():
                    if icon in remarks_text:
                        language = lang_name
                        # tags.append(lang_name) # Language is a separate field
                        break # Assuming one primary language icon
                
                for icon, plat_name in platform_map.items():
                    if icon in remarks_text:
                        platforms.append(plat_name)
                
                # Add any remaining text in remarks as a general tag, removing icons
                cleaned_remarks = remarks_text
                for icon in list(language_map.keys()) + list(platform_map.keys()):
                    cleaned_remarks = cleaned_remarks.replace(icon, "")
                cleaned_remarks = cleaned_remarks.replace('官方实现', '').replace('官方参考', '').replace('社区标杆', '').replace('社区实现', '').strip(' ,.')
                if cleaned_remarks:
                    tags.append(cleaned_remarks)


                servers.append({
                    "name_zh": name_text, # The text from the link, often repo name
                    "name_en": english_name, 
                    "description_zh": chinese_description,
                    "category_zh": category_name,
                    "repository_url": repo_url,
                    "language": language,
                    "platforms": platforms,
                    "tags": list(set(tags)) # Remove duplicate tags
                })
                # processed_in_category +=1 # Comment out increment
            # else:
                # if line and not line.startswith("名称") and not line.startswith("---"): 
                    # print(f"Line did not match server entry regex: {line}") # Comment out debug print
        # print(f"Processed {processed_in_category} servers in category '{category_name}'.") # Comment out debug print (ensure var is defined if uncommented)
        
    return servers

if __name__ == "__main__":
    try:
        with open("awesome_zh_page.txt", "r", encoding="utf-8") as f:
            text_content = f.read()
    except FileNotFoundError:
        print("Error: awesome_zh_page.txt not found. Please create it with the website content.")
        exit(1)
        
    extracted_data = parse_awesome_mcp_zh(text_content)
    
    output_filename = "awesome_mcp_zh.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, indent=4, ensure_ascii=False) # ensure_ascii=False for Chinese
    
    print(f"Extracted {len(extracted_data)} servers and saved to {output_filename}")
