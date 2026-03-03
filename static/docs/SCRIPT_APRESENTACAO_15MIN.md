# Script de Apresentação - Chaplin (15 minutos)

## ⏱️ Timing Total: 15 minutos

---

## 📌 SLIDE 1: Capa (30 segundos)

**O que falar:**
"Bom dia/tarde, meu nome é [seu nome]. Vou apresentar o Chaplin, uma plataforma de marketplace de serviços de manutenção residencial, predial e hoteleira. Essa apresentação vai durar 15 minutos."

**Dica:** Sorria, faça contato visual, fale com clareza.

---

## 📌 SLIDE 2: Problemática (1 minuto)

**O que falar:**
"Hoje, quando você precisa de um serviço de manutenção, você enfrenta vários problemas: 
- Não sabe onde encontrar profissionais confiáveis
- Não consegue comparar preços facilmente
- Não tem garantia de qualidade do trabalho
- O pagamento é inseguro

Isso afeta tanto clientes quanto profissionais. Os clientes ficam inseguros, e os profissionais perdem oportunidades de trabalho. O mercado de manutenção no Brasil movimenta mais de R$ 50 bilhões por ano, mas 70% das buscas ainda são feitas manualmente."

**Dica:** Pause após cada problema para deixar a mensagem passar.

---

## 📌 SLIDE 3: Objetivos (30 segundos)

**O que falar:**
"O Chaplin foi criado com três objetivos principais:
1. Conectar clientes com profissionais verificados
2. Criar um marketplace seguro e confiável
3. Gerar um modelo de negócio sustentável

Vamos resolver esses problemas com tecnologia."

---

## 📌 SLIDE 4: Justificativa (1 minuto)

**O que falar:**
"Por que o Chaplin faz sentido? Existem três razões principais:

Primeiro, a **oportunidade de mercado**: Plataformas de serviços como Uber, 99 e iFood cresceram exponencialmente. Manutenção é o próximo mercado a ser transformado digitalmente.

Segundo, os **benefícios para clientes**: Acesso a profissionais verificados, comparação de preços, comunicação segura, pagamento protegido.

Terceiro, os **benefícios para profissionais**: Acesso a oportunidades de trabalho, construção de reputação, recebimento seguro.

E para a plataforma, temos um modelo de negócio sustentável com comissão de 10% por transação."

**Dica:** Fale com entusiasmo. Esse é o 'pitch' do projeto.

---

## 📌 SLIDE 5: Diagrama de Caso de Uso (1 minuto)

**O que falar:**
"Aqui vemos os quatro atores principais do sistema:

O **Cliente** publica tarefas e aceita propostas.
O **Profissional** visualiza tarefas e faz propostas.
O **Admin** gerencia a plataforma e resolve disputas.
O **Sistema** processa todas as operações automaticamente.

Os casos de uso principais são: autenticação, publicação de tarefas, fazer propostas, chat em tempo real, processamento de pagamentos e avaliações. Todos esses elementos trabalham juntos para criar uma experiência segura e eficiente."

**Dica:** Aponte para cada ator enquanto fala sobre ele.

---

## 📌 SLIDE 6: Fluxo - Publicar Tarefa (1 minuto)

**O que falar:**
"Vamos entender como funciona na prática. Quando um cliente quer publicar uma tarefa:

1. Ele faz login no sistema
2. Clica em 'Nova Tarefa'
3. Preenche um formulário com título, descrição, categoria, orçamento, data, localização e fotos
4. O sistema valida se todos os campos obrigatórios foram preenchidos
5. A tarefa é publicada como 'ABERTA'
6. O sistema notifica profissionais relevantes

Tudo isso leva entre 3 a 5 minutos. Depois disso, a tarefa fica visível para todos os profissionais da plataforma."

**Dica:** Fale como se estivesse contando uma história. Use verbos de ação (clica, preenche, publica).

---

## 📌 SLIDE 7: Fluxo - Fazer Proposta (1 minuto)

**O que falar:**
"Agora, do lado do profissional:

1. Ele visualiza a lista de tarefas abertas
2. Seleciona uma tarefa interessante
3. Preenche uma proposta com valor, descrição da solução e tempo estimado
4. O sistema verifica se ele já fez proposta para essa tarefa (impede duplicatas)
5. Ele confirma e envia a proposta
6. A proposta fica como 'PENDENTE'
7. O cliente é notificado

O profissional pode fazer múltiplas propostas para diferentes tarefas, mas apenas uma por tarefa. Isso garante que o cliente receba propostas de qualidade."

**Dica:** Destaque o ponto 4 (validação de duplicatas) - mostra que o sistema é inteligente.

---

## 📌 SLIDE 8: Fluxo - Pagamento e Conclusão (1 minuto 30 segundos)

**O que falar:**
"Agora vem a parte crítica - o pagamento:

