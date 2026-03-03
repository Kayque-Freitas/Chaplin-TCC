# Chaplin: Plano Estratégico para TCC - Apresentação em Julho

**Timeline: Fevereiro 2026 - Julho 2026 (5 meses)**

---

## 1. Análise da Situação

### 1.1 Restrições e Realidades

| Fator | Realidade |
|-------|-----------|
| **Tempo disponível** | ~5 meses (20 semanas) |
| **Tipo de projeto** | TCC (não é startup) |
| **Complexidade esperada** | Média (não ultra complexo, não CRUD simples) |
| **Equipe** | Presumo 2-4 pessoas |
| **Tecnologias** | Django + HTML/CSS (já decidido) |
| **Funcionalidades extras** | Sem rating, sem mapas complexos |

### 1.2 O que a Banca Espera

A banca de TCC quer ver:

✅ **Problema bem definido** - Você identificou um problema real  
✅ **Solução viável** - Seu sistema resolve o problema  
✅ **Implementação funcional** - Código que funciona, não apenas teoria  
✅ **Documentação clara** - Explicar o que fez e por quê  
✅ **Análise crítica** - Limitações, melhorias futuras  
✅ **Apresentação profissional** - Slides, demo, código limpo  

❌ **NÃO espera**: Uber do Brasil, startup pronta para IPO, 10 mil usuários

---

## 2. Escopo Realista para Julho

### 2.1 O Que DEVE Ter (Essencial)

```
✅ CORE DO SISTEMA
├── Autenticação (Login/Registro)
├── 3 Tipos de Usuários (Síndico, Gestor, Profissional)
├── Criar Tarefa de Manutenção
├── Listar Tarefas (com filtros básicos)
├── Atribuir Tarefa a Profissional
├── Profissional Completar Tarefa (com foto)
├── Dashboard Simples (estatísticas básicas)
└── Chat Básico (mensagens entre síndico e profissional)

✅ QUALIDADE TÉCNICA
├── Banco de dados normalizado
├── APIs REST documentadas
├── Validações no backend
├── Autenticação JWT
├── Testes unitários (mínimo 70% cobertura)
└── Código limpo e bem estruturado

✅ APRESENTAÇÃO
├── Slides profissionais (14-15 slides)
├── Demo funcional ao vivo
├── Documentação técnica
├── Diagrama de arquitetura
└── Vídeo de 2-3 minutos (backup se demo falhar)
```

### 2.2 O Que NÃO Precisa (Pode Deixar para "Trabalhos Futuros")

```
❌ DEIXAR PARA DEPOIS
├── Rating/Avaliações de profissionais
├── Mapas interativos (Google Maps)
├── Pagamentos (Stripe)
├── Notificações push
├── Sistema de propostas com lances
├── Integração com PMS de hotéis
├── App mobile nativo
├── Suporte multi-idioma
├── Dark mode
└── Análise de dados avançada
```

---

## 3. Roadmap de 5 Meses (Fevereiro - Julho)

### **FEVEREIRO (Semanas 1-4): Planejamento e Setup**

#### Semana 1-2: Documentação e Design
- [ ] Finalizar documento de requisitos (já tem base)
- [ ] Criar diagramas (ER, arquitetura, fluxos)
- [ ] Definir wireframes das telas principais
- [ ] Documentar API (endpoints, payloads)
- **Entrega**: Documento de 20-30 páginas

#### Semana 3-4: Setup Técnico
- [ ] Configurar repositório Git
- [ ] Setup Django (models, settings, migrations)
- [ ] Setup banco de dados MySQL
- [ ] Criar estrutura de pastas
- [ ] Configurar Docker (opcional mas recomendado)
- **Entrega**: Backend rodando localmente

---

### **MARÇO (Semanas 5-8): Backend Core**

#### Semana 5-6: Autenticação e Modelos
- [ ] Implementar User Model com 3 roles
- [ ] Implementar Task Model
- [ ] Implementar Property Model
- [ ] JWT Authentication
- [ ] Testes de autenticação
- **Entrega**: Login funcional

#### Semana 7-8: APIs de Tarefas
- [ ] Endpoint: Criar tarefa
- [ ] Endpoint: Listar tarefas (com filtros)
- [ ] Endpoint: Atualizar tarefa
- [ ] Endpoint: Atribuir profissional
- [ ] Testes dos endpoints
- **Entrega**: CRUD completo de tarefas

---

### **ABRIL (Semanas 9-12): Frontend + Integração**

#### Semana 9-10: Frontend Básico
- [ ] Integrar HTML/CSS estático com Django
- [ ] Página de login funcional
- [ ] Dashboard com estatísticas
- [ ] Listagem de tarefas
- **Entrega**: Frontend conectado ao backend

