import os
import re

docs_dir = r"c:\Users\Administrator\Desktop\Chaplin-TCC\static\docs"

replacements = [
    # SCRIPT_APRESENTACAO_15MIN.md
    (r"Um problema é notado no quarto", "Um problema é notado no local/setor"),
    (r"- \*\*Segurança\*\*: Autenticação robusta e Segundo Fator \(2FA\) via QR Code.", "- **Segurança**: Autenticação robusta estendida com suporte completo no Django."),
    
    # RESUMO_GRUPO.md
    (r"### 1. Autenticação e 2FA", "### 1. Autenticação"),
    (r"- \*\*2FA\*\*: Utiliza a biblioteca `pyotp` para gerar códigos temporários que o usuário escaneia via Google Authenticator.\n", ""),
    
    # RESUMO_COMPLETO.md
    (r"\| 2FA \| pyotp \+ qrcode \|\n", ""),
    (r"UserProfile \(role, 2FA, especialidade, endereço\)", "UserProfile (role, especialidade, endereço)"),
    (r"UserProfile \(role, 2FA\)", "UserProfile (role)"),
    (r"Login, registro, 2FA, perfil, admin de contas", "Login, registro, perfil, admin de contas"),
    (r"Templates de login/2FA/admin", "Templates de login/admin"),
    (r"- \*\*2FA\*\* opcional via TOTP \(pyotp\)\. Fluxo: setup QR → confirma código → ativa\.\n", ""),
    (r"Role, 2FA, especialidade", "Role, especialidade"),
    (r"\| Ativar 2FA \| `/usuarios/2fa/configurar/` \|.*\n", ""),
    (r"\(credenciais inválidas, 2FA pendente, sessões expiradas\)", "(credenciais inválidas, sessões expiradas)"),
    (r"- Garantir que o fluxo 2FA \(setup → verificação → desativação\) está funcional e seguro\.\n", ""),
    (r"login com senha errada, fluxo 2FA\.", "login com senha errada."),
    (r"7\. \*\*`mysqlclient` no `requirements.txt`\*\* — desnecessário se usar apenas SQLite/PostgreSQL\. Remover para evitar erros de build\.\n", ""),

    # REQUISITOS_CHAPLIN.md
    (r"- \*\*RF1\.3\*\*: O sistema deve oferecer a opção de Ativar Autenticação de Dois Fatores \(2FA\) para maior segurança\.\n", ""),
    (r"quarto/local", "local/setor"),

    # CHAPLIN_TCC_DOCUMENTO_REFORMULADO.md
    (r"inspeção do quarto", "inspeção do local/setor"),
    (r"Número do quarto", "Local / Setor"),
    (r"vencimento, quarto", "vencimento, local/setor"),
    (r"\| \*\*Banco de Dados\*\* \| MySQL \|", "| **Banco de Dados** | PostgreSQL/SQLite |"),
    (r"MySQL DB", "PostgreSQL"),
    (r"- MySQL: https://www\.mysql\.com/", "- PostgreSQL: https://www.postgresql.org/"),
    
    # CHAPLIN_INTERFACE_INTUITIVA.md
    (r"Número do Quarto", "Local / Setor"),

    # ARQUITETURA_TECNICA.md
    (r"como o segredo do 2FA\.", "como as informações de endereço.")
]

for filename in os.listdir(docs_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(docs_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

print("Done alignment.")
