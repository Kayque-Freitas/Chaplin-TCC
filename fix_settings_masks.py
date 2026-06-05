import os

def update_settings_html():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\settings.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace phone and cep to include mask classes
    content = content.replace('name="phone" id="phone" value="{{ user_profile.phone }}" class="w-full px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-orange-500 focus:outline-none dark:text-white"',
                              'name="phone" id="phone" value="{{ user_profile.phone }}" class="w-full px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-orange-500 focus:outline-none dark:text-white mask-phone"')
    
    content = content.replace('name="cep" id="cep" value="{{ user_profile.cep }}" class="w-full px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-orange-500 focus:outline-none dark:text-white"',
                              'name="cep" id="cep" value="{{ user_profile.cep }}" class="w-full px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-orange-500 focus:outline-none dark:text-white mask-cep"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_settings_html()
