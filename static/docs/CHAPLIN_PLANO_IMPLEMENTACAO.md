# Plano de Implementação - Projeto Chaplin Django

## 📋 Visão Geral

Este documento descreve o plano para implementar o Chaplin como uma aplicação Django funcional, simples e pronta para apresentação de TCC.

**Objetivo**: Criar uma aplicação web que seja:
- ✅ Funcional (CRUD completo de tarefas)
- ✅ Simples (sem complexidades desnecessárias)
- ✅ Apresentável (design profissional)
- ✅ Documentada (para apresentação em TCC)
- ✅ Testável (pronta para demonstração)

---

## 🏗️ Estrutura do Projeto

```
chaplin-django/
├── manage.py
├── requirements.txt
├── chaplin_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── profile.html
│   ├── tasks/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── templates/
│   │       ├── dashboard.html
│   │       ├── tarefas.html
│   │       ├── nova_tarefa.html
│   │       └── detalhe_tarefa.html
│   └── core/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           ├── base.html
│           ├── index.html
│           └── 404.html
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
└── templates/
    └── base.html
```

---

## 🗄️ Banco de Dados

### Modelos Principais

#### 1. **User** (Usuário)
```
- id (PK)
- username (unique)
- email (unique)
- password (hashed)
- first_name
- last_name
- role (choices: admin, gestor, lider, colaborador)
- company (FK para Company)
- created_at
- updated_at
```

#### 2. **Company** (Empresa)
```
- id (PK)
- name
- logo
- primary_color
- secondary_color
- created_at
- updated_at
```

#### 3. **Task** (Tarefa)
```
- id (PK)
- title
- description
- priority (choices: baixa, normal, alta, urgente)
- status (choices: aberta, alocada, concluida, finalizada)
- created_by (FK para User)
- assigned_to (FK para User)
- company (FK para Company)
- due_date
- created_at
- updated_at
```

#### 4. **TaskEvidence** (Evidência de Tarefa)
```
- id (PK)
- task (FK para Task)
- photo (ImageField)
- description
- created_at
```

#### 5. **Message** (Mensagem)
```
- id (PK)
- task (FK para Task)
- sender (FK para User)
- content
- created_at
```

---

## 🎨 Design e Cores

Usar as cores do projeto estático:
- **Primária**: #f97316 (Orange)
- **Secundária**: #2962FF (Blue)
- **Escura**: #000000 (Black)
- **Fundo**: #FFFFFF (White)

Manter a mesma estrutura de layout:
- Header com logo e navegação
- Sidebar colapsável em mobile
- Cards para tarefas
- Formulários simples e intuitivos

---

## 📱 Funcionalidades Principais (MVP)

### Fase 1: Autenticação (Semana 1)
- [x] Login com username/password
- [x] Registro de novo usuário
- [x] Logout
- [x] Proteção de rotas (login_required)
- [x] Perfil de usuário

### Fase 2: Dashboard (Semana 2)
- [x] Dashboard com estatísticas básicas
- [x] Listagem de tarefas por role
- [x] Filtros simples (status, prioridade)
- [x] Contadores (aberta, alocada, concluída)

### Fase 3: CRUD de Tarefas (Semana 3-4)
- [x] Criar tarefa (Gestor)
- [x] Listar tarefas (todos)
- [x] Editar tarefa (Gestor/Líder)
- [x] Deletar tarefa (Admin)
- [x] Visualizar detalhe da tarefa

### Fase 4: Atribuição e Conclusão (Semana 5)
- [x] Atribuir tarefa a colaborador (Líder)
- [x] Marcar como concluída (Colaborador)
- [x] Upload de foto de evidência
- [x] Adicionar descrição de conclusão

### Fase 5: Comunicação (Semana 6)
- [x] Chat simples por tarefa
- [x] Histórico de mensagens
- [x] Notificações básicas

---

## 🔐 Permissões por Role

### Admin
- Gerenciar usuários
- Visualizar todas as tarefas
- Acessar relatórios

### Gestor (Cliente)
- Criar tarefas
- Visualizar tarefas criadas
- Validar conclusão

### Líder (Team Leader)
- Visualizar tarefas recebidas
- Atribuir a colaboradores
- Acompanhar progresso

### Colaborador (Technician)
- Visualizar tarefas atribuídas
- Marcar como concluída
- Upload de evidências

---

## 🛠️ Stack Tecnológico

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| Framework | Django | 4.2+ |
| Database | MySQL | 8.0+ |
| Frontend | HTML/CSS/JS | - |
| CSS Framework | Tailwind CSS | 4.0+ |
| Auth | Django Sessions | Built-in |
| Forms | Django Forms | Built-in |

---

## 📦 Dependências Principais

```
Django==4.2.0
mysqlclient==2.2.0
python-decouple==3.8
Pillow==10.0.0
```

---

## 🚀 Cronograma de Implementação

| Semana | Tarefa | Status |
|--------|--------|--------|
| 1 | Setup Django + Modelos + Auth | ⏳ |
| 2 | Dashboard + Listagem | ⏳ |
| 3-4 | CRUD de Tarefas | ⏳ |
| 5 | Atribuição + Evidências | ⏳ |
| 6 | Chat + Testes | ⏳ |
| 7 | Documentação + Slides | ⏳ |

---

## 📚 Documentação a Ser Criada

1. **Guia de Banco de Dados**
   - Diagrama ER
   - Descrição de cada tabela
   - Relacionamentos

2. **Guia de Apresentação**
   - O que é o Chaplin
   - Como funciona (fluxo)
   - Tecnologias usadas
   - Como executar localmente

3. **FAQ para Banca**
   - Perguntas técnicas comuns
   - Respostas simples e claras
   - Exemplos práticos

4. **Guia de Execução Local**
   - Instalação de dependências
   - Setup do banco de dados
   - Como rodar o servidor
   - Dados de teste

---

## ✅ Checklist Final

Antes de apresentar:

- [ ] Projeto roda localmente sem erros
- [ ] Todas as funcionalidades do MVP funcionam
- [ ] Design segue o projeto estático
- [ ] Banco de dados está documentado
- [ ] Documentação de apresentação está pronta
- [ ] FAQ foi revisado
- [ ] Dados de teste foram criados
- [ ] Apresentação foi ensaiada

---

## 🎯 Próximos Passos

1. Confirmar este plano com o grupo
2. Começar Setup Django (Fase 1)
3. Implementar Modelos e Autenticação
4. Criar Templates com design estático
5. Implementar CRUD
6. Testar e documentar

**Vamos começar?** 🚀
