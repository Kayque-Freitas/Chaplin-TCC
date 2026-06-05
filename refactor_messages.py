import os
import re

def refactor_messages():
    base_dir = r"c:\Users\Administrator\Desktop\Chaplin-TCC"
    
    # 1. Remove messages blocks from all templates
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if 'venv' in root or '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    message_block_pattern = re.compile(r'{%\s*if messages\s*%}.*?{%\s*endif\s*%}', re.DOTALL)
    
    for filepath in html_files:
        # Don't remove from base_dashboard if we just added it, or we will handle it explicitly
        if 'base_dashboard.html' in filepath:
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if '{% if messages %}' in content:
            # remove it
            new_content = message_block_pattern.sub('', content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                print(f"Removed messages block from {filepath}")
                
    # 2. Add messages block to base_dashboard.html
    base_path = os.path.join(base_dir, 'templates', 'shared', 'base_dashboard.html')
    with open(base_path, 'r', encoding='utf-8') as f:
        base_content = f.read()
        
    messages_snippet = """
            <!-- Global Messages -->
            {% if messages %}
            <div class="px-4 sm:px-6 lg:px-8 pt-6 pb-2" id="global-messages">
                <div class="space-y-2">
                    {% for message in messages %}
                    <div class="message-alert p-4 rounded-lg shadow-sm flex justify-between items-center {% if message.tags == 'success' %}bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400 border border-green-200 dark:border-green-800{% elif message.tags == 'error' %}bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400 border border-red-200 dark:border-red-800{% else %}bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400 border border-blue-200 dark:border-blue-800{% endif %} transition-all duration-500">
                        <span>{{ message }}</span>
                        <button type="button" onclick="this.parentElement.style.display='none'" class="ml-4 opacity-50 hover:opacity-100 font-bold text-lg leading-none">&times;</button>
                    </div>
                    {% endfor %}
                </div>
            </div>
            <script>
                // Auto-dismiss messages after 5 seconds
                setTimeout(() => {
                    document.querySelectorAll('.message-alert').forEach(el => {
                        el.style.opacity = '0';
                        setTimeout(() => el.style.display = 'none', 500);
                    });
                }, 5000);
            </script>
            {% endif %}
            """
            
    if "Global Messages" not in base_content:
        base_content = base_content.replace('{% block content %}{% endblock %}', messages_snippet + '{% block content %}{% endblock %}')
        with open(base_path, 'w', encoding='utf-8') as f:
            f.write(base_content)
        print("Added global messages to base_dashboard.html")

if __name__ == "__main__":
    refactor_messages()
