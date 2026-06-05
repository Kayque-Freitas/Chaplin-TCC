# Chaplin — Documento Completo de Handoff para IA

> **Objetivo deste arquivo:** Sintetizar TODO o conhecimento do projeto em um único lugar,
> para que outra IA consiga entender, revisar, corrigir e evoluir o sistema sem contexto prévio.

---

## 1. Visão Geral do Projeto

**Chaplin** é uma aplicação web de **gestão de tarefas de manutenção predial** desenvolvida como TCC.

**O que faz:**
- Gestores criam ordens de serviço (tarefas) e atribuem a técnicos.
- Técnicos executam, documentam com fotos (evidências) e marcam como concluídas.
- Comunicação interna por tarefa, notificações em tempo real e RBAC (controle de acesso por cargo).

**Repositório:** `https://github.com/Kayque-Freitas/Chaplin-TCC.git`

---

## 2. Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Backend | Python 3.13, Django 6.0.3 |
| Banco de Dados | SQLite (dev local) / PostgreSQL (Render produção) |
| Frontend | HTML5, Tailwind CSS (CDN), JavaScript Vanilla |
| CEP | API pública ViaCEP |
| Imagens | Pillow |
| Servidor WSGI | Gunicorn |
| Arquivos estáticos | WhiteNoise |
| Formulários | django-crispy-forms + crispy-bootstrap5 |

---

## 3. Estrutura do Projeto

```
Chaplin-TCC/
├── apps/
│   ├── core/               # Home / Landing page
│   ├── tasks/              # Tarefas, notificações, áreas do prédio
│   │   ├── models.py       # Task, Notification, AreaPredio, TaskEvidence, Message, TipoProblem
│   │   ├── views.py        # Lógica de negócio (CRUD, Kanban, Calendário, etc.)
│   │   ├── forms.py        # Formulários Django
│   │   └── urls.py         # Rotas de tarefas
│   └── users/              # Usuários, perfis, autenticação
│       ├── models.py       # UserProfile (role, especialidade, endereço), ActivityLog, Especialidade
│       ├── views.py        # Login, registro, perfil, admin de contas
│       ├── backends.py     # Backend de autenticação (e-mail ou username)
│       └── urls.py         # Rotas de usuários
├── templates/
│   ├── shared/base_dashboard.html   # Layout base (navbar, sidebar, toggle tema)
│   ├── tasks/                       # Templates de tarefas
│   ├── users/                       # Templates de login/admin
│   └── core/                        # Landing page
├── static/
│   ├── css/styles.css
│   ├── js/main.js
│   └── docs/                        # Documentação auxiliar
├── chaplin_project/
│   ├── settings.py                  # Configurações Django
│   └── urls.py                      # URL raiz
├── build.sh                         # Script de deploy (Render)
├── setup_users.py                   # Script para criar usuários de teste
├── manage.py
├── requirements.txt
├── db.sqlite3                       # Banco local (NÃO versionar em prod)
└── .env                             # Variáveis sensíveis (NÃO versionar)
```

---

## 4. Roles / Permissões (RBAC)

| Role | Criar Tarefa | Alocar | Editar | Ver Todas | Admin Contas |
|---|:---:|:---:|:---:|:---:|:---:|
| **admin** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **gestor** | ✅ | ✅ | ✅ | Só as que criou | ❌ |
| **lider** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **colaborador** | ❌ | ❌ | ❌ | Só as atribuídas a ele | ❌ |

**Implementação:** `_is_manager(user)` em `apps/tasks/views.py` verifica se o role é `admin`, `gestor` ou `lider`.

---

## 5. Funcionalidades Implementadas

