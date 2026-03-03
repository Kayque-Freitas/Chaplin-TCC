# 📊 Diagramas - Chaplin

## 1️⃣ Diagrama de Caso de Uso

```mermaid
graph TB
    Cliente["👤 Cliente"]
    Profissional["👷 Profissional"]
    Admin["👨‍💼 Admin"]
    Sistema["🖥️ Sistema"]

    Cliente -->|Cadastrar| Autenticacao["Autenticação"]
    Profissional -->|Cadastrar| Autenticacao
    Admin -->|Cadastrar| Autenticacao
    
    Cliente -->|Publicar Tarefa| PublicarTarefa["Publicar Tarefa"]
    Profissional -->|Visualizar Tarefas| BuscaTarefas["Buscar Tarefas"]
    Profissional -->|Fazer Proposta| FazerProposta["Fazer Proposta"]
    
    Cliente -->|Visualizar Propostas| VisualizarPropostas["Visualizar Propostas"]
    Cliente -->|Aceitar Proposta| AceitarProposta["Aceitar Proposta"]
    
    Cliente -->|Chat| Chat["Chat em Tempo Real"]
    Profissional -->|Chat| Chat
    
    Cliente -->|Pagar| Pagamento["Processar Pagamento"]
    Sistema -->|Transferir| Pagamento
    
    Cliente -->|Avaliar| Avaliacao["Avaliar Profissional"]
    Profissional -->|Avaliar| Avaliacao
    
    Admin -->|Gerenciar| GerenciarUsuarios["Gerenciar Usuários"]
    Admin -->|Resolver| Disputas["Resolver Disputas"]
    Admin -->|Visualizar| Relatorios["Relatórios"]
    
    Sistema -->|Notificar| Notificacoes["Notificações"]
    
    style Cliente fill:#e1f5ff
    style Profissional fill:#f3e5f5
    style Admin fill:#fff3e0
    style Sistema fill:#e8f5e9
```

---

## 2️⃣ Diagrama de Fluxo - Publicar Tarefa

```mermaid
flowchart TD
    A["👤 Cliente Acessa Sistema"] --> B{Autenticado?}
    B -->|Não| C["Fazer Login"]
    C --> D["Acessa Dashboard"]
    B -->|Sim| D
    
    D --> E["Clica em 'Nova Tarefa'"]
    E --> F["Preenche Formulário"]
    F --> G{Todos os campos<br/>obrigatórios?}
    G -->|Não| H["Exibe Erro"]
    H --> F
    G -->|Sim| I["Upload de Fotos"]
    I --> J["Revisa Informações"]
    J --> K{Confirma?}
    K -->|Não| F
    K -->|Sim| L["Publica Tarefa"]
    
    L --> M["Atualiza Status: ABERTA"]
    M --> N["Busca Profissionais Relevantes"]
    N --> O["Envia Notificações"]
    O --> P["Exibe Confirmação"]
    P --> Q["Redireciona para Detalhes"]
    
    style A fill:#e1f5ff
    style L fill:#4caf50,color:#fff
    style H fill:#f44336,color:#fff
    style P fill:#4caf50,color:#fff
```

---

## 3️⃣ Diagrama de Fluxo - Fazer Proposta

```mermaid
flowchart TD
    A["👷 Profissional Visualiza Tarefas"] --> B["Clica em Tarefa Interessante"]
    B --> C["Visualiza Detalhes"]
    C --> D{Interessado?}
    D -->|Não| E["Volta à Lista"]
    D -->|Sim| F["Clica em 'Fazer Proposta'"]
    
    F --> G["Preenche Formulário"]
    G --> H["Define Valor"]
    H --> I["Descreve Solução"]
    I --> J["Define Tempo Estimado"]
    J --> K{Já fez proposta<br/>nesta tarefa?}
    K -->|Sim| L["Exibe Erro"]
    L --> G
    K -->|Não| M["Revisa Proposta"]
    M --> N{Confirma?}
    N -->|Não| G
    N -->|Sim| O["Envia Proposta"]
    
    O --> P["Atualiza Status: PENDENTE"]
    P --> Q["Notifica Cliente"]
    Q --> R["Exibe Confirmação"]
    R --> S["Profissional Aguarda Resposta"]
    
    style A fill:#f3e5f5
    style O fill:#4caf50,color:#fff
    style L fill:#f44336,color:#fff
```

---

## 4️⃣ Diagrama de Fluxo - Aceitar Proposta e Pagar

