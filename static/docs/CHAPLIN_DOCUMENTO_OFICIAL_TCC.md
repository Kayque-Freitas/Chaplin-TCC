# Chaplin: Plataforma de Gestão de Tarefas para Serviços de Manutenção

**Documento Oficial do Projeto de TCC - ETEC**

---

## 1. Introdução

A Chaplin é uma plataforma de gestão de tarefas desenvolvida para otimizar processos operacionais em empresas que prestam serviços de manutenção e reposição em estabelecimentos hoteleiros e propriedades de aluguel de curta duração (Airbnb). Este projeto surgiu de uma necessidade real identificada em uma empresa do setor, visando resolver problemas concretos de comunicação e organização do trabalho.

---

## 2. Origem da Ideia

### 2.1 A Empresa Charlie

A ideia do projeto Chaplin originou-se de uma conversa com o pai de um dos integrantes do grupo, que trabalha na empresa **Charlie**, uma empresa especializada em prestação de serviços de manutenção e reposição para hotéis e propriedades de aluguel de curta duração.

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

A Chaplin é uma plataforma de gestão de tarefas que centraliza, organiza e simplifica o fluxo de manutenção e reposição em estabelecimentos hoteleiros e propriedades de aluguel de curta duração, conectando gestores de prédios, empresas terceirizadas e colaboradores técnicos em um único ecossistema digital, com foco em simplicidade e acessibilidade para usuários com pouca experiência tecnológica.

### 4.2 Segmento de Mercado Alvo

| Aspecto | Descrição |
|--------|-----------|
| **Clientes Primários** | Gestores de prédios, síndicos e gerentes de operações de hotéis e Airbnb |
| **Usuários Finais** | Camareiras, eletricistas, encanadores, pintores e demais profissionais técnicos |
| **Empresas Terceirizadas** | Empresas de limpeza, manutenção predial e suporte operacional |
| **Escala** | Pequenas a médias propriedades (10-500 quartos) |

### 4.3 Objetivos do Projeto

**Objetivo Geral:**
Desenvolver uma plataforma web que centralize o fluxo de gestão de tarefas de manutenção, tornando-o mais organizado, eficiente e acessível para usuários com diferentes níveis de experiência tecnológica.

**Objetivos Específicos:**
1. Criar uma interface intuitiva e simples, acessível para usuários não-tech
2. Centralizar todas as demandas de manutenção em um único lugar
3. Implementar rastreabilidade completa de cada tarefa
4. Permitir comunicação integrada entre todos os atores do processo
5. Documentar evidências (fotos e descrições) de conclusão de tarefas
6. Reduzir o tempo de coordenação e comunicação informal

---

## 5. Fluxo Operacional

### 5.1 Descrição Detalhada do Processo

O fluxo operacional da Chaplin segue sete etapas principais:

#### **Etapa 1: Identificação de Problemas**
- **Responsável**: Camareiras ou profissionais de limpeza
- **Ação**: Após checkout do hóspede, o profissional realiza inspeção do quarto e identifica problemas (vazamentos, lâmpadas queimadas, móveis danificados) ou necessidades de reposição
- **Saída**: Lista de problemas identificados

#### **Etapa 2: Reporte ao Gestor**
- **Responsável**: Camareiras ou profissionais de limpeza
- **Ação**: O profissional comunica os problemas ao gestor do prédio
- **Saída**: Informação chega ao gestor

#### **Etapa 3: Registro na Plataforma**
- **Responsável**: Gestor do prédio ou gerente de operações
- **Ação**: O gestor acessa a Chaplin e registra a ocorrência, incluindo:
  - Número do quarto
  - Categoria do problema (elétrico, hidráulico, estrutural, limpeza, etc.)
  - Descrição detalhada
  - Fotos do problema
  - Prioridade (urgente, alta, normal, baixa)
  - Prazo desejado de conclusão
- **Saída**: Tarefa criada no sistema com status "ABERTA"

#### **Etapa 4: Direcionamento à Empresa Terceirizada**
- **Responsável**: Sistema Chaplin (automático) ou Gestor (manual)
- **Ação**: A tarefa é direcionada à empresa terceirizada responsável
- **Saída**: Notificação enviada à empresa

#### **Etapa 5: Alocação ao Colaborador**
- **Responsável**: Líder da equipe ou gestor da empresa terceirizada
- **Ação**: O líder recebe a demanda e aloca ao colaborador mais adequado
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
- **Responsável**: Gestor do prédio ou camareiras
- **Ação**: O gestor valida se o serviço foi executado conforme solicitado. Se aprovado, a tarefa é fechada. Se houver problemas, retorna para ajustes.
- **Saída**: Tarefa com status "FINALIZADA" ou "REABERTA"