#### Semana 11-12: Fluxo Principal
- [ ] Criar tarefa (formulário → backend)
- [ ] Atribuir tarefa (dropdown de profissionais)
- [ ] Visualizar detalhes da tarefa
- [ ] Testes de integração
- **Entrega**: Fluxo principal funcionando

---

### **MAIO (Semanas 13-16): Conclusão de Tarefas + Chat**

#### Semana 13-14: Conclusão de Tarefas
- [ ] Endpoint: Completar tarefa
- [ ] Upload de foto (image_after)
- [ ] Notas de conclusão
- [ ] Frontend para conclusão
- [ ] Validações
- **Entrega**: Profissional consegue completar tarefa com foto

#### Semana 15-16: Chat Básico
- [ ] Modelo de mensagens
- [ ] Endpoint: Enviar mensagem
- [ ] Endpoint: Listar mensagens
- [ ] Frontend: Chat simples
- [ ] Validações
- **Entrega**: Chat funcional entre síndico e profissional

---

### **JUNHO (Semanas 17-20): Testes, Documentação e Polimento**

#### Semana 17-18: Testes e Qualidade
- [ ] Testes unitários (70%+ cobertura)
- [ ] Testes de integração
- [ ] Testes de segurança básicos
- [ ] Corrigir bugs encontrados
- **Entrega**: Sistema estável e testado

#### Semana 19-20: Documentação e Apresentação
- [ ] Documentação técnica (README, API docs)
- [ ] Criar slides (14-15 slides)
- [ ] Preparar demo
- [ ] Gravar vídeo de backup
- [ ] Ensaiar apresentação
- **Entrega**: Tudo pronto para apresentar

---

### **JULHO (Semana 21): Apresentação**

- [ ] Apresentação final (15 minutos)
- [ ] Demo ao vivo
- [ ] Responder perguntas da banca
- [ ] Entregar código e documentação

---

## 4. Priorização: O Que Focar

### 4.1 Top 5 Funcionalidades para Impressionar

#### 1️⃣ **Autenticação com 3 Roles Diferentes** (Semana 5-6)
**Por quê**: Mostra que você entende arquitetura de sistemas  
**Impacto**: Alto - Banca vê que você pensou em permissões  
**Tempo**: 1-2 semanas  

```python
# Roles:
- Síndico (cria propriedades, cria tarefas)
- Gestor (gerencia tarefas de uma propriedade)
- Profissional (recebe tarefas, completa)

# Cada role vê telas diferentes
```

#### 2️⃣ **Fluxo Completo de Tarefa** (Semana 7-14)
**Por quê**: Mostra que você entende o problema real  
**Impacto**: Altíssimo - É o core do sistema  
**Tempo**: 6-8 semanas  

```
Síndico cria → Gestor atribui → Profissional executa → Síndico valida
```

#### 3️⃣ **Upload de Fotos com Validação** (Semana 13-14)
**Por quê**: Mostra que você sabe lidar com arquivos  
**Impacto**: Alto - É diferencial real do Chaplin  
**Tempo**: 2-3 semanas  

```python
# Validar:
- Tamanho máximo (5MB)
- Formato (JPG, PNG)
- Qualidade mínima
- Armazenar em pasta segura
```

#### 4️⃣ **Dashboard com Estatísticas** (Semana 9-10)
**Por quê**: Mostra que você entende visualização de dados  
**Impacto**: Médio - Deixa a apresentação mais visual  
**Tempo**: 1-2 semanas  

```
- Total de tarefas (aberta, em progresso, concluída)
- Tarefas por prioridade
- Tempo médio de conclusão
- Profissional mais ativo
```

#### 5️⃣ **Chat Simples** (Semana 15-16)
**Por quê**: Mostra que você sabe comunicação em tempo real  
**Impacto**: Médio - Diferencial competitivo  
**Tempo**: 2 semanas  

```
- Mensagens entre síndico e profissional
- Histórico de conversa
- Notificação simples
```

### 4.2 O Que NÃO Fazer (Armadilhas)

❌ **Não tente fazer**: Rating system (muito complexo para TCC)  
❌ **Não tente fazer**: Mapas com Google Maps (precisa de API key, complexo)  
❌ **Não tente fazer**: Pagamentos com Stripe (risco de falhar na demo)  
❌ **Não tente fazer**: App mobile (muito trabalho extra)  
❌ **Não tente fazer**: Sistema de propostas com lances (muito complexo)  

---

## 5. Estrutura Mínima de Código para Impressionar

### 5.1 Backend (Django)

