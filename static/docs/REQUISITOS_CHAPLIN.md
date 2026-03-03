# 📋 Requisitos Funcionais e Não-Funcionais - Chaplin

## 🎯 Visão Geral

**Chaplin** é uma plataforma de marketplace de serviços de manutenção que conecta clientes (que precisam de serviços) com profissionais qualificados (que oferecem serviços) em residências, prédios e hotéis.

---

## ✅ REQUISITOS FUNCIONAIS (RF)

### **RF1: Autenticação e Cadastro**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF1.1 | O sistema deve permitir cadastro de usuários (cliente ou profissional) | Usuário | ALTA |
| RF1.2 | O sistema deve validar email único no cadastro | Sistema | ALTA |
| RF1.3 | O sistema deve permitir login com email e senha | Usuário | ALTA |
| RF1.4 | O sistema deve gerar token JWT para manter sessão | Sistema | ALTA |
| RF1.5 | O sistema deve permitir recuperação de senha por email | Usuário | MÉDIA |
| RF1.6 | O sistema deve permitir logout | Usuário | ALTA |
| RF1.7 | O sistema deve verificar se profissional é válido (documento, referências) | Admin | MÉDIA |

---

### **RF2: Gerenciamento de Perfil**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF2.1 | O sistema deve permitir editar dados pessoais | Usuário | ALTA |
| RF2.2 | O sistema deve permitir upload de foto de perfil | Usuário | MÉDIA |
| RF2.3 | O sistema deve exibir histórico de serviços do profissional | Cliente | ALTA |
| RF2.4 | O sistema deve exibir rating e avaliações do profissional | Cliente | ALTA |
| RF2.5 | O sistema deve permitir visualizar especialidades do profissional | Cliente | ALTA |
| RF2.6 | O sistema deve permitir profissional adicionar certificações | Profissional | MÉDIA |
| RF2.7 | O sistema deve exibir localização/cobertura do profissional | Cliente | ALTA |

---

### **RF3: Publicação de Tarefas (Clientes)**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF3.1 | O sistema deve permitir cliente criar nova tarefa | Cliente | ALTA |
| RF3.2 | O sistema deve permitir selecionar categoria de serviço | Cliente | ALTA |
| RF3.3 | O sistema deve permitir descrever detalhes da tarefa | Cliente | ALTA |
| RF3.4 | O sistema deve permitir upload de fotos da tarefa | Cliente | MÉDIA |
| RF3.5 | O sistema deve permitir definir orçamento mínimo e máximo | Cliente | ALTA |
| RF3.6 | O sistema deve permitir definir data de vencimento | Cliente | ALTA |
| RF3.7 | O sistema deve permitir definir nível de prioridade | Cliente | ALTA |
| RF3.8 | O sistema deve permitir definir localização do serviço | Cliente | ALTA |
| RF3.9 | O sistema deve validar todos os campos obrigatórios | Sistema | ALTA |
| RF3.10 | O sistema deve notificar profissionais relevantes quando tarefa é publicada | Sistema | ALTA |
| RF3.11 | O sistema deve permitir cliente editar tarefa em aberta | Cliente | MÉDIA |
| RF3.12 | O sistema deve permitir cliente cancelar tarefa em aberta | Cliente | MÉDIA |

---

### **RF4: Busca e Filtragem de Tarefas (Profissionais)**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF4.1 | O sistema deve listar tarefas abertas | Profissional | ALTA |
| RF4.2 | O sistema deve permitir filtrar por categoria | Profissional | ALTA |
| RF4.3 | O sistema deve permitir filtrar por localização/cidade | Profissional | ALTA |
| RF4.4 | O sistema deve permitir filtrar por faixa de orçamento | Profissional | ALTA |
| RF4.5 | O sistema deve permitir filtrar por prioridade | Profissional | MÉDIA |
| RF4.6 | O sistema deve permitir ordenar por data, preço, urgência | Profissional | MÉDIA |
| RF4.7 | O sistema deve exibir detalhes completos da tarefa | Profissional | ALTA |
| RF4.8 | O sistema deve exibir rating do cliente | Profissional | ALTA |
| RF4.9 | O sistema deve exibir número de propostas já recebidas | Profissional | MÉDIA |

---

