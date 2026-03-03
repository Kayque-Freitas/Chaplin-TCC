# 🚀 Guia Completo: Como Rodar o Chaplin Django Localmente

Este guia passo-a-passo vai te ensinar a configurar e rodar o projeto Chaplin na sua máquina.

---

## 📋 Pré-requisitos

Antes de começar, você precisa ter instalado:

1. **Python 3.8+** - [Baixar aqui](https://www.python.org/downloads/)
2. **MySQL 5.7+** - [Baixar aqui](https://dev.mysql.com/downloads/mysql/)
3. **Git** - [Baixar aqui](https://git-scm.com/downloads)
4. **VS Code** (opcional) - [Baixar aqui](https://code.visualstudio.com/)

### Verificar Instalação

Abra o terminal/prompt de comando e execute:

```bash
python --version
mysql --version
git --version
```

Se todos retornarem versões, está tudo certo!

---

## 🔧 Passo 1: Clonar o Repositório

Abra o terminal e execute:

```bash
# Navegar para a pasta onde quer clonar
cd Documentos

# Clonar o repositório
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git

# Entrar na pasta do projeto
cd Chaplin-TCC
```

---

## 🐍 Passo 2: Criar Ambiente Virtual

O ambiente virtual isola as dependências do projeto.

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Você verá `(venv)` no início da linha do terminal.

### Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 Passo 3: Instalar Dependências

Com o ambiente virtual ativo, execute:

```bash
pip install -r requirements.txt
```

Isso vai instalar:
- Django 4.2
- mysqlclient (driver MySQL)
- python-decouple (variáveis de ambiente)
- Pillow (processamento de imagens)
- django-crispy-forms (formulários estilizados)

---

## 🗄️ Passo 4: Configurar Banco de Dados MySQL

### 4.1 Criar Banco de Dados

Abra o MySQL Workbench ou execute no terminal:

```bash
mysql -u root -p
```

Digite sua senha do MySQL (padrão é vazio se não configurou).

Depois execute:

```sql
CREATE DATABASE chaplin_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'chaplin_user'@'localhost' IDENTIFIED BY 'chaplin123';
GRANT ALL PRIVILEGES ON chaplin_db.* TO 'chaplin_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 4.2 Criar Arquivo .env

Na pasta do projeto, crie um arquivo chamado `.env`:

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Abra o arquivo `.env` e configure:

```
SECRET_KEY=django-insecure-chaplin-dev-key-change-in-production
DEBUG=True

DB_NAME=chaplin_db
DB_USER=chaplin_user
DB_PASSWORD=chaplin123
DB_HOST=localhost
DB_PORT=3306
```

---

## 🔄 Passo 5: Executar Migrações

As migrações criam as tabelas no banco de dados.

```bash
python manage.py migrate
```

Você vai ver várias linhas como:
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

## 👤 Passo 6: Criar Superusuário (Admin)

Execute:

```bash
python manage.py createsuperuser
```

Siga as instruções:

```
Username: admin
Email address: admin@chaplin.com
Password: 
Password (again): 
Superuser created successfully.
```

---

## 🎯 Passo 7: Rodar o Servidor

Execute:

```bash
python manage.py runserver
```

Você vai ver:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

---

## 🌐 Passo 8: Acessar a Aplicação

Abra seu navegador e acesse:

- **Home**: `http://localhost:8000/`
- **Admin**: `http://localhost:8000/admin/`
- **Login**: `http://localhost:8000/users/login/`

### Credenciais Padrão:

- **Username**: admin
- **Password**: (a que você criou no passo 6)

---

## 📊 Estrutura de Pastas Importante

```
Chaplin-TCC/
├── manage.py                 ← Executar comandos Django
├── requirements.txt          ← Dependências do projeto
├── .env                      ← Configurações (criar manualmente)
├── chaplin_project/          ← Configurações principais
├── apps/
│   ├── users/               ← Login, registro, perfil
│   ├── tasks/               ← CRUD de tarefas
│   └── core/                ← Home, about
├── templates/               ← Arquivos HTML
├── static/                  ← CSS, JS, imagens
└── media/                   ← Fotos enviadas pelos usuários
```

---

## 🐛 Troubleshooting (Solução de Problemas)

### Erro: "ModuleNotFoundError: No module named 'django'"

**Solução**: Ativar o ambiente virtual

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Erro: "Can't connect to MySQL server"

**Solução**: Verificar se MySQL está rodando

```bash
# Windows
# Abrir Services (services.msc) e iniciar MySQL

# Linux
sudo service mysql start

# Mac
brew services start mysql
```

### Erro: "No such table: auth_user"

**Solução**: Executar migrações

```bash
python manage.py migrate
```

### Erro: "Database doesn't exist"

**Solução**: Criar banco de dados (ver Passo 4)

---

## 🎨 Customizar o Projeto

### Adicionar Nova Página

1. Criar view em `apps/core/views.py`
2. Criar URL em `apps/core/urls.py`
3. Criar template em `templates/core/`

### Adicionar Novo Campo a Tarefa

1. Editar `apps/tasks/models.py`
2. Executar: `python manage.py makemigrations`
3. Executar: `python manage.py migrate`

---

## 📚 Comandos Django Úteis

```bash
# Criar migrações (após alterar models)
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Acessar shell Python com Django
python manage.py shell

# Rodar testes
python manage.py test

# Coletar arquivos estáticos (para produção)
python manage.py collectstatic

# Limpar cache
python manage.py clear_cache
```

---

## 🚀 Próximos Passos

1. ✅ Rodar o servidor localmente
2. ⏳ Criar usuários de teste (admin, gestor, líder, colaborador)
3. ⏳ Criar tarefas de teste
4. ⏳ Testar fluxo completo
5. ⏳ Fazer commits no GitHub

---

## 📞 Precisa de Ajuda?

1. Verifique o arquivo `README_DJANGO.md`
2. Consulte a documentação do [Django](https://docs.djangoproject.com/)
3. Abra uma issue no GitHub

---

**Pronto! Seu projeto Chaplin está rodando localmente! 🎉**
