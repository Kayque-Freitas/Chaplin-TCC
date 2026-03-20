# Diagramas do Sistema - Chaplin

Este documento apresenta a modelagem visual do Chaplin, facilitando o entendimento dos processos e da estrutura técnica.

## 1. Diagrama de Casos de Uso

Este diagrama ilustra como os diferentes atores interagem com as funcionalidades principais do sistema.

```mermaid
graph TD
    subgraph Atores
        G[Gestor do Prédio]
        L[Líder de Equipe]
        C[Colaborador Técnico]
        A[Administrador]
    end

    subgraph "Funcionalidades Chaplin"
        F1(Registrar Demanda/Tarefa)
        F2(Alocar Colaborador)
        F3(Registrar Execução e Fotos)
        F4(Validar e Finalizar Tarefa)
        F5(Chat por Tarefa)
        F6(Gerenciar Empresa e Usuários)
    end

    G --> F1
    G --> F4
    G --> F5

    L --> F2
    L --> F4
    L --> F5

    C --> F3
    C --> F5

    A --> F6
    A --> F4
```

---

## 2. Fluxo Operacional (As 7 Etapas)

O caminho que uma tarefa percorre desde a identificação do problema até o fechamento.

```mermaid
flowchart LR
    E1[1. Identificação] --> E2[2. Reporte]
    E2 --> E3[3. Registro na Chaplin]
    E3 --> E4[4. Recebimento pela Empresa]
    E4 --> E5[5. Alocação]
    E5 --> E6[6. Execução e Fotos]
    E6 --> E7[7. Validação e Fechamento]

    style E3 fill:#f9f,stroke:#333,stroke-width:2px
    style E6 fill:#bbf,stroke:#333,stroke-width:2px
    style E7 fill:#bfb,stroke:#333,stroke-width:2px
```

---

## 3. Arquitetura do Sistema (MTV)

Como o framework Django organiza os dados e a interface.

```mermaid
graph TB
    subgraph Navegador
        UI[Interface HTML/Tailwind]
    end

    subgraph "Servidor Django"
        V[Views - Lógica de Negócio]
        T[Templates - Renderização]
        M[Models - Banco de Dados]
    end

    subgraph Persistência
        DB[(SQLite / PostgreSQL)]
        S3[Armazenamento de Fotos]
    end

    UI <--> V
    V <--> T
    V <--> M
    M <--> DB
    V <--> S3
```

---

## 4. Diagrama de Estados da Tarefa

Os status que uma tarefa pode assumir durante seu ciclo de vida.

```mermaid
stateDiagram-v2
    [*] --> ABERTA: Registro (Gestor)
    ABERTA --> RECEBIDA: Visualização (Líder)
    RECEBIDA --> ALOCADA: Atribuição (Líder)
    ALOCADA --> CONCLUIDA: Execução (Colaborador)
    CONCLUIDA --> FINALIZADA: Validação (Gestor)
    CONCLUIDA --> ALOCADA: Rejeição/Ajuste
    FINALIZADA --> [*]
```