### 5.2 Visualização do Fluxo

```
CAMAREIRAS → GESTOR → CHAPLIN → EMPRESA → LÍDER → COLABORADOR → EXECUÇÃO → VALIDAÇÃO
  (Identifica)  (Comunica) (Registra) (Recebe) (Aloca) (Executa)    (Registra)  (Aprova)
```

### 5.3 Benefícios do Fluxo Otimizado

| Benefício | Impacto |
|-----------|--------|
| **Centralização** | Todas as demandas em um único lugar, sem perda de informações |
| **Rastreabilidade** | Histórico completo de cada tarefa desde criação até conclusão |
| **Eficiência** | Redução de tempo em comunicações informais e coordenação |
| **Qualidade** | Especificações claras reduzem retrabalho e erros |
| **Documentação** | Evidências fotográficas e descritivas para auditoria |
| **Responsabilização** | Cada etapa tem um responsável identificado |

---

## 6. Proposta de Valor

A Chaplin entrega valor através de três pilares fundamentais:

### 6.1 Pilar 1: Organização e Centralização

**O Problema**: Informações dispersas em múltiplos canais (WhatsApp, email, papel)

**A Solução**: Plataforma única onde todas as demandas são registradas, categorizadas e rastreadas

**O Valor**: Redução significativa do tempo gasto em coordenação e busca de informações

### 6.2 Pilar 2: Eficiência Operacional

**O Problema**: Retrabalho, tarefas incompletas e duplicadas

**A Solução**: Especificações claras, alocação inteligente e validação de qualidade

**O Valor**: Redução de retrabalho e aumento de produtividade

### 6.3 Pilar 3: Acessibilidade para Usuários Não-Tech

**O Problema**: Muitos colaboradores têm pouca experiência com tecnologia

**A Solução**: Interface extremamente simples, intuitiva e com linguagem clara

**O Valor**: Todos podem usar sem necessidade de treinamento extenso

---

## 7. Diferenciais da Chaplin

### 7.1 Diferencial 1: Especialização para o Setor de Hospedagem

A Chaplin é construída especificamente para o setor de hospedagem, ao contrário de plataformas genéricas. Isso significa:

- Interface adaptada para o fluxo de manutenção hoteleira
- Categorias de problemas pré-configuradas
- Conformidade com padrões da indústria

### 7.2 Diferencial 2: Extrema Simplicidade e Intuitividade

O grande diferencial da Chaplin é ser **acessível para usuários com pouca experiência tecnológica**:

- Interface limpa e sem complexidades desnecessárias
- Linguagem clara em português simples
- Poucos cliques para realizar ações
- Ícones e cores para facilitar compreensão
- Sem jargão técnico

### 7.3 Diferencial 3: Documentação Integrada com Evidências

A Chaplin captura evidências visuais e descritivas de cada etapa:

- Fotos antes e depois
- Descrição detalhada do problema e da solução
- Registro de tempo e materiais utilizados
- Histórico completo para auditoria

### 7.4 Diferencial 4: Fluxo Colaborativo Multi-Ator

A Chaplin conecta todos os atores do processo em um único ecossistema:

- Camareiras (identificam problemas)
- Gestores de prédios (coordenam)
- Empresas terceirizadas (executam)
- Colaboradores técnicos (realizam serviço)

### 7.5 Diferencial 5: Comunicação Centralizada

Substitui comunicação fragmentada em WhatsApp por um sistema centralizado:

- Chat integrado por tarefa
- Histórico completo de comunicação
- Notificações claras
- Redução de informações perdidas

---

## 8. Requisitos Funcionais

### 8.1 Autenticação e Gestão de Usuários

- Cadastro de usuários com diferentes roles (Síndico, Gestor, Colaborador)
- Login seguro com sessões
- Perfil de usuário com informações pessoais
- Foto de perfil

### 8.2 Gestão de Propriedades

- Síndico pode registrar propriedades manualmente
- Busca de endereço por CEP (API externa)
- Detalhes manuais do quarto (número, andar, descrição)
- Listagem de propriedades por síndico

### 8.3 Gestão de Tarefas

- Criar tarefa com: título, descrição, prioridade, data de vencimento, quarto
- Listar tarefas com filtros (status, prioridade, responsável)
- Atribuir tarefa a colaborador
- Completar tarefa com foto e descrição de evidência
- Visualizar histórico de tarefas

