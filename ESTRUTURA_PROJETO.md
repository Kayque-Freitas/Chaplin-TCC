# Estrutura do Projeto Chaplin

## 📁 Organização de Pastas

```
Chaplin-TCC/
│
├── 📂 apps/                          # Aplicações Django
│   ├── __init__.py
│   ├── 📂 core/                      # App principal
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── 📂 tasks/                     # App de tarefas
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   └── 📂 users/                     # App de usuários
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       └── views.py
│
├── 📂 chaplin_project/               # Configurações do projeto
│   ├── __init__.py
│   ├── settings.py                  # ⚙️ Configurações principais
│   ├── urls.py                      # 🔗 URLs principais
│   ├── asgi.py
│   └── wsgi.py                      # 🚀 WSGI para produção
│
├── 📂 templates/                     # Templates HTML
│   ├── 📂 shared/                   # Templates compartilhados
│   │   ├── base.html                # Base principal
│   │   └── base_dashboard.html      # Base do dashboard
│   │
│   ├── 📂 core/                     # Templates da app core
│   │   ├── index.html               # Home
│   │   ├── docs.html                # Documentação
│   │   ├── demo.html                # Demonstração
│   │   ├── slides.html              # Apresentação
│   │   ├── resources.html           # Recursos
│   │   └── sitemap.html             # Mapa do site
│   │
│   ├── 📂 tasks/                    # Templates da app tasks
│   │   ├── dashboard.html           # Dashboard de tarefas
│   │   ├── list.html                # Lista de tarefas
│   │   ├── create.html              # Criar tarefa
│   │   ├── detail.html              # Detalhe da tarefa
│   │   └── settings.html            # Configurações
│   │
│   └── 📂 users/                    # Templates da app users
│       ├── login.html               # Login
│       ├── register.html            # Registro
│       └── profile.html             # Perfil
│
├── 📂 static/                        # Arquivos estáticos
│   ├── 📂 css/
│   │   └── styles.css               # Estilos customizados
│   │
│   ├── 📂 js/
│   │   └── main.js                  # JavaScript principal
│   │
│   ├── 📂 images/                   # Imagens do projeto
│   │
│   ├── 📂 docs/                     # Documentação em Markdown
│   │   ├── ARQUITETURA_TECNICA.md
│   │   ├── CHAPLIN_DJANGO_SETUP_COMPLETO.md
│   │   ├── CHAPLIN_PLANO_IMPLEMENTACAO.md
│   │   └── ...
│   │
│   ├── 📂 downloads/                # Arquivos para download
│   │   └── chaplin_static.zip
│   │
│   └── 📂 slides/                   # Slides da apresentação
│       ├── slide_01_capa.html
│       ├── slide_02_indice.html
│       └── ...
│
├── 📄 manage.py                      # Gerenciador Django
├── 📄 requirements.txt               # Dependências Python
├── 📄 db.sqlite3                     # Banco de dados (dev)
├── 📄 .gitignore                     # Arquivos ignorados pelo Git
├── 📄 README.md                      # Documentação principal
└── 📄 ESTRUTURA_PROJETO.md           # Este arquivo
```

## 🎯 Convenções de Nomenclatura

### Templates
- **base.html** - Template base principal
- **base_dashboard.html** - Template base do dashboard
- **index.html** - Página inicial/home
- **login.html** - Página de login
- **list.html** - Listagem de items
- **create.html** - Formulário de criação
- **detail.html** - Detalhe de um item
- **settings.html** - Configurações

### Views
- `index_view()` - Página inicial
- `list_view()` - Listar items
- `create_view()` - Criar item
- `detail_view()` - Detalhe do item
- `update_view()` - Atualizar item
- `delete_view()` - Deletar item
- `settings_view()` - Configurações

### URLs
- `app_name = 'app_name'` - Nome da app
- `path('', views.index_view, name='index')`
- `path('list/', views.list_view, name='list')`
- `path('create/', views.create_view, name='create')`
- `path('<int:id>/', views.detail_view, name='detail')`

## 📋 Apps e Responsabilidades

### Core App
**Responsabilidades:**
- Homepage
- Documentação
- Demonstração
- Apresentação TCC
- Recursos
- Mapa do site

