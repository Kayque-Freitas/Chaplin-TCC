# Chaplin: Plataforma de Gestão de Tarefas para Empresas Terceirizadas

**Documento Oficial do Projeto de TCC - ETEC**

---

## 1. Introdução

A Chaplin é uma plataforma web de gestão de tarefas desenvolvida para empresas terceirizadas que prestam serviços de manutenção em hotéis e propriedades de aluguel de curta duração (Airbnb). A aplicação centraliza a comunicação entre gestores de prédios (clientes) e equipes de manutenção (prestadores de serviço), permitindo que cada empresa terceirizada customize a plataforma conforme suas necessidades operacionais.

---

## 2. Origem da Ideia

### 2.1 A Empresa Charlie

A ideia do projeto Chaplin originou-se de uma conversa com o pai de um dos integrantes do grupo, que trabalha na empresa **Charlie**, uma empresa especializada em prestação de serviços de manutenção para hotéis e propriedades de aluguel de curta duração.

### 2.2 O Problema Identificado

Durante o acompanhamento das operações da Charlie, foram identificados diversos desafios no fluxo de trabalho:

**Problemas com o Sistema Atual:**

1. **Formulário Desorganizado e Pouco Intuitivo**: A empresa utilizava um formulário básico, sem estilização adequada e de difícil compreensão, especialmente para colaboradores com pouca familiaridade com tecnologia.

2. **Comunicação Fragmentada**: As demandas de manutenção eram comunicadas através de múltiplos canais, principalmente WhatsApp, causando dispersão de informações e dificuldade em rastrear o histórico de cada tarefa.

3. **Falta de Centralização**: Não havia um local único onde todas as demandas pudessem ser visualizadas e acompanhadas. Informações importantes ficavam espalhadas em conversas de WhatsApp, emails e anotações em papel.

4. **Desafios com Usuários Não-Tech**: Muitos dos colaboradores da empresa possuem pouca ou nenhuma experiência com tecnologia, tornando sistemas complexos inacessíveis e gerando resistência ao uso.

5. **Ausência de Rastreabilidade**: Não havia registro estruturado do histórico completo de uma demanda, desde sua identificação até a conclusão, dificultando auditorias e análise de padrões.

6. **Retrabalho e Falhas**: A comunicação inadequada resultava em tarefas incompletas, duplicadas ou realizadas incorretamente.

### 2.3 A Solução Proposta

A partir desses desafios, surgiu a ideia de desenvolver a **Chaplin**: uma plataforma simples, intuitiva e centralizada que permitisse:

- Registrar demandas de forma clara e organizada
- Centralizar toda a comunicação em um único lugar
- Ser acessível para usuários com pouca experiência tecnológica
- Rastrear o histórico completo de cada tarefa
- Reduzir o uso de WhatsApp para comunicações de trabalho
- Ser customizável para diferentes empresas terceirizadas

---

## 3. Contexto e Problemática

### 3.1 Cenário Atual

O setor de hospedagem no Brasil é significativo economicamente. Hotéis, resorts e anfitriões de Airbnb dependem de empresas terceirizadas para manutenção preventiva e corretiva de suas propriedades. Esse modelo operacional, apesar de amplamente utilizado, enfrenta desafios importantes:

**Problemas Identificados:**

1. **Fragmentação de Comunicação**: As demandas são frequentemente comunicadas através de múltiplos canais (WhatsApp, email, ligações), resultando em perda de informações e falta de rastreabilidade.

2. **Ineficiência Operacional**: Sem um sistema centralizado, gestores enfrentam dificuldades em coordenar tarefas, acompanhar progresso e garantir conclusão dentro de prazos.

3. **Falta de Documentação**: Não existe registro estruturado de problemas identificados, ações tomadas e evidências de conclusão.

4. **Retrabalho e Falhas**: A comunicação inadequada resulta em tarefas incompletas, duplicadas ou realizadas incorretamente.

5. **Ausência de Rastreabilidade**: Impossibilidade de rastrear o histórico completo de uma demanda desde sua identificação até a conclusão.

### 3.2 Impacto Operacional

Esses problemas resultam em:
- Redução da satisfação de hóspedes
- Aumento de custos operacionais
- Comprometimento da reputação do estabelecimento
- Perda de produtividade dos colaboradores
- Dificuldade em cumprir padrões de qualidade