### 8.4 Dashboard

- Gestor visualiza estatísticas de desempenho dos colaboradores
- Síndico visualiza status geral de tarefas
- Colaborador visualiza tarefas atribuídas a ele

### 8.5 Chat/Comunicação

- Mensagens integradas por tarefa
- Envio e recebimento de mensagens em tempo real (com polling)
- Histórico de comunicação

### 8.6 Upload de Fotos

- Upload de fotos de evidência ao completar tarefa
- Armazenamento em cloud (S3)
- Visualização de fotos no histórico

---

## 9. Requisitos Não-Funcionais

### 9.1 Performance

- Respostas das APIs em menos de 200ms
- Páginas carregam em menos de 3 segundos
- Suporte para 100+ usuários simultâneos

### 9.2 Segurança

- Autenticação segura com sessões Django
- Criptografia de senhas com bcrypt
- Proteção contra CSRF
- HTTPS em produção

### 9.3 Escalabilidade

- Arquitetura preparada para crescimento
- Banco de dados normalizado
- Código modular e reutilizável

### 9.4 Confiabilidade

- Backups regulares do banco de dados
- Tratamento de erros robusto
- Logs de todas as ações importantes

### 9.5 Usabilidade

- Interface intuitiva para usuários não-tech
- Linguagem clara e simples
- Responsivo em mobile e desktop
- Acessibilidade (contraste, tamanho de fonte)

---

## 10. Arquitetura Técnica

### 10.1 Stack Tecnológico

| Camada | Tecnologia | Justificativa |
|--------|-----------|--------------|
| **Frontend** | HTML, CSS, JavaScript, Tailwind CSS | Simples, intuitivo, responsivo |
| **Backend** | Django + Django Rest Framework | Framework robusto, seguro, com boas práticas |
| **Banco de Dados** | MySQL | Relacional, ACID, escalável |
| **Armazenamento de Arquivos** | AWS S3 | Escalável, seguro, barato |
| **Autenticação** | Sessões Django | Simples, segura, integrada |

### 10.2 Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend (HTML/CSS/JS)                 │
│                    (Navegador do Usuário)                   │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/HTTPS
┌────────────────────────▼────────────────────────────────────┐
│                   Backend (Django)                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  APIs REST (DRF)                                    │    │
│  │  - Users, Tasks, Properties, Messages              │    │
│  └─────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  Autenticação (Sessões)                             │    │
│  │  - Login, Logout, Permissões                        │    │
│  └─────────────────────────────────────────────────────┘    │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
┌───────▼───────┐ ┌─────▼──────┐ ┌──────▼────────┐
│   MySQL DB    │ │  AWS S3    │ │   Logs        │
│               │ │  (Fotos)   │ │               │
└───────────────┘ └────────────┘ └───────────────┘
```

---

## 11. Cronograma de Desenvolvimento

| Período | Atividade | Duração |
|---------|-----------|---------|
| **Fevereiro** | Documentação, diagramas, setup técnico | 4 semanas |
| **Março** | Backend: Autenticação + APIs de tarefas | 4 semanas |
| **Abril** | Frontend: Integração com backend | 4 semanas |
| **Maio** | Conclusão de tarefas + Chat + S3 | 4 semanas |
| **Junho** | Testes, documentação, slides | 4 semanas |
| **Julho** | Apresentação final | 1 semana |

---

## 12. Conclusão

A Chaplin surge de uma necessidade real identificada em uma empresa do setor de hospedagem. O projeto visa resolver problemas concretos de comunicação, organização e acessibilidade tecnológica, oferecendo uma solução simples, intuitiva e centralizada para gestão de tarefas de manutenção.

O diferencial principal da Chaplin é sua extrema simplicidade e acessibilidade para usuários com pouca experiência tecnológica, algo que plataformas genéricas não oferecem. Isso a torna uma solução viável e prática para empresas reais do setor.

Com a implementação proposta, espera-se alcançar:
- Centralização de todas as demandas
- Redução de comunicação fragmentada em WhatsApp
- Melhor rastreabilidade de tarefas
- Maior eficiência operacional
- Satisfação dos usuários, especialmente aqueles com pouca experiência tecnológica

---

## 13. Referências

- Django Documentation: https://docs.djangoproject.com/
- Django Rest Framework: https://www.django-rest-framework.org/
- AWS S3: https://aws.amazon.com/s3/
- Tailwind CSS: https://tailwindcss.com/

---

**Documento preparado para apresentação de TCC - ETEC**

Data: Fevereiro de 2025