### **RF5: Sistema de Propostas (Bids)**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF5.1 | O sistema deve permitir profissional fazer proposta | Profissional | ALTA |
| RF5.2 | O sistema deve permitir definir valor da proposta | Profissional | ALTA |
| RF5.3 | O sistema deve permitir descrever como será feito o serviço | Profissional | ALTA |
| RF5.4 | O sistema deve permitir definir tempo estimado | Profissional | ALTA |
| RF5.5 | O sistema deve impedir profissional fazer 2 propostas na mesma tarefa | Sistema | ALTA |
| RF5.6 | O sistema deve notificar cliente quando recebe proposta | Sistema | ALTA |
| RF5.7 | O sistema deve permitir cliente visualizar todas as propostas | Cliente | ALTA |
| RF5.8 | O sistema deve permitir cliente aceitar proposta | Cliente | ALTA |
| RF5.9 | O sistema deve permitir cliente rejeitar proposta | Cliente | ALTA |
| RF5.10 | O sistema deve atualizar status da tarefa para "em progresso" quando aceita proposta | Sistema | ALTA |
| RF5.11 | O sistema deve rejeitar automaticamente outras propostas quando cliente aceita uma | Sistema | ALTA |

---

### **RF6: Chat em Tempo Real**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF6.1 | O sistema deve permitir chat entre cliente e profissional | Usuário | ALTA |
| RF6.2 | O sistema deve exibir histórico de mensagens | Usuário | ALTA |
| RF6.3 | O sistema deve marcar mensagens como lidas | Sistema | ALTA |
| RF6.4 | O sistema deve notificar quando recebe mensagem | Sistema | ALTA |
| RF6.5 | O sistema deve permitir enviar fotos no chat | Usuário | MÉDIA |
| RF6.6 | O sistema deve exibir timestamp de cada mensagem | Sistema | ALTA |
| RF6.7 | O sistema deve exibir status "digitando..." em tempo real | Sistema | MÉDIA |
| RF6.8 | O sistema deve permitir deletar mensagem própria | Usuário | BAIXA |

---

### **RF7: Pagamentos**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF7.1 | O sistema deve integrar com Stripe para pagamentos | Sistema | ALTA |
| RF7.2 | O sistema deve permitir cliente pagar pelo serviço | Cliente | ALTA |
| RF7.3 | O sistema deve reter valor até conclusão do serviço | Sistema | ALTA |
| RF7.4 | O sistema deve calcular comissão da plataforma (10%) | Sistema | ALTA |
| RF7.5 | O sistema deve transferir valor para profissional após conclusão | Sistema | ALTA |
| RF7.6 | O sistema deve permitir cliente solicitar reembolso | Cliente | MÉDIA |
| RF7.7 | O sistema deve exibir histórico de pagamentos | Usuário | ALTA |
| RF7.8 | O sistema deve gerar recibos de pagamento | Sistema | MÉDIA |
| RF7.9 | O sistema deve suportar múltiplos métodos (cartão, PIX, boleto) | Sistema | MÉDIA |

---

### **RF8: Avaliações e Ratings**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF8.1 | O sistema deve permitir cliente avaliar profissional após conclusão | Cliente | ALTA |
| RF8.2 | O sistema deve permitir profissional avaliar cliente | Profissional | ALTA |
| RF8.3 | O sistema deve permitir nota de 1 a 5 estrelas | Usuário | ALTA |
| RF8.4 | O sistema deve permitir comentário na avaliação | Usuário | ALTA |
| RF8.5 | O sistema deve calcular rating médio do profissional | Sistema | ALTA |
| RF8.6 | O sistema deve exibir avaliações públicas no perfil | Usuário | ALTA |
| RF8.7 | O sistema deve impedir avaliação duplicada | Sistema | ALTA |
| RF8.8 | O sistema deve permitir responder avaliação | Profissional | MÉDIA |

---

### **RF9: Notificações**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF9.1 | O sistema deve enviar email quando tarefa é publicada (para profissionais relevantes) | Sistema | ALTA |
| RF9.2 | O sistema deve enviar notificação quando recebe proposta | Sistema | ALTA |
| RF9.3 | O sistema deve enviar notificação quando proposta é aceita | Sistema | ALTA |
| RF9.4 | O sistema deve enviar notificação quando recebe mensagem | Sistema | ALTA |
| RF9.5 | O sistema deve enviar SMS para alertas críticos | Sistema | MÉDIA |
| RF9.6 | O sistema deve permitir usuário configurar preferências de notificação | Usuário | MÉDIA |
| RF9.7 | O sistema deve exibir notificações em tempo real no app | Sistema | ALTA |

---

### **RF10: Gerenciamento de Tarefas (Status)**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF10.1 | O sistema deve permitir profissional marcar tarefa como iniciada | Profissional | ALTA |
| RF10.2 | O sistema deve permitir profissional marcar tarefa como concluída | Profissional | ALTA |
| RF10.3 | O sistema deve permitir cliente confirmar conclusão | Cliente | ALTA |
| RF10.4 | O sistema deve permitir cliente solicitar revisão se não satisfeito | Cliente | MÉDIA |
| RF10.5 | O sistema deve exibir timeline da tarefa | Usuário | MÉDIA |
| RF10.6 | O sistema deve permitir cliente cancelar tarefa com justificativa | Cliente | MÉDIA |
| RF10.7 | O sistema deve liberar pagamento após confirmação de conclusão | Sistema | ALTA |