1. O cliente visualiza todas as propostas e escolhe a melhor
2. O sistema rejeita automaticamente as outras propostas
3. Ambos são notificados
4. O cliente clica em 'Pagar Agora' e é redirecionado para o Stripe
5. Ele insere os dados do cartão e confirma
6. O sistema retém o valor: 90% para o profissional, 10% para a plataforma
7. A tarefa muda para 'EM PROGRESSO'
8. O profissional realiza o serviço
9. Quando termina, marca como concluído
10. O cliente confirma a conclusão
11. O pagamento é liberado

Ambos podem se avaliar mutuamente ao final. Isso cria um sistema de reputação confiável."

**Dica:** Enfatize o ponto 4-5 (Stripe) - mostra segurança. Pause antes de falar sobre avaliações.

---

## 📌 SLIDE 9: Requisitos Funcionais - Parte 1 (1 minuto)

**O que falar (RESUMIDO - não leia tudo!):**

"Agora vamos aos requisitos funcionais. Dividimos em dois grupos.

Na **Parte 1**, temos 4 módulos principais:

**Autenticação**: Cadastro de usuários, validação de email, login com JWT, recuperação de senha. Isso garante que apenas usuários legítimos acessem o sistema.

**Perfil**: Cada usuário tem um perfil com dados pessoais, foto, histórico de serviços, rating e avaliações. Profissionais também listam suas especialidades.

**Publicação de Tarefas**: Clientes criam tarefas com título, descrição, fotos, orçamento e prazo. O sistema valida tudo antes de publicar.

**Busca e Filtragem**: Profissionais conseguem filtrar tarefas por categoria, localização, orçamento e ordenar por critérios relevantes.

Esses 4 módulos formam a base do sistema."

**Dica:** Não leia cada requisito individualmente. Resuma em 1-2 frases por módulo. Fale rápido.

---

## 📌 SLIDE 10: Requisitos Funcionais - Parte 2 (1 minuto)

**O que falar (RESUMIDO):**

"Na **Parte 2**, temos os módulos avançados:

**Sistema de Propostas**: Profissionais fazem propostas com valor, descrição e tempo estimado. O sistema impede propostas duplicadas e notifica o cliente.

**Chat em Tempo Real**: Clientes e profissionais se comunicam através de um chat integrado com histórico, notificações e possibilidade de enviar fotos.

**Pagamentos**: Integração com Stripe para processamento seguro. O sistema retém o valor, calcula a comissão e transfere para o profissional.

**Avaliações**: Após conclusão, ambos podem avaliar com estrelas e comentários. Isso cria um sistema de reputação transparente.

Esses 4 módulos transformam o Chaplin em uma plataforma completa de marketplace."

**Dica:** Enfatize "Chat em Tempo Real" e "Pagamentos" - são os diferenciais.

---

## 📌 SLIDE 11: Requisitos Não-Funcionais (1 minuto)

**O que falar (MUITO RESUMIDO):**

"Além dos requisitos funcionais, temos requisitos não-funcionais que garantem qualidade:

**Performance**: Respostas rápidas (menos de 200ms), páginas carregam em menos de 3 segundos, uptime de 99.5%.

**Segurança**: Criptografia de senhas, HTTPS, proteção contra ataques, conformidade com LGPD. Seus dados estão seguros.

**Escalabilidade**: O sistema pode crescer horizontalmente. Se tivermos 10 vezes mais usuários, o sistema continua funcionando.

**Confiabilidade**: Backups automáticos, failover automático, monitoramento 24/7, testes automatizados.

Isso significa que o Chaplin é uma plataforma **segura, rápida e confiável**."

**Dica:** Fale muito rápido aqui. O público não precisa entender cada detalhe técnico. O importante é passar a mensagem de "qualidade e segurança".

---

## 📌 SLIDE 12: Arquitetura Técnica (1 minuto)

**O que falar:**

"Tecnicamente, o Chaplin é construído com:

**Frontend**: React com TypeScript, Tailwind CSS para estilos, Vite para build rápido.

**Backend**: Node.js com Express, tRPC para APIs type-safe, Drizzle ORM para banco de dados.

**Banco de Dados**: MySQL para dados principais, Redis para cache e sessões.

**Integrações**: Stripe para pagamentos, SendGrid para emails, AWS S3 para imagens, Docker para containerização.

Essa stack é moderna, escalável e usada por empresas grandes. Garante que o Chaplin seja mantível e expansível no futuro."

**Dica:** Não entre em detalhes técnicos. Apenas mostre que é uma stack profissional.

---

## 📌 SLIDE 13: Cronograma (1 minuto)

**O que falar:**

"O desenvolvimento está planejado para 6-8 semanas:

**Semana 1**: Setup do ambiente (Docker, repositório, estrutura)
**Semanas 2-3**: Backend core (autenticação, banco de dados, APIs)
**Semana 4**: Frontend core (páginas principais, integração)
**Semana 5**: Features avançadas (chat, propostas, Stripe)
**Semana 6**: Testes e otimizações
**Semanas 7-8**: Deploy em produção e monitoramento

