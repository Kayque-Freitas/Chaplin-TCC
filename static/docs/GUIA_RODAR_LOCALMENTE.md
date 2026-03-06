# 🚀 Guia: Como Rodar o Chaplin em Outro Computador

> Siga cada passo na ordem. Se aparecer algum erro, veja a seção **Troubleshooting** no final.

---

## 📋 Pré-requisitos

Instale antes de começar:

| Software | Versão mínima | Link |
|---|---|---|
| **Python** | 3.10+ | [python.org/downloads](https://www.python.org/downloads/) |
| **Git** | qualquer | [git-scm.com](https://git-scm.com/downloads) |
| **VS Code** (opcional) | qualquer | [code.visualstudio.com](https://code.visualstudio.com/) |

> ⚠️ **Não precisa de MySQL.** O projeto usa **SQLite** — o banco de dados fica num arquivo local (`db.sqlite3`) criado automaticamente.

### Verificar instalação

```bash
python --version   # deve mostrar 3.10 ou superior
git --version
```

---

## 🔧 Passo 1 — Clonar o repositório

```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
```

> Se já tiver a pasta clonada, só atualize:
> ```bash
> git pull origin main
> ```

---

## 🐍 Passo 2 — Criar o Ambiente Virtual

O ambiente virtual isola as bibliotecas do projeto para não misturar com outros projetos Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

✅ Você saberá que está ativo quando aparecer `(venv)` no início do terminal.

---

## 📦 Passo 3 — Instalar as Dependências

```bash
pip install -r requirements.txt
```

Isso instala automaticamente:
- `Django` — framework principal
- `Pillow` — upload de imagens (evidências, avatares)
- `pyotp` — autenticação em dois fatores (2FA)
- `qrcode` — geração do QR Code do 2FA
- `python-decouple` — leitura do arquivo `.env`
- e todas as demais no `requirements.txt`

---

## ⚙️ Passo 4 — Criar o arquivo `.env`

O arquivo `.env` guarda as configurações sensíveis (ex: chave secreta do Django). Ele **não está no repositório** por segurança.

Crie um arquivo chamado `.env` na raiz do projeto:

```
SECRET_KEY=django-insecure-chaplin-dev-key-qualquer-coisa-aqui-123
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

> **Windows:** No explorador de arquivos, crie um arquivo `.env` (com o ponto na frente). Se tiver dificuldade, pelo terminal:
> ```bash
> echo SECRET_KEY=django-insecure-chaplin-dev-key-local > .env
> echo DEBUG=True >> .env
> ```

---

## 🗄️ Passo 5 — Criar o Banco de Dados

```bash
python manage.py migrate
```

Isso cria o arquivo `db.sqlite3` com todas as tabelas do projeto:
- `auth_user` — usuários Django
- `tasks_task` — tarefas
- `tasks_notification` — notificações
- `tasks_areapredio` — áreas do prédio
- `users_userprofile` — perfis com role e 2FA
- e todas as demais

> ✅ Deve aparecer vários `Applying ... OK` sem erros.

---

## 👤 Passo 6 — Criar o Primeiro Usuário (Admin)

```bash
python manage.py createsuperuser
```

Preencha quando pedido:
```
Username: admin
Email: admin@chaplin.com
Password: (escolha uma senha)
```

> Após criar o superusuário, acesse `/usuarios/admin-panel/usuarios/` e configure o **role** dele para `admin` pelo painel do Django Admin em `/admin/`.
>
> Alternativamente, use o shell Django para definir o role diretamente:
> ```bash
> python manage.py shell
> ```
> ```python
> from django.contrib.auth.models import User
> from apps.users.models import UserProfile
> u = User.objects.get(username='admin')
> u.profile.role = 'admin'
> u.profile.save()
> exit()
> ```

---

## ▶️ Passo 7 — Rodar o Servidor

```bash
python manage.py runserver
```

Abra no navegador: **http://127.0.0.1:8000**

---

## 🌐 Páginas Importantes

| Página | URL |
|---|---|
| Home (pública) | http://127.0.0.1:8000/ |
| Login | http://127.0.0.1:8000/usuarios/login/ |
| Dashboard | http://127.0.0.1:8000/tasks/dashboard/ |
| Lista de Tarefas | http://127.0.0.1:8000/tasks/lista/ |
| Kanban | http://127.0.0.1:8000/tasks/kanban/ |
| Calendário | http://127.0.0.1:8000/tasks/calendario/ |
| Notificações | http://127.0.0.1:8000/tasks/notificacoes/ |
| Configurações / 2FA | http://127.0.0.1:8000/tasks/configuracoes/ |
| Áreas do Prédio | http://127.0.0.1:8000/tasks/areas/ |
| Admin Django | http://127.0.0.1:8000/admin/ |

---

## 📁 Arquivos que NÃO estão no repositório (criar manualmente)

| Arquivo | Por quê não está no repo | O que fazer |
|---|---|---|
| `.env` | Segurança (chave secreta) | Criar conforme Passo 4 |
| `db.sqlite3` | Banco de dados local | Criado automaticamente no `migrate` |
| `media/` | Uploads dos usuários | Criado automaticamente ao subir a 1ª foto |
| `venv/` | Ambiente virtual | Criado no Passo 2 |

---

## 🐛 Troubleshooting

### `No module named 'django'`
O ambiente virtual não está ativo. Execute:
```bash
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac
```

### `No module named 'decouple'` ou outro módulo
Instalação incompleta. Execute:
```bash
pip install -r requirements.txt
```

### `django.core.exceptions.ImproperlyConfigured` / SECRET_KEY
O arquivo `.env` não existe ou está errado. Reveja o Passo 4.

### `Table 'xxx' doesn't exist`
As migrações não foram rodadas. Execute:
```bash
python manage.py migrate
```

### `OperationalError: no such table`
Mesmo caso acima. Se persistir:
```bash
python manage.py migrate --run-syncdb
```

### Foto de perfil/evidência não aparece
A pasta `media/` não existe. Crie na raiz do projeto:
```bash
mkdir media
```
E verifique se `MEDIA_ROOT` e `MEDIA_URL` estão em `settings.py`.

### Porta 8000 ocupada
```bash
python manage.py runserver 8080
```

---

## 📚 Comandos Django — Referência Rápida

```bash
# Ativar ambiente virtual
venv\Scripts\activate

# Rodar servidor
python manage.py runserver

# Criar migrações (após alterar models.py)
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Acessar shell Python com Django carregado
python manage.py shell

# Ver todas as rotas do projeto
python manage.py show_urls   # requer django-extensions

# Verificar se há erros no projeto
python manage.py check
```

---

## 🔄 Workflow do Git para o Grupo

```bash
# Antes de trabalhar: pegar as últimas atualizações
git pull origin main

# Trabalhar normalmente...

# Ao terminar: commitar e enviar
git add -A
git commit -m "feat: descrição do que foi feito"
git push origin main
```

> **Boa prática:** sempre dê `git pull` antes de começar a trabalhar para evitar conflitos.

---

**✅ Pronto! O Chaplin está rodando na sua máquina.**