---

## 4. Posicionamento e Objetivos

### 4.1 Missão da Chaplin

A Chaplin é uma plataforma web de gestão de tarefas que centraliza, organiza e simplifica o fluxo de comunicação entre gestores de prédios e empresas terceirizadas de manutenção, permitindo que cada empresa customize a plataforma conforme suas necessidades, com foco em simplicidade e acessibilidade para usuários com pouca experiência tecnológica.

### 4.2 Modelo de Negócio

A Chaplin é uma **aplicação SaaS (Software as a Service)** que pode ser oferecida por empresas terceirizadas aos seus clientes (gestores de prédios) como forma de comunicação e gestão de demandas. Cada empresa terceirizada pode:

- Customizar a plataforma com sua marca
- Gerenciar seus próprios usuários (líderes e colaboradores)
- Receber demandas de seus clientes (gestores de prédios)
- Organizar e atribuir tarefas internamente

### 4.3 Segmento de Mercado Alvo

| Aspecto | Descrição |
|--------|-----------|
| **Clientes Primários** | Empresas terceirizadas de manutenção |
| **Usuários Finais** | Gestores de prédios, líderes de equipe, colaboradores técnicos |
| **Escala** | Pequenas a médias empresas (5-50 colaboradores) |
| **Setor** | Hospedagem (hotéis, resorts, Airbnb) |

### 4.4 Objetivos do Projeto

**Objetivo Geral:**
Desenvolver uma plataforma web que centralize o fluxo de gestão de tarefas de manutenção entre gestores de prédios e empresas terceirizadas, tornando-o mais organizado, eficiente e acessível para usuários com diferentes níveis de experiência tecnológica.

**Objetivos Específicos:**
1. Criar uma interface intuitiva e simples, acessível para usuários não-tech
2. Centralizar todas as demandas de manutenção em um único lugar
3. Implementar rastreabilidade completa de cada tarefa
4. Permitir comunicação integrada entre gestores e equipes
5. Documentar evidências (fotos e descrições) de conclusão de tarefas
6. Reduzir o tempo de coordenação e comunicação informal
7. Permitir customização por empresa terceirizada

---

## 5. Estrutura de Roles (Papéis de Usuário)

A Chaplin possui 4 roles principais, cada um com permissões e responsabilidades específicas:

### 5.1 Role 1: Administrador da Empresa

**Quem é:** Proprietário ou gerente geral da empresa terceirizada

**Permissões:**
- Gerenciar usuários (criar, editar, deletar)
- Atribuir roles aos usuários
- Visualizar todas as tarefas
- Visualizar relatórios e estatísticas
- Customizar configurações da empresa
- Visualizar desempenho de líderes e colaboradores

**Responsabilidades:**
- Criar contas para líderes e colaboradores
- Definir permissões de acesso
- Acompanhar desempenho geral

### 5.2 Role 2: Gestor do Prédio (Cliente)

**Quem é:** Gerente de operações, síndico ou responsável pelo prédio/hotel

**Permissões:**
- Criar novas tarefas/demandas
- Visualizar status de tarefas criadas por ele
- Enviar mensagens para a empresa
- Visualizar histórico de tarefas concluídas
- Fazer upload de fotos do problema

**Responsabilidades:**
- Registrar demandas de manutenção
- Fornecer informações detalhadas do problema
- Validar conclusão das tarefas
- Comunicar-se com a empresa através da plataforma

### 5.3 Role 3: Líder de Equipe

**Quem é:** Supervisor ou coordenador de equipe dentro da empresa terceirizada

**Permissões:**
- Visualizar todas as tarefas recebidas
- Atribuir tarefas a colaboradores
- Visualizar desempenho dos colaboradores
- Comunicar-se com gestores de prédios
- Visualizar relatórios de tarefas por colaborador
- Marcar tarefas como concluídas (após validação)

**Responsabilidades:**
- Receber demandas dos gestores de prédios
- Avaliar complexidade das tarefas
- Atribuir tarefas aos colaboradores mais adequados
- Acompanhar progresso das tarefas
- Validar qualidade do trabalho realizado

### 5.4 Role 4: Colaborador Técnico

**Quem é:** Eletricista, encanador, pintor, camareiro ou outro profissional técnico