- Login/Logout com autenticação por **username OU e-mail** (backend customizado).
- **CRUD de Tarefas** com status: `aberta → alocada → concluída → finalizada`; prioridade: `baixa, normal, alta, urgente`.
- **Alocação de responsável** por tarefa (notifica o alocado).
- **Evidências fotográficas** (foto + descrição + tempo gasto + materiais).
- **Mensagens internas** por tarefa.
- **Endereço automático** via ViaCEP (CEP preenche logradouro, bairro, cidade, estado).
- **Gestão de Áreas do Prédio** (CRUD para gestor/admin).
- **Visualizações**: Kanban e Calendário (FullCalendar).
- **Notificações em tempo real** (badge na navbar via AJAX, página central).
- **Tema Claro/Escuro** persistente (Tailwind `darkMode: 'class'`, `localStorage`).
- **Painel Admin** para gerenciar contas (alterar role, editar dados, log de auditoria `ActivityLog`).

---

## 6. Banco de Dados — Tabelas Principais

| Tabela | Descrição |
|---|---|
| `auth_user` | Usuários padrão Django |
| `users_userprofile` | Role, especialidade, endereço pessoal (OneToOne com `auth_user`) |
| `users_activitylog` | Auditoria de mudanças de role |
| `users_especialidade` | Especialidades técnicas |
| `tasks_task` | Tarefas (título, status, prioridade, endereço, área, tipo_problema) |
| `tasks_taskevidence` | Evidências fotográficas |
| `tasks_message` | Mensagens/comentários por tarefa |
| `tasks_notification` | Notificações do sistema |
| `tasks_areapredio` | Áreas físicas do prédio |
| `tasks_tipoproblem` | Tipos de problemas predefinidos |

**Signal importante:** `apps/users/models.py` tem um `post_save` no `User` que cria automaticamente um `UserProfile`. Isso significa que TODO `User` criado (inclusive via `createsuperuser`) ganha um `UserProfile` automaticamente com role `colaborador`.

---

## 7. URLs Principais

| Página | URL |
|---|---|
| Landing Page | `/` |
| Login | `/usuarios/login/` |
| Registro | `/usuarios/register/` |
| Dashboard | `/tasks/dashboard/` |
| Lista de Tarefas | `/tasks/lista/` |
| Criar Tarefa | `/tasks/criar/` |
| Kanban | `/tasks/kanban/` |
| Calendário | `/tasks/calendario/` |
| Notificações | `/tasks/notificacoes/` |
| Configurações | `/tasks/configuracoes/` |
| Áreas do Prédio | `/tasks/areas/` |
| Admin de Contas | `/usuarios/admin-panel/usuarios/` |

---

## 8. Arquivos-Chave do Código

| Arquivo | Responsabilidade |
|---|---|
| `apps/tasks/models.py` | Modelos: Task, TaskEvidence, Message, Notification, AreaPredio, TipoProblem |
| `apps/tasks/views.py` | CRUD de tarefas, dashboard, kanban, calendário, notificações, áreas |
| `apps/users/models.py` | UserProfile (role), ActivityLog, Especialidade, signal `post_save` |
| `apps/users/views.py` | Login, registro, perfil, admin de contas |
| `apps/users/backends.py` | Backend de autenticação (e-mail ou username) |
| `templates/shared/base_dashboard.html` | Layout base: navbar, sidebar, toggle tema |
| `templates/core/` | Landing page |
| `chaplin_project/settings.py` | Configurações Django (DB, apps, middleware, static, CSRF) |
| `build.sh` | Script de build para deploy no Render |
| `setup_users.py` | Cria 4 usuários de teste (admin, gestor, lider, colaborador) |
| `requirements.txt` | Dependências Python |
| `.env` | SECRET_KEY, DEBUG, DATABASE_URL (NÃO versionado) |

---

## 9. Deploy no Render — Instruções Completas

### 9.1 Configuração do Render

1. **Criar Web Service** no Render vinculado ao repositório GitHub.
2. **Environment**: Python 3.
3. **Build Command**: `bash build.sh` (já existe no repositório).
4. **Start Command**: `gunicorn chaplin_project.wsgi:application`.

### 9.2 Variáveis de Ambiente no Render

Adicionar no painel do Render (Settings → Environment):

| Variável | Valor |
|---|---|
| `SECRET_KEY` | Gerar uma chave segura (`python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`) |
| `DEBUG` | `False` |
| `DATABASE_URL` | Copiar da instância PostgreSQL criada no Render |
| `PYTHON_VERSION` | `3.13.0` |

