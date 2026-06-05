import os

def update_notifications_html():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\notifications.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for Notifications template
    replacements = {
        'class="text-3xl font-bold text-gray-900"': 'class="text-3xl font-bold text-gray-900 dark:text-white"',
        'class="text-gray-500 mt-1"': 'class="text-gray-500 dark:text-gray-400 mt-1"',
        'bg-white rounded-xl border border-gray-200 shadow-sm p-5 flex items-start gap-4': 'bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm p-5 flex items-start gap-4',
        
        # Icons bg
        "{% if notif.tipo == 'tarefa_atribuida' %}bg-blue-100": "{% if notif.tipo == 'tarefa_atribuida' %}bg-blue-100 dark:bg-blue-900/30",
        "{% elif notif.tipo == 'tarefa_concluida' %}bg-green-100": "{% elif notif.tipo == 'tarefa_concluida' %}bg-green-100 dark:bg-green-900/30",
        "{% elif notif.tipo == 'nova_mensagem' %}bg-purple-100": "{% elif notif.tipo == 'nova_mensagem' %}bg-purple-100 dark:bg-purple-900/30",
        "{% elif notif.tipo == 'tarefa_criada' %}bg-yellow-100": "{% elif notif.tipo == 'tarefa_criada' %}bg-yellow-100 dark:bg-yellow-900/30",
        "{% else %}bg-gray-100{% endif %}": "{% else %}bg-gray-100 dark:bg-gray-700{% endif %}",
        
        # Text inside content
        'class="font-semibold text-gray-900 text-sm"': 'class="font-semibold text-gray-900 dark:text-white text-sm"',
        'class="text-sm text-gray-600 mt-1"': 'class="text-sm text-gray-600 dark:text-gray-300 mt-1"',
        
        # Empty states
        'class="text-center py-20 text-gray-400"': 'class="text-center py-20 text-gray-400 dark:text-gray-500"',
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_notifications_html()
    print("Done Notifications")
