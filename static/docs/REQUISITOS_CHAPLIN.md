# Requisitos do Sistema - Chaplin

Este documento lista os requisitos que guiaram o desenvolvimento do Chaplin, focando na centralização da gestão de tarefas e na acessibilidade para o setor de manutenção.

## Requisitos Funcionas (RF)

### 1. Autenticação e Perfis
- **RF1.1**: O sistema deve permitir o login de usuários com E-mail ou Nome de Usuário.
- **RF1.2**: O sistema deve suportar quatro níveis de acesso (Roles): Admin, Gestor, Líder e Colaborador.
- **RF1.3**: O sistema deve oferecer a opção de Ativar Autenticação de Dois Fatores (2FA) para maior segurança.
- **RF1.4**: O sistema deve permitir a edição de perfis individuais, incluindo foto e especialidade técnica.

### 2. Gestão de Tarefas (Ordens de Serviço)
- **RF2.1**: O sistema deve permitir que Gestores criem novas tarefas, definindo título, descrição, quarto/local e prioridade.
- **RF2.2**: O sistema deve carregar automaticamente o endereço do prédio via integração com a API ViaCEP ao informar o CEP.
- **RF2.3**: O sistema deve permitir que Líderes atribuam (aloquem) tarefas abertas a Colaboradores específicos.
- **RF2.4**: O sistema deve permitir que Colaboradores registrem a conclusão da tarefa com uma descrição técnica e evidência fotográfica.
- **RF2.5**: O sistema deve permitir que Gestores validem e finalizem permanentemente a tarefa concluída.

### 3. Comunicação e Notificações
- **RF3.1**: O sistema deve possuir um chat interno por tarefa para troca de mensagens entre os envolvidos.
- **RF3.2**: O sistema deve notificar os usuários sobre novas tarefas, atribuições, mensagens e mudanças de status.
- **RF3.3**: O sistema deve exibir um indicador visual de notificações não lidas na barra de navegação.

### 4. Interface e Dashboard
- **RF4.1**: O sistema deve oferecer dashboards personalizados por role, exibindo estatísticas relevantes (tarefas pendentes, concluídas, etc.).
- **RF4.2**: O sistema deve permitir a alternância entre Tema Claro e Tema Escuro (Modo Noturno).
- **RF4.3**: O sistema deve oferecer visualização de tarefas em formato de Lista, Kanban e Calendário.

---

## Requisitos Não-Funcionais (RNF)

- **RNF1 (Segurança)**: Senhas devem ser armazenadas com hash forte padrão do Django (PBKDF2).
- **RNF2 (Acessibilidade)**: A interface deve ser responsiva, funcionando em desktops, tablets e smartphones.
- **RNF3 (Performance)**: As notificações e carregamentos de endereço devem ser realizados de forma assíncrona (AJAX/Fetch) para não interromper a navegação.
- **RNF4 (Facilidade de Uso)**: A linguagem e a interface devem ser simplificadas, visando usuários com pouco domínio tecnológico.
- **RNF5 (Confiabilidade)**: O sistema deve registrar logs de erro e logs de atividade para auditoria de ações críticas.