### 9.3 Banco de Dados PostgreSQL

1. Criar um banco **PostgreSQL** no Render (Dashboard → New → PostgreSQL).
2. Copiar a **Internal Database URL** e colar como variável `DATABASE_URL`.
3. O `settings.py` já usa `dj_database_url.parse` para ler `DATABASE_URL` automaticamente.
4. O `build.sh` já roda `python manage.py migrate` no deploy.

### 9.4 Arquivos Estáticos

- WhiteNoise já está configurado no middleware (`settings.py` linha 38).
- `STATIC_ROOT = BASE_DIR / 'staticfiles'`.
- `collectstatic` é executado pelo `build.sh`.

### 9.5 CSRF em Produção

O `settings.py` já contém `CSRF_TRUSTED_ORIGINS`. **Atualizar** com o domínio real do Render:

```python
CSRF_TRUSTED_ORIGINS = [
    'https://SEU-APP.onrender.com',   # ← SUBSTITUIR
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]
```

### 9.6 ALLOWED_HOSTS

Está como `['*']`. Em produção, restringir:

```python
ALLOWED_HOSTS = ['SEU-APP.onrender.com', 'localhost', '127.0.0.1']
```

---

## 10. Conflito de Superuser — Problema e Solução

### O Problema

Quando se usa `python manage.py createsuperuser`, o Django cria o `User` na tabela `auth_user`. O signal `post_save` em `apps/users/models.py` cria automaticamente um `UserProfile` com `role='colaborador'`. Isso significa que o superuser **existe** como admin do Django, mas o sistema Chaplin o trata como **colaborador** (sem permissão para criar tarefas, etc.).

### Solução 1 — Usar o Script `setup_users.py`

```bash
python manage.py shell < setup_users.py
```

Este script cria 4 usuários de teste com roles corretos:
- `admin` / `admin123` → role `admin`, `is_superuser=True`
- `gestor` / `gestor123` → role `gestor`
- `lider` / `lider123` → role `lider`
- `colaborador` / `colaborador123` → role `colaborador`

### Solução 2 — Corrigir Manualmente via Shell

```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
user = User.objects.get(username='SEU_SUPERUSER')
user.profile.role = 'admin'
user.profile.save()
```

### Solução 3 — Melhorar o Signal (RECOMENDADO)

Alterar o signal em `apps/users/models.py` para detectar superusers:

```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        role = 'admin' if instance.is_superuser else 'colaborador'
        UserProfile.objects.create(user=instance, role=role)
```

### Solução 4 — Data Migration para Deploy

Criar uma data migration que garanta a existência de um admin:

```bash
python manage.py makemigrations users --empty --name ensure_admin_exists
```

Preencher com:
```python
from django.db import migrations

def create_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    UserProfile = apps.get_model('users', 'UserProfile')
    if not User.objects.filter(is_superuser=True).exists():
        user = User.objects.create_superuser('admin', 'admin@chaplin.com', 'admin123')
        UserProfile.objects.filter(user=user).update(role='admin')

class Migration(migrations.Migration):
    dependencies = [('users', 'XXXX_previous_migration')]
    operations = [migrations.RunPython(create_admin, migrations.RunPython.noop)]
```

---

## 11. Portabilidade — Como Qualquer Membro do Grupo Roda o Projeto

### 11.1 Passo a Passo (Windows)

```bash
# 1. Clonar o repositório
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC

# 2. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Criar arquivo .env na raiz do projeto
# Conteúdo mínimo:
#   SECRET_KEY=qualquer-chave-aleatoria-aqui
#   DEBUG=True
# NÃO definir DATABASE_URL para usar SQLite local

# 5. Aplicar migrações
python manage.py migrate

# 6. Criar usuários de teste com roles corretos
python manage.py shell < setup_users.py

# 7. Rodar o servidor
python manage.py runserver
```

Acesse: `http://127.0.0.1:8000`

Credenciais de teste:
| Usuário | Senha | Role |
|---|---|---|
| admin | admin123 | admin |
| gestor | gestor123 | gestor |
| lider | lider123 | lider |
| colaborador | colaborador123 | colaborador |

