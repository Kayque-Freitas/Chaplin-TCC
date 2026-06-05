import os
import re

def update_maxlengths():
    filepath = r"c:\Users\Administrator\Desktop\Chaplin-TCC\templates\tasks\settings.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define replacements for inputs to add maxlength
    replacements = {
        'id="first_name" name="first_name" value="{{ user.first_name }}" class': 'id="first_name" name="first_name" value="{{ user.first_name }}" maxlength="150" class',
        'id="last_name" name="last_name" value="{{ user.last_name }}" class': 'id="last_name" name="last_name" value="{{ user.last_name }}" maxlength="150" class',
        'id="email" name="email" value="{{ user.email }}" class': 'id="email" name="email" value="{{ user.email }}" maxlength="254" class',
        'id="phone" name="phone" value="{{ user_profile.phone }}" placeholder="(00) 00000-0000" class': 'id="phone" name="phone" value="{{ user_profile.phone }}" placeholder="(00) 00000-0000" maxlength="20" class',
        'id="phone" name="phone" value="{{ user_profile.phone }}" class': 'id="phone" name="phone" value="{{ user_profile.phone }}" maxlength="20" class',
        'id="logradouro" name="logradouro" value="{{ user_profile.logradouro }}" class': 'id="logradouro" name="logradouro" value="{{ user_profile.logradouro }}" maxlength="255" class',
        'id="numero" name="numero" value="{{ user_profile.numero }}" class': 'id="numero" name="numero" value="{{ user_profile.numero }}" maxlength="20" class',
        'id="complemento" name="complemento" value="{{ user_profile.complemento }}" placeholder="Apto, Bloco, etc." class': 'id="complemento" name="complemento" value="{{ user_profile.complemento }}" placeholder="Apto, Bloco, etc." maxlength="100" class',
        'id="bairro" name="bairro" value="{{ user_profile.bairro }}" class': 'id="bairro" name="bairro" value="{{ user_profile.bairro }}" maxlength="100" class',
        'id="cidade" name="cidade" value="{{ user_profile.cidade }}" class': 'id="cidade" name="cidade" value="{{ user_profile.cidade }}" maxlength="100" class',
        'id="estado" name="estado" value="{{ user_profile.estado }}" class': 'id="estado" name="estado" value="{{ user_profile.estado }}" maxlength="2" class',
    }

    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
        else:
            # Handle if there are slight variations
            pattern = old.replace('class', r'class')
            content = re.sub(pattern, new, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_maxlengths()
