# Chaplin Backend em Django: Guia Completo

**Estrutura, Modelos, APIs e Exemplos Prontos para Usar**

---

## 1. Visão Geral da Arquitetura

### 1.1 Stack Recomendado

```
Frontend (Estático HTML/CSS)
        ↓ (Requisições HTTP/JSON)
Django REST API (Backend)
        ↓ (Queries)
MySQL Database
```

### 1.2 Tecnologias

| Componente | Tecnologia | Versão |
|-----------|-----------|--------|
| **Framework** | Django | 4.2+ |
| **API** | Django REST Framework | 3.14+ |
| **Autenticação** | Django JWT | 5.3+ |
| **Banco de Dados** | MySQL | 8.0+ |
| **ORM** | Django ORM | Built-in |
| **Validação** | Serializers (DRF) | Built-in |
| **CORS** | django-cors-headers | 4.0+ |

---

## 2. Estrutura de Pastas

```
chaplin-backend/
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── chaplin/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── users/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── tasks/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── proposals/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   ├── chat/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   └── payments/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── urls.py
│       └── migrations/
├── utils/
│   ├── permissions.py
│   ├── pagination.py
│   └── exceptions.py
└── tests/
    ├── test_users.py
    ├── test_tasks.py
    └── test_proposals.py
```

---

## 3. Setup Inicial

### 3.1 Instalação

```bash
# 1. Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Criar banco de dados
python manage.py migrate

# 4. Criar superuser
python manage.py createsuperuser

# 5. Rodar servidor
python manage.py runserver
```

### 3.2 requirements.txt

```
Django==4.2.0
djangorestframework==3.14.0
django-rest-framework-simplejwt==5.3.0
django-cors-headers==4.0.0
django-filter==23.1
python-decouple==3.8
Pillow==10.0.0
stripe==5.15.0
celery==5.3.0
redis==5.0.0
mysqlclient==2.2.0
```

### 3.3 settings.py (Configuração Básica)