### 11.2 Regras de Portabilidade

1. **NUNCA commitar** `.env` ou `db.sqlite3` no Git (já estão no `.gitignore`).
2. Cada membro cria seu **próprio** `.env` e **próprio** `db.sqlite3` local.
3. Usar `setup_users.py` para popular o banco com dados de teste.
4. Se mudar models, rodar `python manage.py makemigrations` e commitar os arquivos de migration.
5. Ao fazer `git pull`, **sempre** rodar `python manage.py migrate` para aplicar novas migrações.

### 11.3 Workflow Git para o Grupo

```bash
# Antes de começar a trabalhar:
git pull origin main
pip install -r requirements.txt   # caso tenha novas dependências
python manage.py migrate          # caso tenha novas migrações

# Após terminar:
git add .
git commit -m "Descrição clara da mudança"
git push origin main
```

---

## 12. INSTRUÇÕES DE REVISÃO E OTIMIZAÇÃO PARA A IA

> **ATENÇÃO:** Esta seção contém as tarefas que a IA receptora deve executar.

### 12.1 Ajustes de Interface (UI/UX)

#### Navbar — Remover Botões Desnecessários
- **Arquivo:** `templates/shared/base_dashboard.html`
- Remover os links/botões que redirecionam para páginas de "Demonstração" e "Documentação".
- Manter apenas links funcionais: Dashboard, Tarefas, Kanban, Calendário, Notificações, Configurações, Áreas (para gestor/admin).

#### Footer — Remover Completamente
- **Arquivo:** `templates/shared/base_dashboard.html` e qualquer template que contenha `<footer>`.
- Eliminar toda a seção `<footer>` de todas as páginas.

#### Landing Page — Implementar Textos de Marketing
- **Arquivo:** `templates/core/landing.html` (ou equivalente no app `core`).
- Preencher a seção "Sobre Nós" com textos de marketing reais descrevendo o propósito do sistema.
- Garantir que o conteúdo esteja alinhado com a ideia do projeto: **gestão de tarefas de manutenção predial**.

### 12.2 Controle de Fluxo de Acesso

#### Bloquear Acesso via Tela de Cadastro
- **Arquivo:** `apps/users/views.py` → `register_view`
- **Problema atual:** Qualquer pessoa pode se cadastrar e ser logada automaticamente (`login(request, user)` na linha 123), ganhando acesso ao dashboard como `colaborador`.
- **Solução:** Restringir o registro apenas a administradores logados, OU desabilitar o auto-login após registro e exigir aprovação de um admin antes de permitir acesso.
- **Implementação sugerida:**

```python
@login_required  # Só admins podem registrar novos usuários
def register_view(request):
    if not is_admin(request.user) and not _is_manager(request.user):
        django_messages.error(request, 'Sem permissão para criar contas.')
        return redirect('tasks:dashboard')
    # ... resto da lógica
    # REMOVER login(request, user) do final
    # Apenas criar o usuário e redirecionar com mensagem de sucesso
```

- **OU** remover completamente a rota de registro (`/usuarios/register/`) de `apps/users/urls.py` e criar usuários apenas pelo Painel Admin.

### 12.3 Cadastro e Autenticação — Garantir Funcionalidade Completa

- Verificar se `login_view` trata corretamente todos os cenários (credenciais inválidas, sessões expiradas).
- Verificar se o backend `EmailOrUsernameModelBackend` em `apps/users/backends.py` funciona corretamente para login por e-mail E por username.
- Validar que os dados inseridos no cadastro são persistidos corretamente nas tabelas `auth_user` e `users_userprofile`.

### 12.4 Validação de Inputs e Integridade de Dados

- **Aplicar `max_length` em TODOS os campos de formulário** (HTML `maxlength` + validação server-side).
- Limites sugeridos:
  - Username: máx. 30 caracteres
  - Senha: mín. 8 caracteres
  - E-mail: máx. 254 caracteres
  - Título da tarefa: máx. 200 caracteres (já está no model)
  - Descrição: sem limite rígido, mas validar contra conteúdo vazio
  - CEP: exatamente 8 dígitos (formato `XXXXX-XXX` ou `XXXXXXXX`)
  - Telefone: máx. 15 caracteres
