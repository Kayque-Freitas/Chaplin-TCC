# Chaplin — Gestão de Tarefas Predial

O Chaplin é um sistema web desenvolvido como Trabalho de Conclusão de Curso (TCC) para gerenciar a manutenção preventiva e corretiva em edifícios e propriedades. Ele centraliza a comunicação entre gestores, líderes de equipe e colaboradores, garantindo que as ordens de serviço sejam acompanhadas desde a abertura até a conclusão com evidências fotográficas.

## Funcionalidades Principais

- **Gestão de Usuários**: Sistema de permissões baseado em funções (Admin, Gestor, Líder e Colaborador).
- **Controle de Tarefas**: Acompanhamento completo do status da manutenção (Aberta, Alocada, Concluída e Finalizada).
- **Evidências Fotográficas**: Upload de fotos e descrições técnicas para comprovação do serviço.
- **Comunicação Integrada**: Chat interno em cada tarefa para troca de informações entre os envolvidos.
- **Visualização Flexível**: Acompanhamento por lista, Kanban ou Calendário.
- **Segurança**: Autenticação robusta estendida com suporte completo no Django.

---

## Estrutura do Projeto

O projeto é organizado em aplicações Django modulares:

- **`apps/core/`**: Página inicial e componentes estáticos.
- **`apps/tasks/`**: Lógica de tarefas, notificações, áreas do prédio e evidências.
- **`apps/users/`**: Gestão de perfis, autenticação e controle de acesso.

Para uma visão detalhada da arquitetura, consulte [ESTRUTURA_PROJETO.md](ESTRUTURA_PROJETO.md).

---

## Como Começar

Para rodar o projeto localmente pela primeira vez, siga estes passos simplificados:

1. **Clone o repositório e entre na pasta:**
```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
venv\Scripts\activate  # No Windows
```

3. **Instale as dependências e prepare o banco (SQLite):**
```bash
pip install -r requirements.txt
python manage.py migrate
```

4. **Inicie o servidor:**
```bash
python manage.py runserver
```

Para instruções mais detalhadas sobre configuração de banco de dados (PostgreSQL), solução de problemas ou deploy, consulte o [Guia de Configuração](static/docs/GUIA_SETUP.md).

---

## Equipe e Desenvolvimento

Este projeto foi desenvolvido como parte do TCC da ETEC. O objetivo é oferecer uma ferramenta prática e profissional para o mercado de manutenção predial.

- **Desenvolvido por**: [Kayque Freitas](https://github.com/Kayque-Freitas) e equipe.
- **Tecnologias**: Python, Django, Tailwind CSS, SQLite/PostgreSQL.