**Permissões:**
- Visualizar tarefas atribuídas a ele
- Atualizar status da tarefa
- Fazer upload de fotos de evidência
- Adicionar descrição de conclusão
- Visualizar histórico de suas tarefas
- Enviar mensagens relacionadas à tarefa

**Responsabilidades:**
- Executar tarefas conforme especificado
- Registrar conclusão com evidências
- Comunicar-se com o líder sobre dúvidas
- Manter qualidade do trabalho

---

## 6. Fluxo Operacional

### 6.1 Descrição Detalhada do Processo

O fluxo operacional da Chaplin segue sete etapas principais:

#### **Etapa 1: Identificação de Problemas**
- **Responsável**: Camareiras ou profissionais de limpeza do hotel
- **Ação**: Após checkout do hóspede, o profissional realiza inspeção do quarto e identifica problemas (vazamentos, lâmpadas queimadas, móveis danificados) ou necessidades de reposição
- **Saída**: Lista de problemas identificados

#### **Etapa 2: Reporte ao Gestor**
- **Responsável**: Camareiras ou profissionais de limpeza
- **Ação**: O profissional comunica os problemas ao gestor do prédio
- **Saída**: Informação chega ao gestor

#### **Etapa 3: Registro na Plataforma (O "Tobogã")**
- **Responsável**: Gestor do prédio
- **Ação**: O gestor acessa a Chaplin e registra a ocorrência, incluindo:
  - Número do quarto
  - Categoria do problema (elétrico, hidráulico, estrutural, limpeza, etc.)
  - Descrição detalhada
  - Fotos do problema
  - Prioridade (urgente, alta, normal, baixa)
  - Prazo desejado de conclusão
- **Saída**: Tarefa criada no sistema com status "ABERTA"
- **Nota**: A tarefa é automaticamente enviada para o líder da empresa (como se caísse num tobogã)

#### **Etapa 4: Recebimento pela Empresa**
- **Responsável**: Líder de equipe da empresa terceirizada
- **Ação**: O líder recebe notificação de nova tarefa e visualiza os detalhes
- **Saída**: Tarefa visível no dashboard do líder com status "RECEBIDA"

#### **Etapa 5: Alocação ao Colaborador**
- **Responsável**: Líder da equipe
- **Ação**: O líder analisa a complexidade e aloca ao colaborador mais adequado (considerando especialidade e disponibilidade)
- **Saída**: Tarefa atribuída ao colaborador com status "ALOCADA"

#### **Etapa 6: Execução do Serviço**
- **Responsável**: Colaborador técnico
- **Ação**: O colaborador recebe a tarefa com informações detalhadas. Realiza o serviço e registra a conclusão através de:
  - Descrição do que foi feito
  - Fotos antes e depois
  - Tempo gasto
  - Materiais utilizados
- **Saída**: Tarefa com status "CONCLUÍDA" e evidências registradas

#### **Etapa 7: Validação e Fechamento**
- **Responsável**: Gestor do prédio
- **Ação**: O gestor valida se o serviço foi executado conforme solicitado. Se aprovado, a tarefa é fechada. Se houver problemas, retorna para ajustes.
- **Saída**: Tarefa com status "FINALIZADA" ou "REABERTA"

### 6.2 Visualização do Fluxo

```
GESTOR DO PRÉDIO → CHAPLIN (Tobogã) → LÍDER → COLABORADOR → EXECUÇÃO → VALIDAÇÃO
   (Cria)           (Registra)      (Aloca)   (Executa)      (Registra)   (Aprova)
```

### 6.3 Benefícios do Fluxo Otimizado

| Benefício | Impacto |
|-----------|--------|
| **Centralização** | Todas as demandas em um único lugar |
| **Rastreabilidade** | Histórico completo de cada tarefa |
| **Eficiência** | Redução de tempo em comunicações informais |
| **Qualidade** | Especificações claras reduzem retrabalho |
| **Documentação** | Evidências fotográficas para auditoria |
| **Responsabilização** | Cada etapa tem um responsável identificado |

---

## 7. Proposta de Valor

A Chaplin entrega valor através de três pilares fundamentais:

### 7.1 Pilar 1: Organização e Centralização

**O Problema**: Informações dispersas em múltiplos canais (WhatsApp, email, papel)