```
chaplin-backend/
├── apps/
│   ├── users/
│   │   ├── models.py (User com 3 roles)
│   │   ├── serializers.py
│   │   ├── views.py (Login, Registro, Perfil)
│   │   └── urls.py
│   ├── tasks/
│   │   ├── models.py (Task, Property)
│   │   ├── serializers.py
│   │   ├── views.py (CRUD completo)
│   │   └── urls.py
│   ├── chat/
│   │   ├── models.py (Message)
│   │   ├── serializers.py
│   │   ├── views.py (Enviar, Listar)
│   │   └── urls.py
│   └── permissions.py (IsTaskOwner, etc)
├── tests/
│   ├── test_auth.py
│   ├── test_tasks.py
│   └── test_chat.py
├── manage.py
├── requirements.txt
└── .env
```

### 5.2 Frontend (HTML/CSS/JS)

```
chaplin-frontend/
├── index.html (Homepage)
├── pages/
│   ├── login.html
│   ├── dashboard.html
│   ├── tarefas.html
│   ├── nova-tarefa.html
│   ├── detalhes-tarefa.html
│   └── chat.html
├── css/
│   └── styles.css
├── js/
│   ├── main.js
│   ├── api.js (Wrapper para chamadas)
│   └── auth.js (Gerenciar token)
└── assets/
    └── images/
```

---

## 6. Checklist de Desenvolvimento

### Fase 1: Setup (Semanas 1-4)
- [ ] Repositório Git criado
- [ ] Documento de requisitos finalizado
- [ ] Diagramas (ER, arquitetura, fluxos)
- [ ] Django configurado
- [ ] Banco de dados criado
- [ ] Docker configurado (opcional)

### Fase 2: Backend Core (Semanas 5-8)
- [ ] User Model com 3 roles
- [ ] Task Model e Property Model
- [ ] JWT Authentication
- [ ] Endpoints de autenticação
- [ ] Endpoints de tarefas (CRUD)
- [ ] Testes de autenticação e tarefas

### Fase 3: Frontend (Semanas 9-12)
- [ ] Login funcional
- [ ] Dashboard com estatísticas
- [ ] Listagem de tarefas
- [ ] Criar tarefa
- [ ] Atribuir tarefa
- [ ] Integração com backend

### Fase 4: Conclusão e Chat (Semanas 13-16)
- [ ] Completar tarefa com foto
- [ ] Chat básico
- [ ] Validações
- [ ] Testes de integração

### Fase 5: Testes e Documentação (Semanas 17-20)
- [ ] Testes unitários (70%+ cobertura)
- [ ] Documentação técnica
- [ ] Slides (14-15 slides)
- [ ] Demo funcional
- [ ] Vídeo de backup
- [ ] Ensaiar apresentação

---

## 7. Métricas de Sucesso para TCC

### O Que a Banca Vai Avaliar

| Critério | Peso | Como Impressionar |
|----------|------|-------------------|
| **Problema Identificado** | 15% | Mostrar dados reais do mercado |
| **Solução Proposta** | 15% | Explicar como resolve o problema |
| **Implementação** | 30% | Código funcional, bem estruturado |
| **Documentação** | 15% | Diagramas, README, API docs |
| **Apresentação** | 15% | Slides profissionais, demo clara |
| **Análise Crítica** | 10% | Limitações, melhorias futuras |

### Dicas para Cada Critério

**Problema Identificado**:
- Entrevistar 3-5 síndicos/gestores reais
- Mostrar dados de mercado (% de hotéis que usam WhatsApp)
- Documentar os problemas específicos

**Solução Proposta**:
- Explicar como o Chaplin resolve cada problema
- Mostrar comparação com soluções existentes (Asana, WhatsApp)
- Detalhar o fluxo de uso

**Implementação**:
- Código limpo, bem comentado
- Testes automatizados
- Estrutura de pastas organizada
- Sem hardcodes, sem senhas no código

**Documentação**:
- README com instruções de setup
- Diagrama ER do banco
- Diagrama de arquitetura
- Documentação de API (Swagger)

**Apresentação**:
- Slides com visual profissional
- Demo ao vivo (com vídeo de backup)
- Falar com clareza, sem ler slides
- Responder perguntas com segurança

**Análise Crítica**:
- Listar limitações do sistema
- Sugerir melhorias futuras
- Discutir trade-offs de design
- Ser honesto sobre o que não fez

---

## 8. Exemplo de Apresentação (15 minutos)

### Slide 1-2: Introdução (1 min)
- Título, nomes, instituição
- Tema: Simplificar manutenção em hotéis

### Slide 3-4: Problema (2 min)
- Desafios atuais (WhatsApp, planilhas, desorganização)
- Impacto (atrasos, retrabalho, insatisfação)
- Dados de mercado

### Slide 5-6: Solução (2 min)
- O que é Chaplin
- Como funciona (fluxo principal)
- Diferenciais (intuitividade, rastreabilidade)

### Slide 7-9: Arquitetura (2 min)
- Diagrama de arquitetura
- Tecnologias usadas
- Estrutura de banco de dados