```mermaid
flowchart TD
    A["👤 Cliente Recebe Propostas"] --> B["Visualiza Todas as Propostas"]
    B --> C["Compara Valores e Descrições"]
    C --> D["Seleciona Melhor Proposta"]
    D --> E["Clica em 'Aceitar'"]
    
    E --> F["Sistema Rejeita Outras Propostas"]
    F --> G["Atualiza Tarefa: EM_PROGRESSO"]
    G --> H["Notifica Profissional Aceito"]
    H --> I["Notifica Profissionais Rejeitados"]
    
    I --> J["Cliente Visualiza Opção de Pagamento"]
    J --> K["Clica em 'Pagar Agora'"]
    K --> L["Redireciona para Stripe"]
    
    L --> M["Cliente Insere Dados do Cartão"]
    M --> N["Stripe Processa Pagamento"]
    N --> O{Pagamento<br/>Aprovado?}
    O -->|Não| P["Exibe Erro"]
    P --> Q["Cliente Tenta Novamente"]
    Q --> M
    O -->|Sim| R["Cria Registro de Pagamento"]
    
    R --> S["Calcula Comissão 10%"]
    S --> T["Retém Valor até Conclusão"]
    T --> U["Notifica Profissional"]
    U --> V["Exibe Confirmação"]
    V --> W["Abre Chat para Comunicação"]
    
    style A fill:#e1f5ff
    style E fill:#4caf50,color:#fff
    style O fill:#ff9800,color:#fff
    style R fill:#4caf50,color:#fff
```

---

## 5️⃣ Diagrama de Fluxo - Chat em Tempo Real

```mermaid
flowchart TD
    A["👤 Cliente / 👷 Profissional"] --> B["Acessa Tarefa"]
    B --> C["Abre Aba de Chat"]
    C --> D["Visualiza Histórico"]
    D --> E["Digita Mensagem"]
    E --> F["Clica em Enviar"]
    
    F --> G["Socket.io Envia Mensagem"]
    G --> H["Salva no Banco de Dados"]
    H --> I["Emite para Outro Usuário"]
    I --> J["Exibe Mensagem em Tempo Real"]
    J --> K["Marca como Lida"]
    K --> L["Notifica Remetente"]
    
    L --> M{Novo Usuário<br/>Digita?}
    M -->|Sim| N["Exibe 'Digitando...'"]
    N --> O["Aguarda Envio"]
    M -->|Não| P["Aguarda Próxima Mensagem"]
    
    O --> E
    P --> E
    
    style A fill:#e1f5ff
    style F fill:#4caf50,color:#fff
    style J fill:#2196f3,color:#fff
```

---

## 6️⃣ Diagrama de Fluxo - Conclusão e Avaliação

```mermaid
flowchart TD
    A["👷 Profissional Conclui Serviço"] --> B["Clica em 'Marcar Concluído'"]
    B --> C["Notifica Cliente"]
    C --> D["👤 Cliente Recebe Notificação"]
    
    D --> E{Serviço<br/>Satisfatório?}
    E -->|Não| F["Solicita Revisão"]
    F --> G["👷 Profissional Revisa"]
    G --> H["Retorna ao Passo A"]
    
    E -->|Sim| I["Clica em 'Confirmar Conclusão'"]
    I --> J["Sistema Libera Pagamento"]
    J --> K["Calcula Ganho do Profissional"]
    K --> L["Transfere para Conta"]
    L --> M["Notifica Profissional"]
    
    M --> N["Exibe Formulário de Avaliação"]
    N --> O["Cliente Avalia Profissional"]
    O --> P["Define Nota 1-5"]
    P --> Q["Escreve Comentário"]
    Q --> R["Submete Avaliação"]
    
    R --> S["Salva Avaliação"]
    S --> T["Atualiza Rating do Profissional"]
    T --> U["Notifica Profissional"]
    U --> V["Tarefa Finalizada"]
    
    style A fill:#f3e5f5
    style I fill:#4caf50,color:#fff
    style J fill:#4caf50,color:#fff
    style R fill:#2196f3,color:#fff
    style V fill:#4caf50,color:#fff
```

---

## 7️⃣ Diagrama de Fluxo - Busca e Filtragem

