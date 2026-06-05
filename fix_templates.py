import os
import re

def fix_broken_templates():
    files_to_fix = [
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\apps\users\templates\users\admin\list.html",
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\users\verify_email.html",
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\settings.html",
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\detail.html",
        r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\complete.html",
    ]
    
    broken_pattern = re.compile(r'">\s*\{\{\s*message\s*\}\}\s*</div>\s*{%\s*endfor\s*%}\s*</div>\s*{%\s*endif\s*%}', re.DOTALL)
    
    for filepath in files_to_fix:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            new_content = broken_pattern.sub('', content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed {filepath}")

if __name__ == "__main__":
    fix_broken_templates()