**A Solução**: Plataforma única onde todas as demandas são registradas, categorizadas e rastreadas

**O Valor**: Redução significativa do tempo gasto em coordenação e busca de informações

### 7.2 Pilar 2: Eficiência Operacional

**O Problema**: Retrabalho, tarefas incompletas e duplicadas

**A Solução**: Especificações claras, alocação inteligente e validação de qualidade

**O Valor**: Redução de retrabalho e aumento de produtividade

### 7.3 Pilar 3: Acessibilidade para Usuários Não-Tech

**O Problema**: Muitos colaboradores têm pouca experiência com tecnologia

**A Solução**: Interface extremamente simples, intuitiva e com linguagem clara

**O Valor**: Todos podem usar sem necessidade de treinamento extenso

---

## 8. Diferenciais da Chaplin

### 8.1 Diferencial 1: Especialização para o Setor de Hospedagem

A Chaplin é construída especificamente para o setor de hospedagem:

- Interface adaptada para o fluxo de manutenção hoteleira
- Categorias de problemas pré-configuradas
- Conformidade com padrões da indústria

### 8.2 Diferencial 2: Extrema Simplicidade e Intuitividade

O grande diferencial da Chaplin é ser **acessível para usuários com pouca experiência tecnológica**:

- Interface limpa e sem complexidades desnecessárias
- Linguagem clara em português simples
- Poucos cliques para realizar ações
- Ícones e cores para facilitar compreensão

### 8.3 Diferencial 3: Documentação Integrada com Evidências

A Chaplin captura evidências visuais e descritivas de cada etapa:

- Fotos antes e depois
- Descrição detalhada do problema e da solução
- Registro de tempo e materiais utilizados
- Histórico completo para auditoria

### 8.4 Diferencial 4: Comunicação Centralizada

Substitui comunicação fragmentada em WhatsApp por um sistema centralizado:

- Chat integrado por tarefa
- Histórico completo de comunicação
- Notificações claras
- Redução de informações perdidas

### 8.5 Diferencial 5: Customizável por Empresa

Cada empresa terceirizada pode:

- Customizar cores e logo
- Configurar categorias de problemas
- Gerenciar seus próprios usuários
- Adaptar o fluxo às suas necessidades

---

## 9. Requisitos Funcionais

### 9.1 Autenticação e Gestão de Usuários

- Cadastro de usuários com diferentes roles (Admin, Gestor, Líder, Colaborador)
- Login seguro com sessões Django
- Perfil de usuário com informações pessoais
- Foto de perfil
- Recuperação de senha

### 9.2 Gestão de Empresas (Para Admin)

- Criar e gerenciar empresa terceirizada
- Customizar logo e cores da empresa
- Gerenciar usuários da empresa
- Visualizar relatórios gerais

### 9.3 Gestão de Tarefas

- Criar tarefa com: título, descrição, prioridade, data de vencimento, quarto
- Listar tarefas com filtros (status, prioridade, responsável)
- Atribuir tarefa a colaborador
- Completar tarefa com foto e descrição de evidência
- Visualizar histórico de tarefas
- Mudar status da tarefa (Aberta → Alocada → Concluída → Finalizada)

### 9.4 Dashboard

- **Gestor do Prédio**: Visualiza status de suas tarefas
- **Líder**: Visualiza todas as tarefas recebidas e desempenho dos colaboradores
- **Colaborador**: Visualiza tarefas atribuídas a ele
- **Admin**: Visualiza estatísticas gerais da empresa

### 9.5 Chat/Comunicação

- Mensagens integradas por tarefa
- Envio e recebimento de mensagens
- Histórico de comunicação

### 9.6 Upload de Fotos

- Upload de fotos de evidência ao completar tarefa
- Armazenamento em cloud (S3)
- Visualização de fotos no histórico

---

## 10. Requisitos Não-Funcionais

### 10.1 Performance

- Respostas rápidas (< 2 segundos)
- Páginas carregam em menos de 3 segundos
- Suporte para 100+ usuários simultâneos

### 10.2 Segurança

- Autenticação segura com sessões Django
- Criptografia de senhas
- Proteção contra CSRF
- HTTPS em produção

### 10.3 Escalabilidade

