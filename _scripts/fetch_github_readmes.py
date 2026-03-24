import urllib.request
import json
import os
import re

USERNAME = "vyvas33"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECTS_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), "_projects")

def get_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching repos: {e}")
        return []

def get_readme(repo_name):
    # Try main, then master
    for branch in ["main", "master"]:
        url = f"https://raw.githubusercontent.com/{USERNAME}/{repo_name}/{branch}/README.md"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req) as response:
                content = response.read().decode('utf-8')
                return content, branch
        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            else:
                print(f"Error fetching README for {repo_name} on {branch}: {e}")
    return None, None

def process_readme(content, repo_name, branch):
    # Fix relative image links: ![alt](img.png) -> ![alt](https://raw.githubusercontent.com/vyvas33/repo_name/branch/img.png)
    base_url = f"https://raw.githubusercontent.com/{USERNAME}/{repo_name}/{branch}/"
    
    def replace_img(match):
        alt = match.group(1)
        src = match.group(2)
        if not src.startswith("http") and not src.startswith("/") and not src.startswith("data:"):
            src = base_url + src
        return f"![{alt}]({src})"
        
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_img, content)
    
    # Also fix hrefs (basic links)
    def replace_link(match):
        text = match.group(1)
        href = match.group(2)
        if not href.startswith("http") and not href.startswith("#") and not href.startswith("mailto:") and not href.startswith("/"):
            href = f"https://github.com/{USERNAME}/{repo_name}/blob/{branch}/{href}"
        return f"[{text}]({href})"
        
    content = re.sub(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)', replace_link, content)
    
    # Strip the very first top-level heading if it exists so it's not redundant with Jekyll's title
    content = re.sub(r'^\s*#\s+[^\n]+\n+', '', content)
    
    return content

def main():
    if not os.path.exists(PROJECTS_DIR):
        print(f"Projects directory not found at {PROJECTS_DIR}. Creating it...")
        os.makedirs(PROJECTS_DIR)
        
    print("Fetching repositories...")
    repos = get_repos()
    print(f"Found {len(repos)} repositories for user {USERNAME}.")
    
    # Only allow the specified projects
    ALLOWED_REPOS = [
        'hopping_model',
        'muscle_model',
        'articulated_mobile_robot',
        'gesture_controlled_sma_robotic_hand',
        'synthetic_jets'
    ]
    
    count = 0
    for repo in repos:
        name = repo['name']
        description = repo.get('description') or ""
        
        if name not in ALLOWED_REPOS:
            continue
            
        readme_content, branch = get_readme(name)
        if not readme_content:
            print(f"Skipping {name} (No README found)")
            continue
            
        print(f"Processing {name}...")
        processed_content = process_readme(readme_content, name, branch)
        
        description_clean = description.replace('"', '\\"')
        name_title = ' '.join(word.capitalize() for word in name.replace('_', ' ').replace('-', ' ').split())
        
        frontmatter = f"""---
layout: page
title: {name_title}
description: "{description_clean}"
importance: 3
category: work
github: {USERNAME}/{name}
---

"""
        file_path = os.path.join(PROJECTS_DIR, f"{name}.md")
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(frontmatter + processed_content)
        print(f"Created/updated {file_path}")
        count += 1
        
    print(f"\\nSuccessfully processed {count} repositories.")

if __name__ == "__main__":
    main()
