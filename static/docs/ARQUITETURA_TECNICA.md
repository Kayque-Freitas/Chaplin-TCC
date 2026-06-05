# Arquitetura Técnica - Chaplin

O sistema Chaplin foi desenvolvido utilizando o framework **Django**, seguindo o padrão de projeto MTV (Model-Template-View). Esta escolha garante segurança, escalabilidade e rapidez no desenvolvimento de aplicações robustas.

## Stack Tecnológico

### Backend
- **Framework**: Django 4.2 (Python 3.10+)
- **Autenticação**: Django Contrib Auth (Sessões)
- **Segurança**: CSRF Protection, Password Hashing (PBKDF2), RBAC (Role-Based Access Control)

### Frontend
- **Interface**: Django Templates + HTML5
- **Estilização**: Tailwind CSS
- **Interatividade**: JavaScript Vanilla (AJAX para notificações e integração ViaCEP)

### Banco de Dados
- **Desenvolvimento**: SQLite (Arquivo local `db.sqlite3`)
- **Produção**: PostgreSQL (Configurado via variável de ambiente `DATABASE_URL`)

---

## Estrutura de Modelagem (Banco de Dados)

O sistema centraliza as informações em quatro módulos principais:

1. **Usuários e Perfis (`UserProfile`)**: Estende o usuário padrão do Django para incluir o `role` (Admin, Gestor, Líder, Colaborador) e configurações de segurança como as informações de endereço.
2. **Tarefas (`Task`)**: Registra título, descrição, status (`ABERTA`, `ALOCADA`, `CONCLUIDA`, `FINALIZADA`), prioridade e localização da ordem de serviço.
3. **Evidências (`TaskEvidence`)**: Armazena as fotos e descrições enviadas pelos colaboradores ao finalizarem um serviço.
4. **Comunicação (`Message`)**: Histórico de mensagens trocadas dentro de cada tarefa específica.
5. **Notificações (`Notification`)**: Sistema de alertas internos para mudanças de status e novas mensagens.

---

## Fluxo de Dados

1. **Requisição Web**: O usuário acessa uma URL que é roteada pelo arquivo `urls.py`.
2. **Lógica de Negócio**: A `views.py` processa a requisição, valida as permissões do usuário e interage com os `models.py`.
3. **Persistência**: O Django ORM traduz as operações para SQL e as executa no banco de dados.
4. **Renderização**: O Template Engine do Django mescla os dados com os arquivos HTML e retorna a página final ao navegador.

---

## Segurança e Performance

- **Proteção CSRF**: Obrigatória em todos os formulários POST para evitar ataques de falsificação de solicitação.
- **Middleware WhiteNoise**: Utilizado para servir arquivos estáticos (CSS/JS) de forma eficiente, mesmo em ambientes de produção simples.
- **Ambiente Isolado**: Configurações sensíveis (chaves, senhas) são geridas via arquivo `.env`, fora do controle de versão.
