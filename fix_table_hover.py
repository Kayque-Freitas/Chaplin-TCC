import os
import re

def fix_hovers():
    base_dir = r"c:\Users\Administrator\Desktop\Chaplin-TCC"
    
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if 'venv' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Replace hover:bg-gray-50 dark:hover:bg-gray-750 with dark:hover:bg-gray-700
        if 'dark:hover:bg-gray-750' in content:
            content = content.replace('dark:hover:bg-gray-750', 'dark:hover:bg-gray-700')
            modified = True
            
        # Replace dark:hover:bg-gray-700/50 with dark:hover:bg-gray-700 just to be safe
        if 'dark:hover:bg-gray-700/50' in content:
            content = content.replace('dark:hover:bg-gray-700/50', 'dark:hover:bg-gray-700')
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed hover in {filepath}")

if __name__ == "__main__":
    fix_hovers()
