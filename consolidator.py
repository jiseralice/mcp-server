import json
import os
import re

# Helper to normalize repo URLs for better matching (remove trailing slashes, .git)
def normalize_repo_url(url):
    if not url or not isinstance(url, str):
        return ""
    url = url.lower()
    if url.endswith('/'):
        url = url[:-1]
    if url.endswith('.git'):
        url = url[:-4]
    return url

# Helper to merge data from a new entry into an existing one
def merge_entries(existing_entry, new_entry, new_source_filename):
    # Prioritize non-empty fields and specific sources if needed
    # For descriptions, try to keep both if they are different and one is potentially a translation
    
    # Standardize incoming fields first
    new_name = new_entry.get("name", new_entry.get("name_en"))
    new_name_zh = new_entry.get("name_zh")
    new_desc = new_entry.get("description", new_entry.get("description_en"))
    new_desc_zh = new_entry.get("description_zh")
    new_cat_en = new_entry.get("category", new_entry.get("category_en")) # 'category' from awesome-mcp-servers
    new_cat_zh = new_entry.get("category_zh")

    # Name merging
    if not existing_entry.get("name") and new_name: # Primary English name
        existing_entry["name"] = new_name
    if not existing_entry.get("name_zh") and new_name_zh:
        existing_entry["name_zh"] = new_name_zh
    # If existing name is a placeholder and new name is more descriptive
    if existing_entry.get("name") and "(Fallback Name)" in existing_entry["name"] and new_name and "(Fallback Name)" not in new_name:
        existing_entry["name"] = new_name

    # Description merging
    if not existing_entry.get("description") and new_desc:
        existing_entry["description"] = new_desc
    if not existing_entry.get("description_zh") and new_desc_zh:
        existing_entry["description_zh"] = new_desc_zh
    # If descriptions are different, and one is clearly longer/better or a translation
    if new_desc and existing_entry.get("description") and new_desc.lower() != existing_entry["description"].lower():
        if len(new_desc) > len(existing_entry["description"]) and not new_desc_zh: # Prefer longer English desc
            existing_entry["description"] = new_desc
    if new_desc_zh and existing_entry.get("description_zh") and new_desc_zh.lower() != existing_entry["description_zh"].lower():
         if len(new_desc_zh) > len(existing_entry["description_zh"]): # Prefer longer Chinese desc
            existing_entry["description_zh"] = new_desc_zh


    # Language merging - ensure it's a list and unique
    current_langs = set(existing_entry.get("languages", []))
    # Handle 'language' (singular, from awesome-mcp-servers) and 'languages' (list, from others)
    raw_new_langs = new_entry.get("language", new_entry.get("languages", []))
    if not isinstance(raw_new_langs, list):
        raw_new_langs = [raw_new_langs] if raw_new_langs else []
    
    for lang in raw_new_langs:
        if lang and isinstance(lang, str): # Basic validation
            # Normalize common variations
            if lang.lower() == "typescript/javascript" or lang.lower() == "javascript":
                current_langs.add("TypeScript") # Standardize to TypeScript if JS is mentioned
                current_langs.add("JavaScript")
            elif lang.lower() == "go" or lang.lower() == "golang":
                current_langs.add("Go")
            else:
                current_langs.add(lang.capitalize())
    existing_entry["languages"] = sorted(list(filter(None, current_langs)))


    # Category merging - try to get both English and Chinese if available
    if not existing_entry.get("category_en") and new_cat_en:
        existing_entry["category_en"] = new_cat_en
    if not existing_entry.get("category_zh") and new_cat_zh:
        existing_entry["category_zh"] = new_cat_zh
    # If new category is more descriptive (e.g. not a generic one)
    if new_cat_en and existing_entry.get("category_en") and \
       new_cat_en.lower() not in ["other tools and integrations", "developer tools"] and \
       existing_entry["category_en"].lower() in ["other tools and integrations", "developer tools"]:
        existing_entry["category_en"] = new_cat_en


    # Tags and Platforms merging
    for field in ["tags", "platforms"]:
        existing_items = set(existing_entry.get(field, []))
        new_items_raw = new_entry.get(field, [])
        if not isinstance(new_items_raw, list): new_items_raw = [new_items_raw] if new_items_raw else []
        
        for item in new_items_raw:
            if item and isinstance(item, str): # Ensure items are valid strings
                 existing_items.add(item.strip())
        existing_entry[field] = sorted(list(filter(None, existing_items)))

    if new_source_filename not in existing_entry["source_files"]:
        existing_entry["source_files"].append(new_source_filename)
        existing_entry["source_files"].sort()
        
    return existing_entry

