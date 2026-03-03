# 🚀 Guia Completo: Setup Django Local para Chaplin TCC

## 📋 Índice
1. [Setup Django Local](#setup-django-local)
2. [Modelos de Dados](#modelos-de-dados)
3. [APIs REST](#apis-rest)
4. [Autenticação com Sessões](#autenticação-com-sessões)
5. [S3 Cloud Storage](#s3-cloud-storage)
6. [Chat com Polling](#chat-com-polling)
7. [Integração Frontend-Backend](#integração-frontend-backend)
8. [Git Workflow](#git-workflow)

---

## 1. Setup Django Local

### 1.1 Pré-requisitos

Você precisa ter instalado:
- **Python 3.10+** (verifique com `python --version`)
- **pip** (gerenciador de pacotes Python)
- **MySQL 8.0+** (banco de dados)
- **Git** (controle de versão)
- **VS Code** (editor)

### 1.2 Instalação Passo-a-Passo

#### Passo 1: Criar Pasta do Projeto

```bash
# Crie uma pasta para o projeto
mkdir chaplin-backend
cd chaplin-backend
```

#### Passo 2: Criar Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# No Windows:
venv\Scripts\activate

# No macOS/Linux:
source venv/bin/activate
```

#### Passo 3: Instalar Dependências

```bash
# Criar arquivo requirements.txt
pip install django==4.2.0
pip install djangorestframework==3.14.0
pip install mysql-connector-python==8.0.33
pip install python-decouple==3.8
pip install django-cors-headers==4.0.0
pip install boto3==1.26.0
pip install pillow==9.5.0
pip install celery==5.2.7
pip install redis==4.5.4
```

Ou crie um arquivo `requirements.txt`:

```txt
Django==4.2.0
djangorestframework==3.14.0
mysql-connector-python==8.0.33
python-decouple==3.8
django-cors-headers==4.0.0
boto3==1.26.0
Pillow==9.5.0
celery==5.2.7
redis==4.5.4
```

E instale tudo de uma vez:

```bash
pip install -r requirements.txt
```

#### Passo 4: Criar Projeto Django

```bash
# Criar projeto Django
django-admin startproject chaplin_project .

# Criar apps
python manage.py startapp users
python manage.py startapp tasks
python manage.py startapp properties
python manage.py startapp messages
```

#### Passo 5: Configurar Banco de Dados (MySQL)

Edite `chaplin_project/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'chaplin_db',
        'USER': 'root',
        'PASSWORD': 'sua_senha_mysql',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Passo 6: Criar Banco de Dados MySQL

```bash
# No terminal MySQL
mysql -u root -p

# Dentro do MySQL:
CREATE DATABASE chaplin_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
```

#### Passo 7: Executar Migrações

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário (admin)
python manage.py createsuperuser
```

#### Passo 8: Testar Servidor

```bash
# Iniciar servidor
python manage.py runserver

# Acesse: http://localhost:8000
# Admin: http://localhost:8000/admin
```

---

## 2. Modelos de Dados

### 2.1 Estrutura de Usuários

Edite `users/models.py`:

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('sindico', 'Síndico'),
        ('gestor', 'Gestor'),
        ('colaborador', 'Colaborador'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='colaborador')
    phone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
```

### 2.2 Estrutura de Propriedades

Edite `properties/models.py`:

```python
from django.db import models
from users.models import User

class Property(models.Model):
    sindico = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    total_rooms = models.IntegerField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.city}/{self.state}"

class Room(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    floor = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('property', 'room_number')
    
    def __str__(self):
        return f"Quarto {self.room_number} - {self.property.name}"
```

### 2.3 Estrutura de Tarefas

Edite `tasks/models.py`:

```python
from django.db import models
from users.models import User
from properties.models import Room

class Task(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_progresso', 'Em Progresso'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]
    
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='tasks')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks_created')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='media')
    
    due_date = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)
    
    evidence_photo = models.ImageField(upload_to='task_evidence/', null=True, blank=True)
    evidence_description = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
```

### 2.4 Estrutura de Mensagens (Chat)

Edite `messages/models.py`:

```python
from django.db import models
from users.models import User
from tasks.models import Task

class Message(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='messages_sent')
    
    content = models.TextField()
    attachment = models.FileField(upload_to='messages/', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"Mensagem de {self.sender.get_full_name()} em {self.task.title}"
```

---

## 3. APIs REST

### 3.1 Serializers

Crie `users/serializers.py`:

```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone', 'profile_picture']
        read_only_fields = ['id']
```

Crie `tasks/serializers.py`:

```python
from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'room', 'created_by', 'assigned_to', 'title', 'description', 
                  'status', 'priority', 'due_date', 'completed_at', 'evidence_photo', 
                  'evidence_description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'completed_at']
```

### 3.2 Views (API Endpoints)

Crie `tasks/views.py`:

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'sindico':
            # Síndico vê todas as tarefas de suas propriedades
            return Task.objects.filter(room__property__sindico=user)
        elif user.role == 'gestor':
            # Gestor vê tarefas de suas propriedades
            return Task.objects.filter(room__property__sindico=user)
        else:
            # Colaborador vê apenas tarefas atribuídas a ele
            return Task.objects.filter(assigned_to=user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'concluida'
        task.completed_at = timezone.now()
        task.evidence_photo = request.FILES.get('evidence_photo')
        task.evidence_description = request.data.get('evidence_description')
        task.save()
        return Response(TaskSerializer(task).data)
    
    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get('user_id')
        task.assigned_to_id = user_id
        task.status = 'em_progresso'
        task.save()
        return Response(TaskSerializer(task).data)
```

### 3.3 URLs

Crie `chaplin_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
```

---

## 4. Autenticação com Sessões

### 4.1 Login View

Crie `users/views.py`:

```python
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return Response({
            'success': True,
            'user': UserSerializer(user).data,
            'message': 'Login realizado com sucesso'
        })
    else:
        return Response({
            'success': False,
            'message': 'Usuário ou senha inválidos'
        }, status=401)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'success': True, 'message': 'Logout realizado'})

@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated:
        return Response(UserSerializer(request.user).data)
    else:
        return Response({'error': 'Não autenticado'}, status=401)
```

### 4.2 URLs de Autenticação

Edite `chaplin_project/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from users.views import login_view, logout_view, current_user

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/login/', login_view, name='login'),
    path('api/auth/logout/', logout_view, name='logout'),
    path('api/auth/me/', current_user, name='current_user'),
    path('api-auth/', include('rest_framework.urls')),
]
```

### 4.3 Configurar Sessões

Edite `chaplin_project/settings.py`:

```python
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 1209600  # 2 semanas
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  # True em produção com HTTPS
CSRF_COOKIE_SECURE = False  # True em produção
```

---

## 5. S3 Cloud Storage

### 5.1 O Que é S3?

**Amazon S3 (Simple Storage Service)** é um serviço de armazenamento em nuvem que permite você guardar arquivos (fotos, documentos, etc.) sem ocupar espaço no seu servidor.

**Vantagens:**
- Escalável (cresce conforme necessário)
- Seguro (criptografia integrada)
- Barato (paga apenas pelo que usa)
- Rápido (distribuído globalmente)

**Desvantagem:**
- Requer conta AWS (Amazon Web Services)

### 5.2 Setup S3

#### Passo 1: Criar Conta AWS

1. Acesse [aws.amazon.com](https://aws.amazon.com)
2. Clique em "Create an AWS Account"
3. Preencha seus dados
4. Ative o acesso programático (Access Keys)

#### Passo 2: Criar Bucket S3

1. Vá para S3 Dashboard
2. Clique em "Create bucket"
3. Nome: `chaplin-tcc-bucket`
4. Região: `sa-east-1` (São Paulo)
5. Clique em "Create"

#### Passo 3: Configurar Django para S3

Instale:

```bash
pip install django-storages
```

Edite `chaplin_project/settings.py`:

```python
# Adicione ao final
USE_S3 = True

if USE_S3:
    # AWS S3 Settings
    AWS_ACCESS_KEY_ID = 'sua_access_key'
    AWS_SECRET_ACCESS_KEY = 'sua_secret_key'
    AWS_STORAGE_BUCKET_NAME = 'chaplin-tcc-bucket'
    AWS_S3_REGION_NAME = 'sa-east-1'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_LOCATION = 'media'
    
    # Static files (CSS, JavaScript, Images)
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/static/'
    STATIC_ROOT = 'static/'
    
    # Media files (User uploads)
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/media/'
    MEDIA_ROOT = 'media/'
    
    # Use S3 for storage
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
else:
    # Local storage (desenvolvimento)
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

#### Passo 4: Usar S3 no Modelo

```python
# Em tasks/models.py
evidence_photo = models.ImageField(
    upload_to='task_evidence/%Y/%m/%d/',
    null=True,
    blank=True,
    storage=default_storage  # Usa S3 automaticamente
)
```

### 5.3 Variáveis de Ambiente

Para não expor suas chaves, use `.env`:

```bash
pip install python-decouple
```

Crie `.env`:

```
AWS_ACCESS_KEY_ID=sua_access_key
AWS_SECRET_ACCESS_KEY=sua_secret_key
USE_S3=True
```

Edite `chaplin_project/settings.py`:

```python
from decouple import config

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
USE_S3 = config('USE_S3', default=False, cast=bool)
```

---

## 6. Chat com Polling

### 6.1 O Que é Polling?

**Polling** é uma técnica onde o cliente (navegador) **pergunta ao servidor** a cada X segundos se há novas mensagens.

**Fluxo:**
```
Cliente                    Servidor
   |                          |
   |--- "Tem mensagens?" ---->|
   |                          |
   |<--- "Sim, aqui estão" ----|
   |                          |
   | (aguarda 3 segundos)     |
   |                          |
   |--- "Tem mensagens?" ---->|
   |                          |
   |<--- "Não" -------|
   |                          |
```

**Vantagens:**
- Simples de implementar
- Funciona em qualquer navegador
- Não precisa de WebSocket

**Desvantagens:**
- Menos eficiente (muitas requisições)
- Latência maior (demora até 3 segundos para chegar)

### 6.2 Implementar Chat com Polling

#### Passo 1: API para Listar Mensagens

Edite `messages/views.py`:

```python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from tasks.models import Task

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        task_id = self.request.query_params.get('task_id')
        if task_id:
            return Message.objects.filter(task_id=task_id).order_by('created_at')
        return Message.objects.none()
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
```

#### Passo 2: Serializer de Mensagens

Crie `messages/serializers.py`:

```python
from rest_framework import serializers
from .models import Message
from users.serializers import UserSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'task', 'sender', 'content', 'attachment', 'created_at']
        read_only_fields = ['id', 'created_at']
```

#### Passo 3: Frontend - Polling de Mensagens

No arquivo `js/chat.js`:

```javascript
// Configuração
const POLL_INTERVAL = 3000; // 3 segundos
let lastMessageId = 0;
let pollingInterval = null;

// Função para buscar mensagens
async function fetchMessages(taskId) {
    try {
        const response = await fetch(`/api/messages/?task_id=${taskId}`);
        const messages = await response.json();
        
        // Mostrar apenas mensagens novas
        messages.forEach(msg => {
            if (msg.id > lastMessageId) {
                displayMessage(msg);
                lastMessageId = msg.id;
            }
        });
    } catch (error) {
        console.error('Erro ao buscar mensagens:', error);
    }
}

// Função para mostrar mensagem na tela
function displayMessage(message) {
    const chatContainer = document.getElementById('chat-messages');
    const messageEl = document.createElement('div');
    messageEl.className = 'message';
    messageEl.innerHTML = `
        <strong>${message.sender.first_name}</strong>
        <p>${message.content}</p>
        <small>${new Date(message.created_at).toLocaleTimeString()}</small>
    `;
    chatContainer.appendChild(messageEl);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Função para enviar mensagem
async function sendMessage(taskId, content) {
    try {
        const response = await fetch('/api/messages/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({
                task: taskId,
                content: content
            })
        });
        
        if (response.ok) {
            document.getElementById('message-input').value = '';
            // Buscar mensagens imediatamente
            fetchMessages(taskId);
        }
    } catch (error) {
        console.error('Erro ao enviar mensagem:', error);
    }
}

// Iniciar polling
function startPolling(taskId) {
    // Buscar mensagens imediatamente
    fetchMessages(taskId);
    
    // Depois, a cada 3 segundos
    pollingInterval = setInterval(() => {
        fetchMessages(taskId);
    }, POLL_INTERVAL);
}

// Parar polling
function stopPolling() {
    if (pollingInterval) {
        clearInterval(pollingInterval);
    }
}

// Helper para pegar CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Event listeners
document.getElementById('send-btn').addEventListener('click', () => {
    const taskId = document.getElementById('task-id').value;
    const content = document.getElementById('message-input').value;
    if (content.trim()) {
        sendMessage(taskId, content);
    }
});

// Iniciar quando página carrega
document.addEventListener('DOMContentLoaded', () => {
    const taskId = document.getElementById('task-id').value;
    startPolling(taskId);
});

// Parar quando página fecha
window.addEventListener('beforeunload', () => {
    stopPolling();
});
```

#### Passo 4: HTML do Chat

```html
<div id="chat-container">
    <input type="hidden" id="task-id" value="{{ task.id }}">
    
    <div id="chat-messages" style="height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; margin-bottom: 10px;">
        <!-- Mensagens aparecem aqui -->
    </div>
    
    <div style="display: flex; gap: 10px;">
        <input 
            type="text" 
            id="message-input" 
            placeholder="Digite sua mensagem..." 
            style="flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px;"
        >
        <button id="send-btn" style="padding: 10px 20px; background-color: #f97316; color: white; border: none; border-radius: 5px; cursor: pointer;">
            Enviar
        </button>
    </div>
</div>

<script src="/js/chat.js"></script>
```

---

## 7. Integração Frontend-Backend

### 7.1 Remover Validação Local

No `js/main.js`, remova `e.preventDefault()`:

```javascript
// ANTES (bloqueia envio)
form.addEventListener('submit', (e) => {
    e.preventDefault();
    showNotification('Demo', 'success');
});

// DEPOIS (permite envio para backend)
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    
    try {
        const response = await fetch('/api/tasks/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: formData
        });
        
        if (response.ok) {
            showNotification('Tarefa criada com sucesso!', 'success');
            form.reset();
        } else {
            showNotification('Erro ao criar tarefa', 'error');
        }
    } catch (error) {
        console.error('Erro:', error);
        showNotification('Erro de conexão', 'error');
    }
});
```

### 7.2 Carregar Dados Dinamicamente

```javascript
// Carregar tarefas do backend
async function loadTasks() {
    try {
        const response = await fetch('/api/tasks/');
        const tasks = await response.json();
        
        const taskList = document.getElementById('tasks-list');
        taskList.innerHTML = '';
        
        tasks.forEach(task => {
            const taskEl = document.createElement('div');
            taskEl.className = 'task-card';
            taskEl.innerHTML = `
                <h3>${task.title}</h3>
                <p>${task.description}</p>
                <span class="status">${task.status}</span>
                <span class="priority">${task.priority}</span>
            `;
            taskList.appendChild(taskEl);
        });
    } catch (error) {
        console.error('Erro ao carregar tarefas:', error);
    }
}

// Chamar ao carregar página
document.addEventListener('DOMContentLoaded', loadTasks);
```

---

## 8. Git Workflow

### 8.1 Inicializar Repositório

```bash
# Clonar repositório
git clone https://github.com/Kayque-Freitas/Chaplin-TCC.git
cd Chaplin-TCC

# Criar branch para backend
git checkout -b feature/django-backend

# Ou criar nova branch
git branch feature/django-backend
git checkout feature/django-backend
```

### 8.2 Estrutura de Commits

```bash
# Adicionar arquivos
git add .

# Commit com mensagem descritiva
git commit -m "feat: adicionar modelos de usuário e tarefas"

# Tipos de commit:
# feat: nova funcionalidade
# fix: correção de bug
# docs: documentação
# style: formatação
# refactor: refatoração
# test: testes
# chore: tarefas gerais
```

### 8.3 Enviar para GitHub

```bash
# Enviar branch
git push origin feature/django-backend

# No GitHub, abrir Pull Request (PR)
# Descrever as mudanças
# Aguardar review
# Fazer merge para main
```

### 8.4 Workflow Completo

```bash
# 1. Criar branch
git checkout -b feature/chat-polling

# 2. Fazer mudanças
# ... editar arquivos ...

# 3. Verificar mudanças
git status

# 4. Adicionar e commitar
git add .
git commit -m "feat: implementar chat com polling"

# 5. Enviar
git push origin feature/chat-polling

# 6. Abrir PR no GitHub
# ... descrição do PR ...

# 7. Após aprovação, fazer merge
git checkout main
git pull origin main
git merge feature/chat-polling
git push origin main

# 8. Deletar branch local
git branch -d feature/chat-polling
```

### 8.5 .gitignore

Crie `.gitignore` na raiz do projeto:

```
# Virtual Environment
venv/
env/

# Django
*.pyc
__pycache__/
*.db
*.sqlite3
media/
static/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

---

## 9. Checklist de Implementação

### Semana 1
- [ ] Setup Django local
- [ ] Criar modelos (User, Property, Task, Message)
- [ ] Criar banco de dados MySQL
- [ ] Executar migrações

### Semana 2
- [ ] Criar APIs REST (CRUD de tarefas)
- [ ] Implementar autenticação com sessões
- [ ] Testar login/logout
- [ ] Integrar frontend com backend

### Semana 3
- [ ] Implementar S3 para upload de fotos
- [ ] Testar upload de evidências
- [ ] Configurar variáveis de ambiente

### Semana 4
- [ ] Implementar chat com polling
- [ ] Testar envio/recebimento de mensagens
- [ ] Otimizar performance

### Semana 5-6
- [ ] Testes completos
- [ ] Documentação
- [ ] Deploy

---

## 10. Comandos Úteis

```bash
# Criar superusuário
python manage.py createsuperuser

# Listar migrações
python manage.py showmigrations

# Desfazer migração
python manage.py migrate tasks 0001

# Shell Django (testar código)
python manage.py shell

# Coletar arquivos estáticos
python manage.py collectstatic

# Limpar cache
python manage.py clear_cache

# Criar dados de teste
python manage.py seed_data
```

---

## 11. Troubleshooting

### Erro: "No module named 'mysql'"
```bash
pip install mysql-connector-python
```

### Erro: "ModuleNotFoundError: No module named 'rest_framework'"
```bash
pip install djangorestframework
```

### Erro: "CSRF token missing"
```javascript
// Adicione CSRF token em fetch
headers: {
    'X-CSRFToken': getCookie('csrftoken')
}
```

### Erro: "Connection refused" (MySQL)
```bash
# Verifique se MySQL está rodando
# Windows: Services > MySQL
# macOS: brew services start mysql
# Linux: sudo systemctl start mysql
```

---

## 12. Próximos Passos

1. **Hoje**: Setup Django local
2. **Amanhã**: Criar modelos e APIs
3. **Próxima semana**: Integração frontend
4. **Semana seguinte**: S3 e Chat
5. **Semana 4**: Testes e deploy

Qualquer dúvida, me pergunte! 🚀