Temos 4 milestones principais que garantem que o projeto está no caminho certo.

A equipe estimada é de 2-3 desenvolvedores usando metodologia Agile."

**Dica:** Mostre confiança no cronograma. Fale com segurança.

---

## 📌 SLIDE 14: Conclusão (1 minuto)

**O que falar:**

"Para resumir:

O **Chaplin** é uma plataforma de marketplace que conecta clientes com profissionais de manutenção de forma segura e eficiente.

Nossos **diferenciais** são: verificação rigorosa de profissionais, avaliações transparentes, chat integrado e pagamento seguro.

O **impacto esperado** é alcançar 1.000+ usuários no primeiro ano, gerar R$ 500k em receita, e atingir 95% de satisfação do cliente.

Os **próximos passos** são: finalizar o MVP em 6-8 semanas, fazer testes com usuários beta, e lançar oficialmente.

O Chaplin vai **transformar o mercado de manutenção residencial, predial e hoteleira**."

**Dica:** Termine com confiança e energia. Deixe espaço para perguntas.

---

## 🎯 RESUMO DE TIMING

| Slide | Conteúdo | Tempo |
|-------|----------|-------|
| 1 | Capa | 0:30 |
| 2 | Problemática | 1:00 |
| 3 | Objetivos | 0:30 |
| 4 | Justificativa | 1:00 |
| 5 | Caso de Uso | 1:00 |
| 6 | Fluxo Tarefa | 1:00 |
| 7 | Fluxo Proposta | 1:00 |
| 8 | Fluxo Pagamento | 1:30 |
| 9 | Req. Func. 1 | 1:00 |
| 10 | Req. Func. 2 | 1:00 |
| 11 | Req. Não-Func. | 1:00 |
| 12 | Arquitetura | 1:00 |
| 13 | Cronograma | 1:00 |
| 14 | Conclusão | 1:00 |
| **TOTAL** | | **15:00** |

---

## 💡 DICAS GERAIS DE APRESENTAÇÃO

### Estrutura da Fala
1. **Introdução** (Slides 1-3): Contexto e problema
2. **Solução** (Slides 4-8): Como o Chaplin resolve
3. **Detalhes Técnicos** (Slides 9-12): Requisitos e arquitetura
4. **Plano** (Slides 13-14): Cronograma e conclusão

### Linguagem
- ✅ Use linguagem simples e clara
- ✅ Evite jargão técnico desnecessário
- ✅ Fale como se estivesse contando uma história
- ✅ Use exemplos do dia a dia

### Pacing
- ✅ Fale com ritmo constante (não muito rápido, não muito lento)
- ✅ Faça pausas entre ideias principais
- ✅ Deixe tempo para o público processar informações

### Contato Visual
- ✅ Olhe para a banca, não para o slide
- ✅ Faça contato visual com diferentes pessoas
- ✅ Use gestos naturais para enfatizar pontos

### Nervosismo
- ✅ Respire fundo antes de começar
- ✅ Pratique em voz alta pelo menos 3 vezes
- ✅ Lembre-se: você é o especialista no Chaplin

### Perguntas
- ✅ Escute a pergunta completamente
- ✅ Responda com confiança
- ✅ Se não souber, diga "ótima pergunta, vou verificar"

---

## 📝 CHECKLIST PRÉ-APRESENTAÇÃO

- [ ] Testei a apresentação em voz alta
- [ ] Cronometrei e ficou dentro de 15 minutos
- [ ] Verifiquei a qualidade do áudio/vídeo
- [ ] Preparei respostas para perguntas comuns
- [ ] Vesti-me apropriadamente
- [ ] Cheguei 15 minutos antes
- [ ] Fiz contato visual com a banca
- [ ] Respirei fundo antes de começar

---

## ❓ PERGUNTAS COMUNS E RESPOSTAS

**P: Por que 10% de comissão?**
R: "É uma taxa competitiva no mercado de marketplaces. Uber cobra 25%, iFood cobra 30%. 10% é justo para o cliente e sustentável para a plataforma."

**P: Como vocês vão garantir a qualidade dos profissionais?**
R: "Temos um sistema de verificação rigoroso: validação de documentos, certificações, histórico de trabalho. Além disso, o sistema de avaliações mantém profissionais ruins fora da plataforma."

**P: Qual é o diferencial do Chaplin?**
R: "Nossos diferenciais são: verificação rigorosa, chat integrado, pagamento seguro com proteção ao cliente, e foco específico em manutenção (não é genérico como TaskRabbit)."

**P: Qual é o público-alvo?**
R: "Clientes: proprietários de imóveis residenciais, síndicos de prédios, gerentes de hotéis. Profissionais: encanadores, eletricistas, pintores, etc."

**P: Qual é o modelo de receita?**
R: "Comissão de 10% por transação. Também temos planos premium para profissionais (destaque, anúncios) e possibilidade de seguro de qualidade."

---

Boa sorte na apresentação! 🚀
