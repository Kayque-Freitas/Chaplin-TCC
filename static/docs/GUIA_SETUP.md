# Guia de Configuração - Chaplin

Este guia contém as instruções necessárias para configurar e rodar o projeto Chaplin em um ambiente local.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:
- **Python 3.10+**
- **Git**

O projeto utiliza **SQLite** por padrão, portanto não é necessário configurar um banco de dados externo para o desenvolvimento inicial.

## Configuração Passo a Passo

### 1. Clonar o Repositório
Abra o terminal e execute:
```bash
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC
```

### 2. Criar e Ativar o Ambiente Virtual
É recomendado usar um ambiente virtual para isolar as dependências:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
Com o ambiente virtual ativo, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do projeto com o seguinte conteúdo:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Preparar o Banco de Dados
Execute as migrações para criar as tabelas no SQLite:
```bash
python manage.py migrate
```

### 6. Criar Usuário Administrador
Para acessar o painel de controle e criar outros usuários, crie um superusuário:
```bash
python manage.py createsuperuser
```

### 7. Iniciar o Servidor
```bash
python manage.py runserver
```
O sistema estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Estrutura de Permissões
O Chaplin trabalha com quatro níveis de acesso:
1. **Admin**: Acesso total ao sistema e gestão de contas.
2. **Gestor**: Responsável por abrir ordens de serviço e validar conclusões.
3. **Líder**: Recebe as ordens e as atribui aos colaboradores em campo.
4. **Colaborador**: Executa a tarefa e registra as evidências fotográficas.

## Solução de Problemas Comuns

- **Erro de Módulo não Encontrado**: Verifique se o ambiente virtual (`venv`) está devidamente ativado.
- **Erro de Banco de Dados**: Certifique-se de que executou o comando `python manage.py migrate`.
- **Imagens não aparecem**: Verifique se a pasta `media/` foi criada e se as permissões de escrita estão corretas.

## Configurações para Produção
Embora o SQLite seja ideal para testes, o projeto está preparado para **PostgreSQL**. Para trocar o banco, basta configurar as variáveis `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST` e `DB_PORT` no seu arquivo `.env`.