def main():
    files_to_process = [
        "mcp_servers.json",
        "awslabs_mcp_servers.json",
        "playwright_mcp_server.json",
        "github_mcp_server.json",
        "browsermcp_server.json",
        "whatsapp_mcp_server.json",
        "n8n_nodes_mcp.json",
        "figma_context_mcp.json",
        "awesome_mcp_zh.json"
    ]

    consolidated_servers = {} # Use repo_url as key for de-duplication

    # Define a loose priority for sources if a conflict occurs beyond simple field merging
    # Lower number means higher priority if we need to decide which 'base' entry to keep.
    # This can be used if we decide to overwrite existing entries rather than just merge fields.
    # For now, the merge_entries function tries to intelligently combine.
    # source_priority = {
    #     "mcp_servers.json": 1, 
    #     "awesome_mcp_zh.json": 2, 
    #     "github_mcp_server.json": 3, ...
    # }

    # Basic category mapping (can be expanded)
    # Key: category from individual file, Value: standardized English category
    category_map = {
        "Browser Automation": "Browser Automation", # Already good
        "Version Control": "Version Control",       # Already good
        "Communication": "Communication",           # Already good
        "Design Tools": "Developer Tools",          # Map to broader category
        "Workflow Automation": "Developer Tools",   # Map to broader category
        # Categories from awesome-mcp-zh (map by emoji or Chinese name if needed)
        # Example: "🌐 浏览器自动化与网页交互": "Browser Automation", (parser already extracts this)
    }


    for filename in files_to_process:
        if not os.path.exists(filename):
            print(f"Warning: File {filename} not found. Skipping.")
            continue
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: File {filename} contains invalid JSON. Skipping.")
            continue

        for entry in data:
            repo_url = normalize_repo_url(entry.get("repository_url"))
            
            # Use name as part of key if repo_url is empty (less reliable)
            unique_key = repo_url
            if not unique_key:
                name_en = entry.get("name", entry.get("name_en", "")).strip().lower()
                name_zh = entry.get("name_zh", "").strip().lower()
                if name_en or name_zh: # Only use name if available
                    unique_key = f"name:{name_en}|{name_zh}" 
                else: # Cannot reliably de-duplicate
                    # Add it with a unique-enough key or handle as a separate list
                    # If no URL and no name, it's hard to process reliably, might skip or log
                    print(f"Skipping entry with no URL and no identifiable name in {filename}: {str(entry)[:100]}")
                    continue

            # Standardize the new entry before merging or adding
            current_name_en = entry.get("name", entry.get("name_en"))
            current_name_zh = entry.get("name_zh")
            current_desc_en = entry.get("description", entry.get("description_en"))
            current_desc_zh = entry.get("description_zh")
            current_cat_en = entry.get("category", entry.get("category_en")) # 'category' from awesome-mcp-servers
            current_cat_zh = entry.get("category_zh")
            
            # Apply category mapping for English category
            if current_cat_en and category_map.get(current_cat_en):
                current_cat_en = category_map[current_cat_en]
            elif current_cat_en and "mcp server" in current_cat_en.lower(): # Generic fallback
                 current_cat_en = "Other Tools and Integrations"


            # Standardize languages for the current entry
            raw_langs = entry.get("language", entry.get("languages", []))
            if not isinstance(raw_langs, list): raw_langs = [raw_langs] if raw_langs else []
            processed_langs = set()
            for lang_item in raw_langs:
                if lang_item and isinstance(lang_item, str):
                    if lang_item.lower() == "typescript/javascript" or lang_item.lower() == "javascript":
                        processed_langs.add("TypeScript")
                        processed_langs.add("JavaScript")
                    elif lang_item.lower() == "go" or lang_item.lower() == "golang":
                        processed_langs.add("Go")
                    else:
                        processed_langs.add(lang_item.capitalize())
            
            standardized_new_entry = {
                "name": current_name_en,
                "name_en": current_name_en,
                "name_zh": current_name_zh,
                "description": current_desc_en,
                "description_zh": current_desc_zh,
                "category_en": current_cat_en,
                "category_zh": current_cat_zh,
                "repository_url": entry.get("repository_url"),
                "normalized_repo_url": repo_url,
                "languages": sorted(list(filter(None, processed_langs))),
                "platforms": entry.get("platforms", []),
                "tags": entry.get("tags", []),
                "source_files": [filename] # Initial source
            }


            if unique_key in consolidated_servers:
                consolidated_servers[unique_key] = merge_entries(consolidated_servers[unique_key], standardized_new_entry, filename)
            else:
                consolidated_servers[unique_key] = standardized_new_entry
                
    final_list = list(consolidated_servers.values())

    # Post-processing: One final pass for category and language consistency if needed
    for server in final_list:
        if server.get("category_en") and category_map.get(server["category_en"]):
            server["category_en"] = category_map[server["category_en"]]
        if not server.get("languages"): # Ensure languages field is present
            server["languages"] = []
        if not server.get("platforms"):
            server["platforms"] = []
        if not server.get("tags"):
            server["tags"] = []


    output_filename = "consolidated_mcp_servers.json"
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(final_list, f, indent=4, ensure_ascii=False)

    print(f"Consolidated {len(final_list)} servers into {output_filename}")

if __name__ == "__main__":
    main()