```mermaid
flowchart TD
    A["👷 Profissional Acessa Tarefas"] --> B["Visualiza Lista de Tarefas Abertas"]
    B --> C["Aplica Filtros"]
    
    C --> D["Seleciona Categoria"]
    C --> E["Seleciona Localização"]
    C --> F["Define Faixa de Orçamento"]
    C --> G["Seleciona Prioridade"]
    
    D --> H["Sistema Aplica Filtros"]
    E --> H
    F --> H
    G --> H
    
    H --> I["Busca no Banco de Dados"]
    I --> J["Retorna Tarefas Relevantes"]
    J --> K["Ordena por Critério"]
    K --> L{Mais de 10<br/>resultados?}
    
    L -->|Sim| M["Pagina Resultados"]
    L -->|Não| N["Exibe Todos"]
    
    M --> O["Exibe Lista com Filtros Aplicados"]
    N --> O
    
    O --> P["Profissional Visualiza Tarefa"]
    P --> Q["Clica em Detalhes"]
    Q --> R["Visualiza Informações Completas"]
    R --> S["Vê Rating do Cliente"]
    R --> T["Vê Número de Propostas"]
    
    S --> U{Interessado?}
    T --> U
    U -->|Sim| V["Faz Proposta"]
    U -->|Não| W["Volta à Lista"]
    
    style A fill:#f3e5f5
    style B fill:#e3f2fd
    style O fill:#f5f5f5
    style V fill:#4caf50,color:#fff
```

---

## 8️⃣ Diagrama de Fluxo - Administração

```mermaid
flowchart TD
    A["👨‍💼 Admin Acessa Painel"] --> B["Visualiza Dashboard"]
    B --> C["Opções de Gerenciamento"]
    
    C --> D["Gerenciar Usuários"]
    C --> E["Gerenciar Tarefas"]
    C --> F["Resolver Disputas"]
    C --> G["Visualizar Relatórios"]
    
    D --> D1["Listar Todos os Usuários"]
    D1 --> D2["Filtrar por Tipo"]
    D2 --> D3{Ação?}
    D3 -->|Verificar| D4["Validar Profissional"]
    D3 -->|Bloquear| D5["Desativar Usuário"]
    D3 -->|Visualizar| D6["Ver Detalhes"]
    
    E --> E1["Listar Todas as Tarefas"]
    E1 --> E2["Filtrar por Status"]
    E2 --> E3{Ação?}
    E3 -->|Cancelar| E4["Cancelar Tarefa"]
    E3 -->|Revisar| E5["Verificar Conteúdo"]
    
    F --> F1["Listar Disputas"]
    F1 --> F2["Visualizar Detalhes"]
    F2 --> F3{Decisão?}
    F3 -->|Favorecer Cliente| F4["Reembolsar"]
    F3 -->|Favorecer Profissional| F5["Liberar Pagamento"]
    F3 -->|Rejeitar Ambos| F6["Investigar Mais"]
    
    G --> G1["Gráficos de Atividade"]
    G --> G2["Relatório Financeiro"]
    G --> G3["Relatório de Usuários"]
    
    style A fill:#fff3e0
    style C fill:#ffe0b2
    style D4 fill:#4caf50,color:#fff
    style F4 fill:#2196f3,color:#fff
```

---

## 9️⃣ Diagrama de Arquitetura do Sistema

```mermaid
graph TB
    subgraph Frontend["🖥️ Frontend (React + TypeScript)"]
        Home["Home Page"]
        Dashboard["Dashboard"]
        Tarefas["Tarefas"]
        Chat["Chat"]
        Perfil["Perfil"]
    end
    
    subgraph Backend["⚙️ Backend (Node.js + Express)"]
        Auth["Autenticação"]
        TarefasAPI["Tarefas API"]
        PropostasAPI["Propostas API"]
        ChatAPI["Chat API"]
        PagamentosAPI["Pagamentos API"]
    end
    
    subgraph Servicos["🔧 Serviços Externos"]
        Stripe["Stripe (Pagamentos)"]
        SendGrid["SendGrid (Email)"]
        AWS["AWS S3 (Imagens)"]
        Twilio["Twilio (SMS)"]
    end
    
    subgraph Dados["💾 Banco de Dados"]
        MySQL["MySQL"]
        Redis["Redis"]
    end
    
    Frontend -->|HTTPS + WebSocket| Backend
    Backend --> Stripe
    Backend --> SendGrid
    Backend --> AWS
    Backend --> Twilio
    Backend --> MySQL
    Backend --> Redis
    
    style Frontend fill:#e3f2fd
    style Backend fill:#f3e5f5
    style Servicos fill:#fff3e0
    style Dados fill:#e8f5e9
```

---

## 🔟 Diagrama de Sequência - Fluxo Completo de Tarefa

