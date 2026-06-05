import os

def update_kanban_html():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\kanban.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for Kanban template
    replacements = {
        'class="text-3xl font-bold text-gray-900"': 'class="text-3xl font-bold text-gray-900 dark:text-white"',
        'class="text-gray-500 mt-1"': 'class="text-gray-500 dark:text-gray-400 mt-1"',
        'bg-white rounded-lg shadow-sm border border-gray-200 p-1': 'bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-1',
        'text-gray-500 hover:text-gray-700 hover:bg-gray-50': 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-white hover:bg-gray-50 dark:hover:bg-gray-700',
        
        # Columns
        'bg-gray-100 rounded-xl p-4': 'bg-gray-100 dark:bg-gray-800/50 rounded-xl p-4',
        'text-sm font-bold text-gray-700 uppercase tracking-wide': 'text-sm font-bold text-gray-700 dark:text-gray-300 uppercase tracking-wide',
        
        # Cards
        'block bg-white rounded-lg shadow-sm border border-gray-200 p-4': 'block bg-white dark:bg-gray-800 rounded-lg shadow-sm border border-gray-200 dark:border-gray-700 p-4',
        
        # Text inside cards
        'font-semibold text-gray-800 group-hover:text-orange-600': 'font-semibold text-gray-800 dark:text-white group-hover:text-orange-600 dark:group-hover:text-orange-400',
        'font-semibold text-gray-700 group-hover:text-orange-600 text-sm mb-2 line-through': 'font-semibold text-gray-700 dark:text-gray-300 group-hover:text-orange-600 dark:group-hover:text-orange-400 text-sm mb-2 line-through',
        'text-xs text-gray-500 mb-3': 'text-xs text-gray-500 dark:text-gray-400 mb-3',
        'border-t border-gray-100': 'border-t border-gray-100 dark:border-gray-700',
        'text-xs text-gray-500">{% if': 'text-xs text-gray-500 dark:text-gray-400">{% if',
        
        # Empty states
        'text-gray-400 text-sm': 'text-gray-400 dark:text-gray-500 text-sm',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_kanban_html()
    print("Done Kanban")