- **Remover incoerências**: verificar se há campos duplicados, campos não utilizados, ou validações faltantes.
- **Garantir alinhamento**: cada funcionalidade deve convergir para o objetivo central (gestão de tarefas prediais).

### 12.5 Criação de Tarefas e Dashboard

- Testar o fluxo completo: criar tarefa → alocar responsável → colaborador visualiza → conclui com evidência → gestor finaliza.
- Verificar que o dashboard exibe estatísticas corretas por role.
- Confirmar que o Kanban e o Calendário refletem os dados reais.
- Testar que colaboradores NÃO conseguem acessar tarefas de outros.
- Testar que gestores só veem tarefas que eles criaram.

### 12.6 Testes Automatizados

Rodar/escrever testes para:
- **Autenticação:** login com username, login com e-mail, login com senha errada.
- **Registro:** criação de usuário, bloqueio de username duplicado, persistência do `UserProfile`.
- **CRUD de Tarefas:** criar, editar, alocar, concluir, deletar — verificando permissões por role.
- **Notificações:** geração automática ao criar/alocar/concluir tarefa.
- **Áreas:** CRUD restrito a gestor/admin.
- Comando: `python manage.py test`

### 12.7 Análise de Pontos de Falha

Pontos críticos identificados que a IA deve investigar e corrigir:

1. **`register_view` sem proteção** — permite acesso não autorizado ao sistema (ver seção 12.2).
2. **Signal `create_user_profile`** — superuser criado via `createsuperuser` recebe role `colaborador` (ver seção 10).
3. **`ALLOWED_HOSTS = ['*']`** — inseguro em produção.
4. **`CSRF_TRUSTED_ORIGINS`** — contém URL de outro ambiente (`manus.computer`). Limpar.
5. **Falta de validação nos forms** — `register_view` não valida comprimento de senha, formato de e-mail, nem caracteres especiais.
6. **`setup_users.py` usa senhas fracas** — ok para dev, mas não devem ir para produção.
8. **Falta de `@login_required`** em `register_view` — depende da decisão de quem pode registrar (ver seção 12.2).
9. **`admin_user_edit_view`** — ao promover para admin, define `is_superuser=True` e `is_staff=True`; ao rebaixar, remove `is_superuser` mas NÃO remove `is_staff`. Verificar se isso é intencional.
10. **`complete_task_view`** — não verifica se o usuário é o responsável pela tarefa antes de permitir conclusão. Qualquer usuário logado pode concluir qualquer tarefa acessando a URL diretamente.

### 12.8 Sugestões de Melhorias

1. **Middleware de permissão centralizado** — em vez de verificar `_is_manager()` em cada view, criar um decorator ou middleware.
2. **Django Forms** — usar `ModelForm` para `register_view` (atualmente usa `request.POST.get()` direto, sem validação robusta).
3. **Paginação** — adicionar paginação na lista de tarefas (`tasks_list_view`).
4. **Delete de tarefa** — não existe view de exclusão de tarefa (o CRUD está incompleto).
5. **Finalizar tarefa** — não existe view para mudar status de `concluída` → `finalizada` (o gestor deveria poder fazer isso).
6. **Confirmação de senha** no registro — campo `password_confirm` para evitar erros de digitação.
7. **Recuperação de senha** — implementar via Django `PasswordResetView`.
8. **Logger estruturado** — usar `logging` do Python em vez de depender apenas de `print`.
9. **CI/CD** — configurar GitHub Actions para rodar testes automaticamente em cada push.
10. **Testes E2E** — usar Selenium ou Playwright para testar fluxos completos no navegador.

---

## 13. Setup Rápido (Resumo)

```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Criar .env com SECRET_KEY=qualquer-coisa e DEBUG=True
python manage.py migrate
python manage.py shell < setup_users.py
python manage.py runserver
```

---

*Documento gerado em 20/03/2026. Contém todo o conhecimento acumulado do projeto Chaplin até esta data.*
