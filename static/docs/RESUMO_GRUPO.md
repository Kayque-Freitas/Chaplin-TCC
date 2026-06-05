# Resumo para o Grupo de TCC - Chaplin

Este documento serve como uma referência rápida para que todos os membros do grupo entendam o funcionamento do sistema e possam explicá-lo durante a apresentação.

## O Que é o Chaplin?
O Chaplin é uma plataforma web de **gestão de manutenção predial**. O fluxo básico consiste em:
1. Um **Gestor** abre uma ordem de serviço (tarefa).
2. O sistema notifica o **Líder**, que atribui a tarefa a um **Colaborador**.
3. O **Colaborador** executa o serviço, tira uma foto (evidência) e marca como concluído.
4. O **Gestor** valida o serviço e finaliza a ordem.

## Tipos de Usuário (Roles)
- **Admin**: Gerenciamento de todas as contas e acesso total.
- **Gestor**: Cria tarefas, gerencia as áreas do prédio e valida as conclusões.
- **Líder**: Atribui tarefas aos colaboradores e acompanha o progresso geral.
- **Colaborador**: Visualiza apenas as suas tarefas e registra a execução.

## Principais Funcionalidades Técnicas

### 1. Autenticação
- **Funcionamento**: Login padrão do Django estendido para aceitar E-mail ou CPF/Username.

### 2. Integração ViaCEP
- **Objetivo**: Facilitar o preenchimento do endereço da tarefa.
- **Fluxo**: Ao digitar o CEP, um script JavaScript faz uma requisição para a API do ViaCEP e preenche automaticamente rua, bairro e cidade.

### 3. Sistema de Notificações
- **Gatilhos**: Tarefa criada, alocada, concluída ou nova mensagem no chat.
- **Visualização**: Um sino na barra de navegação mostra as notificações não lidas em tempo real.

### 4. Modo Escuro (Claro/Escuro)
- **Persistência**: A escolha do usuário é salva no navegador (`localStorage`) para que a página não "pisque" ao recarregar.

## Tecnologias Utilizadas
- **Backend**: Python 3.10+, Django 4.2.
- **Frontend**: HTML5, Tailwind CSS (Design), JavaScript (Interações).
- **Banco de Dados**: SQLite (Desenvolvimento) / PostgreSQL (Produção).

## Arquivos Chave do Projeto
- `apps/tasks/models.py`: Define o que é salvo no banco (Tarefa, Evidência, Mensagem).
- `apps/tasks/views.py`: Contém a lógica de negócio (o que acontece em cada ação).
- `templates/shared/base_dashboard.html`: Estrutura principal visual do sistema.
- `settings.py`: Configurações globais do Django.