```python
import os
from datetime import timedelta
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY', default='sua-chave-secreta-aqui')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Apps instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    
    # Local
    'apps.users',
    'apps.tasks',
    'apps.proposals',
    'apps.chat',
    'apps.payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
]

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
}

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME', default='chaplin'),
        'USER': config('DB_USER', default='root'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}

# Timezone
USE_TZ = True
TIME_ZONE = 'America/Sao_Paulo'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 4. Modelos de Dados (Models)

### 4.1 User Model (apps/users/models.py)

```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Modelo customizado de usuário com campos específicos do Chaplin
    """
    ROLE_CHOICES = (
        ('gestor', 'Gestor de Propriedade'),
        ('profissional', 'Profissional Técnico'),
        ('empresa', 'Empresa Terceirizada'),
    )
    
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        help_text="Tipo de usuário no sistema"
    )
    
    phone = models.CharField(
        max_length=20,
        blank=True,
        help_text="Telefone de contato"
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        help_text="Foto de perfil"
    )
    
    bio = models.TextField(
        blank=True,
        help_text="Biografia ou descrição profissional"
    )
    
    # Para profissionais
    specialties = models.CharField(
        max_length=255,
        blank=True,
        help_text="Especialidades (ex: Hidráulica, Elétrica)"
    )
    
    # Para empresas
    company_name = models.CharField(
        max_length=255,
        blank=True,
        help_text="Nome da empresa"
    )
    
    cnpj = models.CharField(
        max_length=18,
        blank=True,
        unique=True,
        help_text="CNPJ da empresa"
    )
    
    # Avaliação
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.0,
        help_text="Avaliação média (0-5)"
    )
    
    total_tasks_completed = models.IntegerField(
        default=0,
        help_text="Total de tarefas concluídas"
    )
    
    is_verified = models.BooleanField(
        default=False,
        help_text="Usuário verificado"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"
```

### 4.2 Task Model (apps/tasks/models.py)

```python
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    """
    Modelo de Tarefa de Manutenção
    """
    STATUS_CHOICES = (
        ('aberta', 'Aberta'),
        ('em_progresso', 'Em Progresso'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    )
    
    PRIORITY_CHOICES = (
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    )
    
    # Informações básicas
    title = models.CharField(
        max_length=255,
        help_text="Título da tarefa"
    )
    
    description = models.TextField(
        help_text="Descrição detalhada do problema"
    )
    
    # Localização
    room_number = models.CharField(
        max_length=10,
        help_text="Número do quarto/sala"
    )
    
    property = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="Propriedade onde está o problema"
    )
    
    # Status e Prioridade
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='aberta',
        help_text="Status atual da tarefa"
    )
    
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='media',
        help_text="Nível de prioridade"
    )
    
    # Responsáveis
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks_created',
        help_text="Usuário que criou a tarefa"
    )
    
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks_assigned',
        help_text="Profissional responsável"
    )
    
    # Datas
    due_date = models.DateTimeField(
        help_text="Data de vencimento"
    )
    
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Data de conclusão"
    )
    
    # Evidências
    image_before = models.ImageField(
        upload_to='tasks/before/',
        blank=True,
        null=True,
        help_text="Foto antes do serviço"
    )
    
    image_after = models.ImageField(
        upload_to='tasks/after/',
        blank=True,
        null=True,
        help_text="Foto depois do serviço"
    )
    
    completion_notes = models.TextField(
        blank=True,
        help_text="Notas de conclusão"
    )
    
    # Metadados
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'tasks'
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', 'priority']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        return f"[{self.get_status_display()}] {self.title} - Quarto {self.room_number}"


class Property(models.Model):
    """
    Modelo de Propriedade (Hotel/Airbnb)
    """
    name = models.CharField(
        max_length=255,
        help_text="Nome da propriedade"
    )
    
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='properties',
        help_text="Proprietário da propriedade"
    )
    
    address = models.CharField(
        max_length=255,
        help_text="Endereço"
    )
    
    city = models.CharField(
        max_length=100,
        help_text="Cidade"
    )
    
    state = models.CharField(
        max_length=2,
        help_text="Estado (UF)"
    )
    
    total_rooms = models.IntegerField(
        help_text="Total de quartos"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'properties'
        verbose_name = 'Propriedade'
        verbose_name_plural = 'Propriedades'
    
    def __str__(self):
        return f"{self.name} - {self.city}/{self.state}"
```

### 4.3 Proposal Model (apps/proposals/models.py)

```python
from django.db import models
from django.contrib.auth import get_user_model
from apps.tasks.models import Task

User = get_user_model()

class Proposal(models.Model):
    """
    Modelo de Proposta de Serviço
    """
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('aceita', 'Aceita'),
        ('rejeitada', 'Rejeitada'),
        ('cancelada', 'Cancelada'),
    )
    
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='proposals',
        help_text="Tarefa relacionada"
    )
    
    professional = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='proposals_made',
        help_text="Profissional que fez a proposta"
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Valor proposto"
    )
    
    estimated_hours = models.IntegerField(
        help_text="Horas estimadas para conclusão"
    )
    
    description = models.TextField(
        help_text="Descrição da proposta"
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        help_text="Status da proposta"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'proposals'
        verbose_name = 'Proposta'
        verbose_name_plural = 'Propostas'
        unique_together = ('task', 'professional')
    
    def __str__(self):
        return f"Proposta de {self.professional.get_full_name()} - R${self.price}"
```

---

## 5. Serializers (Validação e Conversão)

### 5.1 User Serializer (apps/users/serializers.py)

```python
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer para usuários (leitura)
    """
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone', 'avatar', 'bio', 'specialties',
            'company_name', 'rating', 'total_tasks_completed',
            'is_verified', 'created_at'
        )
        read_only_fields = ('id', 'created_at', 'rating', 'total_tasks_completed')


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer para criar novo usuário (registro)
    """
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        help_text="Mínimo 8 caracteres"
    )
    password_confirm = serializers.CharField(
        write_only=True,
        help_text="Confirmação de senha"
    )
    
    class Meta:
        model = User
        fields = (
            'username', 'email', 'password', 'password_confirm',
            'first_name', 'last_name', 'role', 'phone'
        )
    
    def validate(self, data):
        """Validar senhas"""
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError(
                {"password": "As senhas não conferem"}
            )
        return data
    
    def create(self, validated_data):
        """Criar usuário"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer customizado para login (retorna dados do usuário)
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Adicionar dados customizados ao token
        token['username'] = user.username
        token['role'] = user.role
        token['email'] = user.email
        
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Adicionar dados do usuário na resposta
        data['user'] = UserSerializer(self.user).data
        
        return data