**Models:** Nenhum (apenas views estáticas)

**URLs:**
- `/` - Home
- `/docs/` - Documentação
- `/demo/` - Demonstração
- `/slides/` - Apresentação
- `/resources/` - Recursos
- `/sitemap/` - Mapa

### Tasks App
**Responsabilidades:**
- Gerenciar tarefas
- Dashboard de tarefas
- Criar/editar/deletar tarefas
- Evidências de tarefas
- Mensagens de tarefas

**Models:**
- Task
- TaskEvidence
- Message

**URLs:**
- `/tasks/dashboard/` - Dashboard
- `/tasks/list/` - Lista
- `/tasks/create/` - Criar
- `/tasks/<id>/` - Detalhe
- `/tasks/settings/` - Configurações

### Users App
**Responsabilidades:**
- Autenticação
- Gerenciar usuários
- Perfil de usuário
- Roles e permissões

**Models:**
- User (Django)
- UserProfile

**URLs:**
- `/users/login/` - Login
- `/users/register/` - Registro
- `/users/profile/` - Perfil

## 🔄 Fluxo de Requisição

```
1. Usuário acessa URL
   ↓
2. Django processa em urls.py
   ↓
3. View é chamada
   ↓
4. View processa dados (models, lógica)
   ↓
5. Template é renderizado com contexto
   ↓
6. HTML é retornado ao navegador
```

## 📦 Dependências Principais

```
Django==4.2.0
django-crispy-forms==2.0
crispy-bootstrap5==0.7
python-decouple==3.8
```

## 🚀 Como Adicionar Nova Feature

### 1. Criar Nova App (se necessário)
```bash
python manage.py startapp nova_app
```

### 2. Adicionar Models
Editar `apps/nova_app/models.py`

### 3. Criar Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar Views
Editar `apps/nova_app/views.py`

### 5. Criar Templates
Criar pasta `templates/nova_app/` com templates

### 6. Adicionar URLs
Editar `apps/nova_app/urls.py` e incluir em `chaplin_project/urls.py`

### 7. Registrar no Admin (opcional)
Editar `apps/nova_app/admin.py`

## 🔐 Configurações Importantes

### settings.py
- `DEBUG` - Modo de desenvolvimento
- `ALLOWED_HOSTS` - Hosts permitidos
- `INSTALLED_APPS` - Apps instalados
- `DATABASES` - Configuração do banco
- `STATIC_URL` - URL dos arquivos estáticos
- `CSRF_TRUSTED_ORIGINS` - Origins CSRF confiáveis
- `LOGIN_URL` - URL de login
- `LOGIN_REDIRECT_URL` - Redirecionamento após login

## 📝 Padrões de Código

### Views
```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def list_view(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/list.html', context)
```

### Templates
```html
{% extends "shared/base.html" %}

{% block title %}Tarefas - Chaplin{% endblock %}

{% block content %}
<div class="container">
    <h1>Tarefas</h1>
    <!-- Conteúdo -->
</div>
{% endblock %}
```

### URLs
```python
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('list/', views.list_view, name='list'),
    path('create/', views.create_view, name='create'),
    path('<int:id>/', views.detail_view, name='detail'),
]
```

## 🧪 Testes

Estrutura de testes:
```
apps/
├── tasks/
│   └── tests.py
├── users/
│   └── tests.py
└── core/
    └── tests.py
```

Executar testes:
```bash
python manage.py test
```

## 📊 Banco de Dados

### Diagrama de Relacionamentos
```
User (Django)
├── UserProfile (1:1)
├── Task (1:N) - assigned_to
├── Task (1:N) - created_by
├── TaskEvidence (1:N)
└── Message (1:N)

Task
├── TaskEvidence (1:N)
└── Message (1:N)
```

## 🚀 Deploy

### Preparar para Produção
1. Definir `DEBUG = False`
2. Configurar `ALLOWED_HOSTS`
3. Usar banco de dados PostgreSQL
4. Configurar variáveis de ambiente
5. Coletar arquivos estáticos
6. Configurar HTTPS

```bash
python manage.py collectstatic --noinput
```

---

**Última atualização:** 2026-03-02
**Versão:** 1.0.0
