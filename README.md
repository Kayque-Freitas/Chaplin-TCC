# Chaplin - Field Service Management (FSM)

Chaplin é um sistema de Gestão de Ordens de Serviço (Work Orders) desenvolvido como Trabalho de Conclusão de Curso (TCC). O foco principal do sistema é gerenciar tarefas de campo, manutenções e suportes de forma ágil, fluida e com extrema empatia pelo usuário final que possui baixo letramento digital. 

## Principais Funcionalidades

- **Fluxo de Tarefas Bem Definido:** Transições de status restritas e seguras (Aberta &rarr; Alocada &rarr; Concluída &rarr; Finalizada).
- **Perfis de Acesso (RBAC):** Visões e permissões adaptadas para Gestores (visão macro), Líderes (distribuição) e Colaboradores (execução).
- **Geolocalização:** Endereçamento completo nas tarefas (CEP, Bairro, Rua) para viabilizar serviços de campo.
- **Evidências Físicas:** Upload de fotos para auditar e comprovar a conclusão dos serviços (`TaskEvidence`).
- **Comunicação Interna:** Troca de mensagens vinculada diretamente a cada tarefa.
- **Design Minimalista e Inclusivo:** Interface otimizada construída com Tailwind CSS (incluindo Dark Mode), focada em diminuir a curva de aprendizado. Conta também com um layout responsivo e preparado para dispositivos mobile.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Django
- **Frontend:** HTML5, Tailwind CSS, JavaScript Vanilla
- **Banco de Dados:** SQLite (Dev) / PostgreSQL (Prod)

---

## 📋 Pré-requisitos

Certifique-se de ter instalado em sua máquina:
- **Python 3.10+** (ou superior)
- **Pip** (Gerenciador de pacotes do Python)
- **Git** (Para clonar o repositório)

## 💻 Como Rodar o Projeto Localmente

Siga o passo a passo abaixo para rodar o projeto na sua máquina (utilizando SQLite como padrão para desenvolvimento rápido):

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Chaplin-TCC.git
   cd Chaplin-TCC
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # Linux/Mac
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto. Você precisará de uma chave de segurança secreta para o Django. Para gerar uma chave segura, rode no terminal:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```
   Em seguida, coloque o conteúdo abaixo dentro do seu arquivo `.env`:
   ```env
   SECRET_KEY=cole_a_chave_gerada_aqui
   DEBUG=True
   ```

5. **Aplique as Migrations (Cria o banco de dados):**
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário (Gestor):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Rode o servidor:**
   ```bash
   python manage.py runserver
   ```
   Acesse: `http://localhost:8000`

### 🔑 Acesso Rápido (Contas Padrão)

O banco de dados SQLite já acompanha os 4 perfis de usuários pré-configurados para você testar imediatamente o sistema, sem precisar criar dados do zero. Todas as contas possuem a mesma senha padrão:

| Perfil | Usuário (Login) | Senha |
| --- | --- | --- |
| **Admin do Sistema** | `admin` | `chaplin123` |
| **Gestor** | `gestor` | `chaplin123` |
| **Líder** | `lider` | `chaplin123` |
| **Colaborador** | `colaborador` | `chaplin123` |

---

## 🐘 Como Migrar de SQLite para PostgreSQL

O projeto vem configurado para usar o SQLite, o que é ótimo para testes e desenvolvimento rápido. No entanto, para ambientes de produção, recomendamos fortemente o PostgreSQL. 

Veja como realizar a migração:

### 1. Instalar as dependências do Postgres
Com o ambiente virtual ativado, instale o driver do PostgreSQL para o Python:
```bash
pip install psycopg2-binary
```
*(Não se esqueça de rodar `pip freeze > requirements.txt` para atualizar suas dependências no repositório).*

### 2. Criar o Banco de Dados no Postgres
No seu gerenciador de banco de dados (como pgAdmin ou DBeaver) ou via terminal (`psql`), crie um novo banco de dados. Exemplo:
```sql
CREATE DATABASE chaplin_db;
CREATE USER chaplin_user WITH PASSWORD 'sua_senha_segura';
ALTER ROLE chaplin_user SET client_encoding TO 'utf8';
ALTER ROLE chaplin_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE chaplin_user SET timezone TO 'America/Sao_Paulo';
GRANT ALL PRIVILEGES ON DATABASE chaplin_db TO chaplin_user;
```

### 3. Atualizar o `settings.py`
Vá até `chaplin_project/settings.py` e localize o dicionário `DATABASES`. Substitua a configuração antiga pela seguinte:

```python
import os
# Comente ou apague a configuração do SQLite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Adicione a nova configuração do Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'chaplin_db', # ou os.environ.get('DB_NAME')
        'USER': 'chaplin_user',
        'PASSWORD': 'sua_senha_segura',
        'HOST': 'localhost', # ou o IP do seu servidor Postgres
        'PORT': '5432',
    }
}
```

> **Dica de Segurança:** É altamente recomendado que você coloque as informações de `NAME`, `USER`, e `PASSWORD` dentro do seu arquivo `.env` e carregue-os no `settings.py` usando `os.getenv('DB_NAME')` ou a biblioteca `python-decouple`, para não vazar senhas no GitHub.

### 4. Rodar as Migrations no Novo Banco
Como o banco Postgres está zerado, você precisará criar as tabelas novamente:
```bash
python manage.py migrate
python manage.py createsuperuser
```

E pronto! Seu projeto já está rodando em PostgreSQL.

---
*Desenvolvido com dedicação como Trabalho de Conclusão de Curso.*