```

### 5.2 Task Serializer (apps/tasks/serializers.py)

```python
from rest_framework import serializers
from apps.tasks.models import Task, Property
from apps.users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer para tarefas
    """
    created_by_detail = UserSerializer(
        source='created_by',
        read_only=True
    )
    assigned_to_detail = UserSerializer(
        source='assigned_to',
        read_only=True
    )
    
    class Meta:
        model = Task
        fields = (
            'id', 'title', 'description', 'room_number',
            'property', 'status', 'priority',
            'created_by', 'created_by_detail',
            'assigned_to', 'assigned_to_detail',
            'due_date', 'completed_at',
            'image_before', 'image_after',
            'completion_notes', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'created_by', 'created_at', 'updated_at',
            'completed_at'
        )
    
    def create(self, validated_data):
        """Criar tarefa com usuário atual como criador"""
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)


class PropertySerializer(serializers.ModelSerializer):
    """
    Serializer para propriedades
    """
    class Meta:
        model = Property
        fields = (
            'id', 'name', 'owner', 'address', 'city',
            'state', 'total_rooms', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')
    
    def create(self, validated_data):
        """Criar propriedade com usuário atual como dono"""
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)
```

---

## 6. Views (API Endpoints)

### 6.1 User Views (apps/users/views.py)

```python
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from apps.users.serializers import (
    UserSerializer, UserCreateSerializer,
    CustomTokenObtainPairSerializer
)

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar usuários
    
    Endpoints:
    - GET /api/users/ - Listar usuários
    - POST /api/users/ - Criar novo usuário
    - GET /api/users/{id}/ - Detalhes do usuário
    - PUT /api/users/{id}/ - Atualizar usuário
    - DELETE /api/users/{id}/ - Deletar usuário
    - POST /api/users/register/ - Registro de novo usuário
    - GET /api/users/me/ - Dados do usuário logado
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        """Usar serializer diferente para criação"""
        if self.action == 'create' or self.action == 'register':
            return UserCreateSerializer
        return UserSerializer
    
    def get_permissions(self):
        """Permitir criação sem autenticação"""
        if self.action == 'create' or self.action == 'register':
            return [AllowAny()]
        return super().get_permissions()
    
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        """
        Endpoint de registro
        POST /api/users/register/
        """
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'message': 'Usuário criado com sucesso',
                    'user': UserSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Endpoint para obter dados do usuário logado
        GET /api/users/me/
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['put'], permission_classes=[IsAuthenticated])
    def update_profile(self, request):
        """
        Endpoint para atualizar perfil do usuário logado
        PUT /api/users/update_profile/
        """
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'message': 'Perfil atualizado com sucesso',
                    'user': serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Endpoint customizado de login
    POST /api/token/
    """
    serializer_class = CustomTokenObtainPairSerializer