---

### **RF11: Dashboard e Relatórios**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF11.1 | O sistema deve exibir dashboard com estatísticas para cliente | Cliente | ALTA |
| RF11.2 | O sistema deve exibir dashboard com estatísticas para profissional | Profissional | ALTA |
| RF11.3 | O sistema deve exibir número de tarefas abertas/em progresso/concluídas | Usuário | ALTA |
| RF11.4 | O sistema deve exibir ganhos totais do profissional | Profissional | ALTA |
| RF11.5 | O sistema deve exibir gastos totais do cliente | Cliente | ALTA |
| RF11.6 | O sistema deve exibir gráficos de atividade | Usuário | MÉDIA |
| RF11.7 | O sistema deve permitir exportar relatório em PDF | Usuário | BAIXA |

---

### **RF12: Administração**

| ID | Descrição | Ator | Prioridade |
|----|-----------|------|-----------|
| RF12.1 | O sistema deve permitir admin visualizar todas as tarefas | Admin | ALTA |
| RF12.2 | O sistema deve permitir admin visualizar todos os usuários | Admin | ALTA |
| RF12.3 | O sistema deve permitir admin verificar profissional | Admin | ALTA |
| RF12.4 | O sistema deve permitir admin bloquear usuário | Admin | ALTA |
| RF12.5 | O sistema deve permitir admin resolver disputas | Admin | ALTA |
| RF12.6 | O sistema deve permitir admin visualizar relatórios financeiros | Admin | ALTA |
| RF12.7 | O sistema deve permitir admin gerenciar categorias de serviço | Admin | MÉDIA |

---

## ⚙️ REQUISITOS NÃO-FUNCIONAIS (RNF)

### **RNF1: Performance**

| ID | Descrição | Métrica | Prioridade |
|----|-----------|---------|-----------|
| RNF1.1 | Tempo de resposta da API | < 200ms (p95) | ALTA |
| RNF1.2 | Tempo de carregamento da página | < 3s (first contentful paint) | ALTA |
| RNF1.3 | Taxa de erro da API | < 0.1% | ALTA |
| RNF1.4 | Disponibilidade do sistema | 99.5% uptime | ALTA |
| RNF1.5 | Capacidade de suportar picos de tráfego | 10x tráfego normal | ALTA |
| RNF1.6 | Tempo de resposta do chat | < 100ms | ALTA |

---

### **RNF2: Segurança**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF2.1 | Autenticação segura | JWT com expiração 24h | ALTA |
| RNF2.2 | Criptografia de senhas | bcryptjs com salt 10 | ALTA |
| RNF2.3 | Comunicação criptografada | HTTPS/TLS 1.3 | ALTA |
| RNF2.2 | Proteção contra SQL Injection | ORM (Drizzle) + Parameterized queries | ALTA |
| RNF2.5 | Proteção contra XSS | React (sanitização automática) + CSP | ALTA |
| RNF2.6 | Proteção contra CSRF | CSRF tokens | ALTA |
| RNF2.7 | Rate limiting | 100 requisições/minuto por IP | ALTA |
| RNF2.8 | Validação de entrada | Zod schema validation | ALTA |
| RNF2.9 | Dados sensíveis criptografados | Documentos, fotos de perfil | ALTA |
| RNF2.10 | Conformidade LGPD | Direito ao esquecimento, consentimento | ALTA |
| RNF2.11 | Auditoria de ações | Log de todas as transações | MÉDIA |

---

### **RNF3: Escalabilidade**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF3.1 | Arquitetura horizontal | Load balancing com Nginx | ALTA |
| RNF3.2 | Cache distribuído | Redis para sessões e cache | ALTA |
| RNF3.3 | Banco de dados escalável | MySQL com replicação | ALTA |
| RNF3.4 | Fila de jobs | Bull/BullMQ para tasks assíncronas | MÉDIA |
| RNF3.5 | CDN para assets | Cloudflare para imagens/CSS/JS | ALTA |
| RNF3.6 | Microserviços preparados | Arquitetura modular | MÉDIA |

---

### **RNF4: Confiabilidade**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF4.1 | Backup automático | Backup diário do banco de dados | ALTA |
| RNF4.2 | Recuperação de falhas | Failover automático | ALTA |
| RNF4.3 | Monitoramento 24/7 | Sentry, DataDog, PagerDuty | ALTA |
| RNF4.4 | Alertas de erro | Notificação em tempo real | ALTA |
| RNF4.5 | Logs estruturados | ELK Stack (Elasticsearch, Logstash, Kibana) | MÉDIA |
| RNF4.6 | Testes automatizados | 80% cobertura de testes | ALTA |
| RNF4.7 | Testes E2E | Cypress/Playwright | MÉDIA |

