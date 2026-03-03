# Chaplin - Plataforma de Gestão de Tarefas e Colaboração

**Chaplin** é uma plataforma web moderna para gestão de tarefas, colaboração em equipe e acompanhamento de projetos. Desenvolvida com Django e Tailwind CSS, oferece uma experiência intuitiva e responsiva para equipes de todos os tamanhos.

## 🎯 Características Principais

- **Gestão de Tarefas** - Criar, atualizar e acompanhar tarefas em tempo real
- **Colaboração em Equipe** - Comunicação integrada entre membros da equipe
- **Múltiplos Roles** - Admin, Gestor, Líder e Colaborador com permissões específicas
- **Dashboard Inteligente** - Visualização de estatísticas e tarefas recentes
- **Evidências de Tarefas** - Anexar arquivos e documentos às tarefas
- **Responsivo** - Funciona perfeitamente em desktop, tablet e mobile
- **Autenticação Segura** - Sistema de login com sessões seguras

## 🏗️ Estrutura do Projeto

```
Chaplin-TCC/
├── apps/                          # Aplicações Django
│   ├── core/                      # App principal (home, docs, demo)
│   ├── tasks/                     # App de tarefas
│   └── users/                     # App de usuários
├── chaplin_project/               # Configurações do projeto
│   ├── settings.py               # Configurações principais
│   ├── urls.py                   # URLs principais
│   └── wsgi.py                   # WSGI para produção
├── templates/                     # Templates HTML
│   ├── shared/                   # Templates compartilhados
│   ├── core/                     # Templates da app core
│   ├── tasks/                    # Templates da app tasks
│   └── users/                    # Templates da app users
├── static/                        # Arquivos estáticos
│   ├── css/
│   ├── js/
│   ├── images/
│   ├── docs/
│   ├── downloads/
│   └── slides/
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## 🚀 Instalação e Setup

### Pré-requisitos

- Python 3.8+
- pip
- Git

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/Chaplin-TCC.git
cd Chaplin-TCC
```

### Passo 2: Criar Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar Migrações

```bash
python manage.py migrate
```

### Passo 5: Criar Usuário Admin

```bash
python manage.py createsuperuser
```

### Passo 6: Executar Servidor

```bash
python manage.py runserver
```

Acesse: http://localhost:8000

## 📋 Credenciais de Teste

| Usuário | Senha | Role |
|---------|-------|------|
| admin | admin123 | Admin |
| gestor | gestor123 | Gestor |
| lider | lider123 | Líder |
| colaborador | colaborador123 | Colaborador |

## 👥 Roles e Permissões

### Admin
- Acesso total ao sistema
- Gerenciar usuários
- Visualizar relatórios
- Configurar sistema

### Gestor
- Criar e gerenciar tarefas
- Atribuir tarefas a líderes
- Visualizar progresso
- Gerar relatórios

### Líder
- Alocar tarefas a colaboradores
- Acompanhar progresso
- Comunicar com equipe
- Visualizar evidências

### Colaborador
- Executar tarefas atribuídas
- Enviar evidências
- Comunicar com líder
- Visualizar tarefas

## 🌐 URLs Principais

### Públicas
- `/` - Home
- `/docs/` - Documentação
- `/demo/` - Demonstração
- `/slides/` - Apresentação TCC
- `/resources/` - Recursos
- `/sitemap/` - Mapa do Site
- `/users/login/` - Login
- `/users/register/` - Registro

### Autenticadas
- `/tasks/dashboard/` - Dashboard
- `/tasks/list/` - Lista de Tarefas
- `/tasks/create/` - Nova Tarefa
- `/tasks/<id>/` - Detalhe da Tarefa
- `/tasks/settings/` - Configurações
- `/admin/` - Painel Administrativo

## 🛠️ Tecnologias Utilizadas

### Backend
- **Django 4.2+** - Framework web
- **Django ORM** - Mapeamento objeto-relacional
- **SQLite** - Banco de dados (desenvolvimento)
- **Python 3.8+** - Linguagem de programação

### Frontend
- **HTML5** - Marcação
- **Tailwind CSS 4** - Estilização
- **JavaScript Vanilla** - Interatividade

## 📊 Modelos de Dados

### User (Django)
- username
- email
- password
- first_name
- last_name

### UserProfile
- user (ForeignKey)
- role (admin, gestor, lider, colaborador)
- phone
- department

### Task
- title
- description
- priority (baixa, média, alta)
- status (aberta, alocada, em_progresso, concluída)
- assigned_to (ForeignKey User)
- created_by (ForeignKey User)
- due_date

### TaskEvidence
- task (ForeignKey Task)
- user (ForeignKey User)
- file
- description

### Message
- sender (ForeignKey User)
- task (ForeignKey Task)
- content

## 🔐 Segurança

- **CSRF Protection** - Proteção contra ataques CSRF
- **SQL Injection Prevention** - Uso de ORM Django
- **XSS Prevention** - Escapamento automático
- **Password Hashing** - Senhas criptografadas
- **Session Security** - Sessões seguras

## 🐛 Troubleshooting

### Erro: "No module named 'apps'"
Certifique-se de que está no diretório raiz e o ambiente virtual está ativado.

### Erro: "Table doesn't exist"
Execute as migrações:
```bash
python manage.py migrate
```

### Erro: "Static files not found"
Colete os arquivos estáticos:
```bash
python manage.py collectstatic --noinput
```

## 📚 Documentação Adicional

- [Arquitetura Técnica](static/docs/ARQUITETURA_TECNICA.md)
- [Guia de Setup Completo](static/docs/CHAPLIN_DJANGO_SETUP_COMPLETO.md)
- [Plano de Implementação](static/docs/CHAPLIN_PLANO_IMPLEMENTACAO.md)

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto é licenciado sob a Licença MIT.

---

**Desenvolvido com ❤️ para melhorar a colaboração em equipe**