### Slide 10-12: Funcionalidades (3 min)
- Autenticação com 3 roles
- Fluxo de tarefa (criar → atribuir → completar)
- Chat integrado

### Slide 13-14: Resultados (2 min)
- Demo ao vivo (ou vídeo)
- Screenshots de funcionalidades
- Estatísticas (linhas de código, testes, etc)

### Slide 15: Conclusão (1 min)
- Resumo
- Limitações
- Trabalhos futuros

### Slide 16: Perguntas
- Aberto para perguntas

---

## 9. Dicas Práticas para Não Falhar

### ✅ Faça

1. **Comece pelo backend** - Frontend é mais fácil depois
2. **Teste constantemente** - Não deixe para o final
3. **Documente enquanto desenvolve** - Não deixe para depois
4. **Faça backup regularmente** - Git + GitHub
5. **Crie um vídeo de backup** - Se a demo falhar
6. **Pratique a apresentação** - Mínimo 5 vezes
7. **Tenha um plano B** - Se algo falhar na demo
8. **Durmam bem antes da apresentação** - Não é brincadeira

### ❌ Não Faça

1. **Não deixe para última hora** - Você terá bugs
2. **Não tente fazer tudo** - Foque no essencial
3. **Não use código copiado sem entender** - Banca vai perguntar
4. **Não esqueça de testes** - Banca vai perguntar sobre cobertura
5. **Não faça apresentação muito longa** - 15 minutos é pouco
6. **Não fale muito rápido** - Deixe claro
7. **Não use muitos efeitos nos slides** - Profissional, não colorido
8. **Não confie 100% na demo ao vivo** - Tenha vídeo de backup

---

## 10. Timeline Semanal Recomendada

### Fevereiro
- **Semana 1**: Finalizar documentação
- **Semana 2**: Criar diagramas
- **Semana 3-4**: Setup Django + Banco

### Março
- **Semana 5-6**: User Model + JWT
- **Semana 7-8**: Task APIs

### Abril
- **Semana 9-10**: Frontend básico
- **Semana 11-12**: Integração frontend-backend

### Maio
- **Semana 13-14**: Upload de fotos
- **Semana 15-16**: Chat

### Junho
- **Semana 17-18**: Testes
- **Semana 19-20**: Documentação + Slides

### Julho
- **Semana 21**: Apresentação

---

## 11. Recursos Necessários

### Tecnologias (Já Decididas)
- ✅ Django 4.2+
- ✅ Django REST Framework
- ✅ MySQL 8.0+
- ✅ HTML/CSS/JavaScript
- ✅ JWT para autenticação

### Ferramentas Recomendadas
- Git + GitHub (versionamento)
- VS Code (editor)
- Postman (testar APIs)
- Draw.io (diagramas)
- Figma (wireframes - opcional)
- OBS Studio (gravar vídeo)

### Serviços (Gratuitos)
- GitHub (repositório)
- Vercel ou Render (deploy - opcional)
- Imgur ou similar (hospedagem de fotos - opcional)

---

## 12. Exemplo de Estrutura de Apresentação Profissional

### Slide Design
- **Cor principal**: Laranja (já definida no Chaplin)
- **Fonte**: Sans-serif (Roboto, Inter)
- **Layout**: 60% conteúdo, 40% espaço em branco
- **Imagens**: Screenshots do sistema funcionando

### Estrutura de Texto
- Máximo 5 linhas por slide
- Títulos claros e diretos
- Usar bullets, não parágrafos
- Números e dados em destaque

---

## 13. Plano B (Se Algo Falhar)

### Se a Demo Falhar
- Tenha um vídeo de 2-3 minutos gravado
- Mostre screenshots das funcionalidades
- Explique o fluxo mesmo sem a demo

### Se Faltar Tempo
- Priorize: Autenticação → Tarefas → Chat
- Se não tiver chat, tudo bem
- Foco em qualidade, não quantidade

### Se a Banca Perguntar Algo Que Não Sabe
- Seja honesto: "Não implementei isso, mas seria..."
- Mostre que pensou sobre o problema
- Sugira como faria no futuro

---

## Conclusão: O Que Realmente Importa

Para uma apresentação de TCC em julho, você precisa de:

1. **Um problema bem definido** ✅ (Você já tem)
2. **Uma solução viável** ✅ (Você já tem)
3. **Implementação funcional** ⏳ (Próximas 5 meses)
4. **Documentação clara** ⏳ (Junho)
5. **Apresentação profissional** ⏳ (Junho-Julho)

**Não precisa de**: Rating, mapas complexos, pagamentos, app mobile, 10 mil usuários.

**Foco**: Fazer bem feito o essencial. Uma banca de TCC prefere um sistema simples mas bem implementado do que um sistema complexo com bugs.

---

**Você consegue fazer isso em 5 meses? SIM!** 💪

Comece agora com o setup técnico. Boa sorte!