- Arquitetura preparada para crescimento
- Banco de dados normalizado
- Código modular e reutilizável

### 10.4 Confiabilidade

- Backups regulares do banco de dados
- Tratamento de erros robusto
- Logs de todas as ações importantes

### 10.5 Usabilidade

- Interface intuitiva para usuários não-tech
- Linguagem clara e simples
- Responsivo em mobile e desktop
- Acessibilidade (contraste, tamanho de fonte)

---

## 11. Arquitetura Técnica

### 11.1 Stack Tecnológico

| Camada | Tecnologia | Justificativa |
|--------|-----------|--------------|
| **Frontend** | HTML, CSS, JavaScript, Tailwind CSS | Simples, intuitivo, responsivo |
| **Backend** | Django + Templates | Integrado, seguro, com boas práticas |
| **Banco de Dados** | MySQL | Relacional, ACID, escalável |
| **Armazenamento de Arquivos** | AWS S3 | Escalável, seguro, barato |
| **Autenticação** | Sessões Django | Simples, segura, integrada |

### 11.2 Estrutura do Projeto

```
chaplin/
├── manage.py
├── chaplin_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── tasks/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   ├── messages/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── templates/
│   └── companies/
│       ├── models.py
│       ├── views.py
│       └── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── login.html
│   └── dashboard.html
└── requirements.txt
```

### 11.3 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                   Django Application                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Templates (HTML) + Static Files (CSS/JS)           │   │
│  │  - Login                                             │   │
│  │  - Dashboard                                         │   │
│  │  - Tarefas (CRUD)                                    │   │
│  │  - Chat                                              │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Views (Lógica de Negócio)                           │   │
│  │  - Autenticação                                      │   │
│  │  - Gestão de Tarefas                                 │   │
│  │  - Gestão de Usuários                                │   │
│  │  - Chat                                              │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Models (Banco de Dados)                             │   │
│  │  - User                                              │   │
│  │  - Company                                           │   │
│  │  - Task                                              │   │
│  │  - Message                                           │   │
│  └──────────────────────────────────────────────────────┘   │
└────────────────────────┬─────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼───────┐ ┌─────▼──────┐ ┌──────▼────────┐
│   MySQL DB    │ │  AWS S3    │ │   Logs        │
│               │ │  (Fotos)   │ │               │
└───────────────┘ └────────────┘ └───────────────┘
```

---

## 12. Cronograma de Desenvolvimento

| Período | Atividade | Duração |
|---------|-----------|---------|
| **Fevereiro** | Documentação, diagramas, setup técnico | 4 semanas |
| **Março** | Backend: Modelos + Views de autenticação | 4 semanas |
| **Abril** | Frontend: Templates + CRUD de tarefas | 4 semanas |
| **Maio** | Chat + Upload S3 + Testes | 4 semanas |
| **Junho** | Documentação, slides, ajustes finais | 4 semanas |
| **Julho** | Apresentação final | 1 semana |

---

## 13. Conclusão

A Chaplin surge de uma necessidade real identificada em uma empresa do setor de hospedagem. O projeto visa resolver problemas concretos de comunicação, organização e acessibilidade tecnológica, oferecendo uma solução simples, intuitiva e centralizada para gestão de tarefas de manutenção.

O diferencial principal da Chaplin é sua extrema simplicidade e acessibilidade para usuários com pouca experiência tecnológica, algo que plataformas genéricas não oferecem. Além disso, a aplicação é customizável, permitindo que cada empresa terceirizada a adapte conforme suas necessidades.

Com a implementação proposta, espera-se alcançar:
- Centralização de todas as demandas
- Redução de comunicação fragmentada em WhatsApp
- Melhor rastreabilidade de tarefas
- Maior eficiência operacional
- Satisfação dos usuários, especialmente aqueles com pouca experiência tecnológica
- Uma ferramenta que empresas terceirizadas possam oferecer aos seus clientes

---

## 14. Referências

- Django Documentation: https://docs.djangoproject.com/
- Django Templates: https://docs.djangoproject.com/en/stable/topics/templates/
- AWS S3: https://aws.amazon.com/s3/
- Tailwind CSS: https://tailwindcss.com/
- MySQL: https://www.mysql.com/

---

**Documento preparado para apresentação de TCC - ETEC**

Data: Fevereiro de 2025