---

### **RNF5: Usabilidade**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF5.1 | Interface responsiva | Mobile-first, breakpoints otimizados | ALTA |
| RNF5.2 | Acessibilidade | WCAG 2.1 AA compliance | ALTA |
| RNF5.3 | Tempo de aprendizado | Interface intuitiva, onboarding | ALTA |
| RNF5.4 | Suporte a múltiplos idiomas | i18n (português, inglês, espanhol) | MÉDIA |
| RNF5.5 | Modo escuro | Dark mode opcional | BAIXA |
| RNF5.6 | Offline support | Service workers para funcionalidades básicas | BAIXA |

---

### **RNF6: Manutenibilidade**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF6.1 | Código limpo | ESLint, Prettier, SonarQube | ALTA |
| RNF6.2 | Documentação | JSDoc, README, API docs | ALTA |
| RNF6.3 | Versionamento | Git com conventional commits | ALTA |
| RNF6.4 | CI/CD | GitHub Actions com testes automáticos | ALTA |
| RNF6.5 | Arquitetura modular | Separação clara de responsabilidades | ALTA |
| RNF6.6 | Padrões de design | Factory, Observer, Strategy | MÉDIA |

---

### **RNF7: Compatibilidade**

| ID | Descrição | Suporte | Prioridade |
|----|-----------|---------|-----------|
| RNF7.1 | Navegadores | Chrome, Firefox, Safari, Edge (últimas 2 versões) | ALTA |
| RNF7.2 | Sistemas operacionais | Windows, macOS, Linux | ALTA |
| RNF7.3 | Dispositivos móveis | iOS 12+, Android 8+ | ALTA |
| RNF7.4 | Conexões de rede | Suporta 3G/4G/5G/WiFi | ALTA |
| RNF7.5 | Resolução de tela | 320px até 4K | ALTA |

---

### **RNF8: Compliance e Regulamentação**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF8.1 | LGPD | Consentimento, direito ao esquecimento | ALTA |
| RNF8.2 | Termos de Serviço | Aceitar antes de usar | ALTA |
| RNF8.3 | Política de Privacidade | Transparência de dados | ALTA |
| RNF8.4 | Proteção ao Consumidor | Garantia de qualidade, reembolso | ALTA |
| RNF8.5 | Impostos | Cálculo automático de impostos | MÉDIA |

---

### **RNF9: Interoperabilidade**

| ID | Descrição | Implementação | Prioridade |
|----|-----------|----------------|-----------|
| RNF9.1 | API RESTful | Documentação com Swagger | MÉDIA |
| RNF9.2 | Webhooks | Para integrações externas | MÉDIA |
| RNF9.3 | OAuth 2.0 | Login com Google, Facebook | MÉDIA |
| RNF9.4 | Integração Stripe | Pagamentos e assinaturas | ALTA |
| RNF9.5 | Integração SendGrid | Envio de emails | ALTA |

---

## 📊 Resumo Executivo

### **Requisitos Funcionais: 87 requisitos**
- Autenticação: 7 RF
- Perfil: 7 RF
- Tarefas: 12 RF
- Busca: 9 RF
- Propostas: 11 RF
- Chat: 8 RF
- Pagamentos: 9 RF
- Avaliações: 8 RF
- Notificações: 7 RF
- Status: 7 RF
- Dashboard: 7 RF
- Admin: 7 RF

### **Requisitos Não-Funcionais: 69 requisitos**
- Performance: 6 RNF
- Segurança: 11 RNF
- Escalabilidade: 6 RNF
- Confiabilidade: 7 RNF
- Usabilidade: 6 RNF
- Manutenibilidade: 6 RNF
- Compatibilidade: 5 RNF
- Compliance: 5 RNF
- Interoperabilidade: 5 RNF

---

## 🎯 Priorização

### **ALTA (MVP - Semana 1-4)**
- Autenticação
- Publicação de tarefas
- Busca e filtragem
- Sistema de propostas
- Chat básico
- Pagamentos

### **MÉDIA (Semana 5-8)**
- Notificações avançadas
- Avaliações
- Dashboard
- Admin básico
- Múltiplos métodos de pagamento

### **BAIXA (Pós-MVP)**
- Modo escuro
- Exportar relatórios
- Offline support
- Múltiplos idiomas

---

**Total de requisitos: 156 (87 funcionais + 69 não-funcionais)**

Quer que eu crie os diagramas de caso de uso e fluxogramas agora?
