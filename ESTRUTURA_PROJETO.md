# Estrutura do Projeto Chaplin

O sistema Chaplin é uma aplicação web construída com o framework **Django 4.2**. O projeto foi organizado para ser modular e fácil de manter, separando as responsabilidades em diferentes aplicações internas.

## Organização de Diretórios

Abaixo está uma visão geral da estrutura de pastas e arquivos principais:

```
Chaplin-TCC/
├── apps/                 # Aplicações Django locais
│   ├── core/             # Páginas estáticas (Home, Landing Page)
│   ├── tasks/            # Gestão de Tarefas, Notificações e Áreas
│   └── users/            # Gestão de Perfis, 2FA e Autenticação
├── chaplin_project/      # Configurações do projeto Django
│   ├── settings.py       # Configurações de Banco, Apps e Segurança
│   └── urls.py           # Roteamento global das URLs
├── templates/            # Arquivos HTML (utilizando Django Templates)
│   ├── shared/           # Layouts base e componentes compartilhados
│   ├── core/             # Templates da app core
│   ├── tasks/            # Templates da app tasks
│   └── users/            # Templates da app users
├── static/               # Arquivos Estáticos (CSS, JS, Imagens, Documentos)
│   ├── css/              # Estilos (via Tailwind CSS)
│   ├── js/               # Lógica JavaScript (ViaCEP, Relógio, Notificações)
│   └── docs/             # Documentação em Markdown
├── media/                # Arquivos de mídia (evidências, fotos de perfil)
├── manage.py             # Script de comando para gerenciar o Django
├── requirements.txt      # Dependências do Python
└── .env                  # Variáveis de ambiente (Chaves secretas, Debug)
```

## Descrição das Aplicações

### 1. **Core App (`apps/core/`)**
A aplicação responsável pela parte institucional.
- **Views**: Gerencia a renderização da Home e das páginas de apoio.
- **Templates**: `index.html`, `contato.html`.

### 2. **Tasks App (`apps/tasks/`)**
A aplicação central do sistema, onde reside toda a lógica de negócio das tarefas.
- **Modelos Principais**: `Task`, `Notification`, `AreaPredio`, `TaskEvidence`, `Message`.
- **Funcionalidades**: CRUD de tarefas, comentários, registro de fotos, notificações automáticas.
- **URLs Relevantes**: `/tasks/dashboard/`, `/tasks/kanban/`, `/tasks/lista/`.

### 3. **Users App (`apps/users/`)**
Responsável por toda a camada de segurança e perfis.
- **Modelos Principais**: `UserProfile` (extensão do `User` padrão do Django).
- **Backend de Autenticação**: Permite login tanto por e-mail quanto por nome de usuário.
- **Funcionalidades**: Registro, Login/Logout, Painel Admin de usuários e Configuração de 2FA.

## Convenções de Código

- **Estilização**: O projeto utiliza **Tailwind CSS** (via CDN no momento) para o design responsivo.
- **Banco de Dados**: Em desenvolvimento é utilizado o **SQLite** (`db.sqlite3`). Para produção, o código está preparado para **PostgreSQL**.
- **Internacionalização**: O sistema está configurado para o fuso horário de São Paulo e idioma `pt-br`.

## Contribuição e Alterações
Ao adicionar novas funcionalidades, siga o fluxo:
1. Defina o modelo em `models.py`.
2. Rode as migrações (`makemigrations` e `migrate`).
3. Crie a lógica na `views.py`.
4. Mapeie a rota em `urls.py`.
5. Desenvolva o template correspondente.