```mermaid
sequenceDiagram
    participant C as 👤 Cliente
    participant S as 🖥️ Sistema
    participant P as 👷 Profissional
    participant ST as 💳 Stripe
    
    C->>S: 1. Publica Tarefa
    S->>S: Valida Dados
    S->>S: Salva no Banco
    S->>P: Notifica Profissionais
    
    P->>S: 2. Faz Proposta
    S->>S: Valida Proposta
    S->>C: Notifica Cliente
    
    C->>S: 3. Aceita Proposta
    S->>S: Rejeita Outras Propostas
    S->>P: Notifica Aceitação
    
    C->>S: 4. Inicia Pagamento
    S->>ST: Cria Sessão Checkout
    C->>ST: 5. Paga com Cartão
    ST->>S: Confirma Pagamento
    S->>S: Retém Valor (10% comissão)
    
    P->>S: 6. Marca Concluído
    S->>C: Notifica Conclusão
    
    C->>S: 7. Confirma Conclusão
    S->>S: Libera Pagamento
    S->>P: Transfere Valor
    
    C->>S: 8. Avalia Profissional
    P->>S: 9. Avalia Cliente
    S->>S: Atualiza Ratings
    
    S->>C: Tarefa Finalizada ✅
    S->>P: Tarefa Finalizada ✅
```

---

## 1️⃣1️⃣ Diagrama de Estados - Tarefa

```mermaid
stateDiagram-v2
    [*] --> ABERTA: Publicada
    
    ABERTA --> EM_PROGRESSO: Proposta Aceita
    ABERTA --> CANCELADA: Cliente Cancela
    
    EM_PROGRESSO --> CONCLUIDA: Profissional Conclui
    EM_PROGRESSO --> CANCELADA: Disputa
    
    CONCLUIDA --> AVALIADA: Cliente Avalia
    
    CANCELADA --> [*]
    AVALIADA --> [*]
    
    note right of ABERTA
        Aguardando propostas
        Profissionais podem fazer bids
    end note
    
    note right of EM_PROGRESSO
        Profissional trabalha
        Cliente e profissional comunicam
    end note
    
    note right of CONCLUIDA
        Serviço finalizado
        Aguardando confirmação
    end note
    
    note right of AVALIADA
        Ambos avaliaram
        Pagamento liberado
    end note
```

---

## 1️⃣2️⃣ Diagrama de Estados - Proposta

```mermaid
stateDiagram-v2
    [*] --> PENDENTE: Profissional Faz Bid
    
    PENDENTE --> ACEITA: Cliente Aceita
    PENDENTE --> REJEITADA: Cliente Rejeita
    PENDENTE --> CANCELADA: Tarefa Cancelada
    
    ACEITA --> [*]: Tarefa Iniciada
    REJEITADA --> [*]
    CANCELADA --> [*]
    
    note right of PENDENTE
        Aguardando resposta do cliente
        Profissional pode visualizar
    end note
    
    note right of ACEITA
        Profissional foi escolhido
        Tarefa muda para EM_PROGRESSO
    end note
```

---

## 1️⃣3️⃣ Diagrama de Componentes

```mermaid
graph TB
    subgraph UI["UI Components"]
        Button["Button"]
        Card["Card"]
        Form["Form"]
        Modal["Modal"]
        Input["Input"]
    end
    
    subgraph Pages["Pages"]
        Home["Home"]
        Dashboard["Dashboard"]
        TarefasPage["Tarefas"]
        ChatPage["Chat"]
    end
    
    subgraph Hooks["Custom Hooks"]
        useAuth["useAuth"]
        useTarefas["useTarefas"]
        useChat["useChat"]
    end
    
    subgraph Store["State Management"]
        AuthStore["Auth Store"]
        FilterStore["Filter Store"]
    end
    
    subgraph Services["Services"]
        TRPCClient["tRPC Client"]
        SocketClient["Socket.io Client"]
        StripeClient["Stripe Client"]
    end
    
    Pages -->|Usa| UI
    Pages -->|Usa| Hooks
    Hooks -->|Usa| Store
    Hooks -->|Usa| Services
    
    style UI fill:#e3f2fd
    style Pages fill:#f3e5f5
    style Hooks fill:#fff3e0
    style Store fill:#e8f5e9
    style Services fill:#fce4ec
```

---

Esses diagramas cobrem:
- ✅ Caso de uso completo
- ✅ Fluxos principais do sistema
- ✅ Arquitetura geral
- ✅ Sequência de operações
- ✅ Estados das entidades
- ✅ Componentes do sistema

Quer que eu gere os slides agora com todos esses diagramas?
