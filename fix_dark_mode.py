import os

def update_create_html():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\create.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply dark mode to create.html
    replacements = {
        'class="text-3xl font-bold text-gray-900"': 'class="text-3xl font-bold text-gray-900 dark:text-white"',
        'class="text-gray-600 mt-2"': 'class="text-gray-600 dark:text-gray-400 mt-2"',
        'bg-white rounded-xl shadow-sm border border-gray-200': 'bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700',
        'text-lg font-bold text-gray-800 border-b border-gray-100': 'text-lg font-bold text-gray-800 dark:text-white border-b border-gray-100 dark:border-gray-700',
        'block text-sm font-medium text-gray-700 mb-1': 'block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1',
        'text-sm font-semibold text-gray-700 mb-3': 'text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3',
        'border-gray-300 hover:bg-gray-50 text-gray-700': 'border-gray-300 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300',
        'border-t border-dashed border-gray-200 pt-5': 'border-t border-dashed border-gray-200 dark:border-gray-700 pt-5',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def update_forms_py():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\apps\tasks\forms.py"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Forms inputs: replace base classes with dark variants
    old_input_class = "'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500'"
    new_input_class = "'class': 'w-full px-4 py-2 bg-white dark:bg-gray-900 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:border-orange-500'"

    old_readonly_class = "'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-orange-500 bg-gray-50'"
    new_readonly_class = "'class': 'w-full px-4 py-2 bg-gray-50 dark:bg-gray-800 text-gray-900 dark:text-white border border-gray-300 dark:border-gray-600 rounded-lg focus:outline-none focus:border-orange-500'"

    content = content.replace(old_readonly_class, new_readonly_class)
    content = content.replace(old_input_class, new_input_class)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_create_html()
    update_forms_py()
    print("Done")