```

### 6.2 Task Views (apps/tasks/views.py)

```python
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from apps.tasks.models import Task, Property
from apps.tasks.serializers import TaskSerializer, PropertySerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar tarefas
    
    Endpoints:
    - GET /api/tasks/ - Listar tarefas
    - POST /api/tasks/ - Criar tarefa
    - GET /api/tasks/{id}/ - Detalhes da tarefa
    - PUT /api/tasks/{id}/ - Atualizar tarefa
    - DELETE /api/tasks/{id}/ - Deletar tarefa
    - POST /api/tasks/{id}/complete/ - Marcar como concluída
    - GET /api/tasks/my-tasks/ - Minhas tarefas
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'priority', 'property']
    search_fields = ['title', 'description', 'room_number']
    ordering_fields = ['created_at', 'due_date', 'priority']
    ordering = ['-created_at']
    
    def get_queryset(self):
        """Filtrar tarefas por usuário"""
        user = self.request.user
        
        # Gestores veem suas propriedades
        # Profissionais veem tarefas atribuídas a eles
        if user.role == 'gestor':
            return Task.objects.filter(property__owner=user)
        elif user.role == 'profissional':
            return Task.objects.filter(assigned_to=user)
        
        return Task.objects.all()
    
    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """
        Marcar tarefa como concluída
        POST /api/tasks/{id}/complete/
        """
        task = self.get_object()
        
        # Validações
        if task.status == 'concluida':
            return Response(
                {'error': 'Tarefa já está concluída'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if task.assigned_to != request.user:
            return Response(
                {'error': 'Você não está autorizado a concluir esta tarefa'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Atualizar tarefa
        task.status = 'concluida'
        task.completed_at = timezone.now()
        task.completion_notes = request.data.get('completion_notes', '')
        
        # Salvar imagens se fornecidas
        if 'image_after' in request.FILES:
            task.image_after = request.FILES['image_after']
        
        task.save()
        
        return Response(
            {
                'message': 'Tarefa concluída com sucesso',
                'task': TaskSerializer(task).data
            }
        )
    
    @action(detail=False, methods=['get'])
    def my_tasks(self, request):
        """
        Listar minhas tarefas
        GET /api/tasks/my_tasks/
        """
        tasks = self.get_queryset()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Estatísticas de tarefas
        GET /api/tasks/statistics/
        """
        tasks = self.get_queryset()
        
        stats = {
            'total': tasks.count(),
            'aberta': tasks.filter(status='aberta').count(),
            'em_progresso': tasks.filter(status='em_progresso').count(),
            'concluida': tasks.filter(status='concluida').count(),
            'cancelada': tasks.filter(status='cancelada').count(),
        }
        
        return Response(stats)


class PropertyViewSet(viewsets.ModelViewSet):
    """
    API para gerenciar propriedades
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Filtrar propriedades do usuário"""
        return Property.objects.filter(owner=self.request.user)
```

---

## 7. URLs (Rotas da API)

### 7.1 apps/users/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from apps.users.views import UserViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 7.2 apps/tasks/urls.py

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tasks.views import TaskViewSet, PropertyViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'properties', PropertyViewSet, basename='property')

urlpatterns = [
    path('', include(router.urls)),
]
```

### 7.3 chaplin/urls.py (Principal)

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/', include('apps.tasks.urls')),
    path('api/proposals/', include('apps.proposals.urls')),
    path('api/chat/', include('apps.chat.urls')),
    path('api/payments/', include('apps.payments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## 8. Integração com Frontend

### 8.1 Exemplo: Criar Tarefa (JavaScript)

```javascript
// 1. Obter token JWT (após login)
const loginData = {
    username: 'usuario@example.com',
    password: 'senha123'
};

const loginResponse = await fetch('http://localhost:8000/api/users/token/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(loginData)
});

const { access } = await loginResponse.json();
const token = access;

// 2. Criar tarefa
const taskData = {
    title: 'Consertar torneira do banheiro',
    description: 'Torneira do banheiro está vazando água',
    room_number: '302',
    property: 1,
    priority: 'alta',
    due_date: '2024-02-25T10:00:00Z'
};

const taskResponse = await fetch('http://localhost:8000/api/tasks/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(taskData)
});

const task = await taskResponse.json();
console.log('Tarefa criada:', task);

// 3. Listar tarefas
const listResponse = await fetch('http://localhost:8000/api/tasks/', {
    headers: {
        'Authorization': `Bearer ${token}`
    }
});

const tasks = await listResponse.json();
console.log('Tarefas:', tasks);

// 4. Atualizar tarefa
const updateResponse = await fetch(`http://localhost:8000/api/tasks/${task.id}/`, {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({
        status: 'em_progresso',
        assigned_to: 2
    })
});

const updatedTask = await updateResponse.json();
console.log('Tarefa atualizada:', updatedTask);
```

### 8.2 Exemplo: Completar Tarefa com Foto

```javascript
// Completar tarefa com foto
const formData = new FormData();
formData.append('completion_notes', 'Torneira consertada com sucesso');
formData.append('image_after', fileInput.files[0]); // Arquivo da foto

const completeResponse = await fetch(
    `http://localhost:8000/api/tasks/${taskId}/complete/`,
    {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${token}`
        },
        body: formData
    }
);

const completedTask = await completeResponse.json();
console.log('Tarefa concluída:', completedTask);
```

### 8.3 Wrapper JavaScript para Facilitar

```javascript
// utils/api.js
class ChaplinAPI {
    constructor(baseURL = 'http://localhost:8000/api') {
        this.baseURL = baseURL;
        this.token = localStorage.getItem('token');
    }
    
    setToken(token) {
        this.token = token;
        localStorage.setItem('token', token);
    }
    
    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };
        
        if (this.token) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }
        
        const response = await fetch(url, {
            ...options,
            headers
        });
        
        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`);
        }
        
        return response.json();
    }
    
    // Autenticação
    async login(username, password) {
        const data = await this.request('/users/token/', {
            method: 'POST',
            body: JSON.stringify({ username, password })
        });
        this.setToken(data.access);
        return data;
    }
    
    async register(userData) {
        return this.request('/users/register/', {
            method: 'POST',
            body: JSON.stringify(userData)
        });
    }
    
    // Tarefas
    async getTasks(filters = {}) {
        const query = new URLSearchParams(filters).toString();
        return this.request(`/tasks/?${query}`);
    }
    
    async createTask(taskData) {
        return this.request('/tasks/', {
            method: 'POST',
            body: JSON.stringify(taskData)
        });
    }
    
    async completeTask(taskId, completionData) {
        const formData = new FormData();
        Object.keys(completionData).forEach(key => {
            formData.append(key, completionData[key]);
        });
        
        return this.request(`/tasks/${taskId}/complete/`, {
            method: 'POST',
            headers: {},
            body: formData
        });
    }
    
    // Usuário
    async getMe() {
        return this.request('/users/me/');
    }
    
    async updateProfile(userData) {
        return this.request('/users/update_profile/', {
            method: 'PUT',
            body: JSON.stringify(userData)
        });
    }
}

// Uso
const api = new ChaplinAPI();

// Login
await api.login('usuario@example.com', 'senha123');

// Criar tarefa
const task = await api.createTask({
    title: 'Consertar torneira',
    description: 'Torneira vazando',
    room_number: '302',
    property: 1,
    priority: 'alta',
    due_date: '2024-02-25T10:00:00Z'
});

// Listar tarefas
const tasks = await api.getTasks({ status: 'aberta', priority: 'alta' });

// Completar tarefa
const completionData = {
    completion_notes: 'Concluído com sucesso',
    image_after: fileInput.files[0]
};
await api.completeTask(task.id, completionData);
```

---

## 9. Permissões Customizadas

### 9.1 utils/permissions.py

```python
from rest_framework import permissions

class IsTaskOwner(permissions.BasePermission):
    """
    Permissão: Apenas o criador da tarefa pode editá-la
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user


class IsTaskAssignee(permissions.BasePermission):
    """
    Permissão: Apenas o profissional atribuído pode completar
    """
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user


class IsPropertyOwner(permissions.BasePermission):
    """
    Permissão: Apenas o dono da propriedade pode gerenciá-la
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
```

---

## 10. Testes

### 10.1 tests/test_tasks.py

```python
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from apps.tasks.models import Task, Property

User = get_user_model()

class TaskAPITestCase(TestCase):
    def setUp(self):
        """Preparar dados de teste"""
        self.client = APIClient()
        
        # Criar usuários
        self.gestor = User.objects.create_user(
            username='gestor@test.com',
            password='test123',
            role='gestor'
        )
        
        self.profissional = User.objects.create_user(
            username='prof@test.com',
            password='test123',
            role='profissional'
        )
        
        # Criar propriedade
        self.property = Property.objects.create(
            name='Hotel Test',
            owner=self.gestor,
            address='Rua Test, 123',
            city='São Paulo',
            state='SP',
            total_rooms=10
        )
    
    def test_create_task(self):
        """Testar criação de tarefa"""
        self.client.force_authenticate(user=self.gestor)
        
        data = {
            'title': 'Consertar torneira',
            'description': 'Torneira vazando',
            'room_number': '302',
            'property': self.property.id,
            'priority': 'alta',
            'due_date': '2024-02-25T10:00:00Z'
        }
        
        response = self.client.post('/api/tasks/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
    
    def test_list_tasks(self):
        """Testar listagem de tarefas"""
        self.client.force_authenticate(user=self.gestor)
        
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_complete_task(self):
        """Testar conclusão de tarefa"""
        # Criar tarefa
        task = Task.objects.create(
            title='Consertar torneira',
            description='Torneira vazando',
            room_number='302',
            property=self.property,
            created_by=self.gestor,
            assigned_to=self.profissional,
            due_date='2024-02-25T10:00:00Z'
        )
        
        # Profissional conclui
        self.client.force_authenticate(user=self.profissional)
        
        data = {
            'completion_notes': 'Concluído com sucesso'
        }
        
        response = self.client.post(
            f'/api/tasks/{task.id}/complete/',
            data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, 'concluida')
```

---

## 11. Deploy

### 11.1 Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Executar migrações e coletar arquivos estáticos
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Expor porta
EXPOSE 8000

# Comando para rodar
CMD ["gunicorn", "chaplin.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 11.2 docker-compose.yml

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_DATABASE: chaplin
      MYSQL_ROOT_PASSWORD: root123
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DEBUG=True
      - DB_NAME=chaplin
      - DB_USER=root
      - DB_PASSWORD=root123
      - DB_HOST=db

volumes:
  mysql_data:
```

---

## 12. Checklist de Implementação

- [ ] Setup inicial do Django
- [ ] Configurar banco de dados MySQL
- [ ] Criar modelos (User, Task, Property, Proposal)
- [ ] Criar serializers
- [ ] Criar views/viewsets
- [ ] Configurar URLs
- [ ] Implementar autenticação JWT
- [ ] Configurar CORS
- [ ] Criar testes
- [ ] Documentar API (Swagger/DRF)
- [ ] Fazer deploy

---

## 13. Próximos Passos

1. **Implementar Chat em Tempo Real** (WebSockets)
2. **Integrar Stripe** para pagamentos
3. **Adicionar Notificações** (Email/SMS)
4. **Implementar Sistema de Avaliações**
5. **Criar Dashboard de Análises**

---

**Pronto para começar? Clone o repositório e siga o setup inicial!** 🚀

