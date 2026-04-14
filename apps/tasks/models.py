from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    """Modelo de Tarefa de Manutenção"""
    
    PRIORITY_CHOICES = [
        ('baixa', 'Baixa'),
        ('normal', 'Normal'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    STATUS_CHOICES = [
        ('aberta', 'Aberta'),
        ('alocada', 'Alocada'),
        ('concluida', 'Concluída'),
        ('finalizada', 'Finalizada'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='normal')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberta')
    
    # Relacionamentos
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tasks_created')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned')
    
    # Datas
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    # Localização e Tipo
    # Descrição manual do local (setor/sala) — mantido por compatibilidade
    location = models.CharField(max_length=200, blank=True, verbose_name='Local / Setor')
    # Endereço completo via ViaCEP
    cep = models.CharField(max_length=9, blank=True, verbose_name='CEP')
    logradouro = models.CharField(max_length=200, blank=True, verbose_name='Logradouro')
    numero = models.CharField(max_length=20, blank=True, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=100, blank=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, verbose_name='Estado')

    @property
    def endereco_completo(self):
        """Retorna o endereço formatado, se preenchido."""
        partes = []
        if self.logradouro:
            partes.append(self.logradouro)
        if self.numero:
            partes.append(self.numero)
        if self.complemento:
            partes.append(self.complemento)
        if self.bairro:
            partes.append(self.bairro)
        if self.cidade and self.estado:
            partes.append(f"{self.cidade} - {self.estado}")
        elif self.cidade:
            partes.append(self.cidade)
        if self.cep:
            partes.append(self.cep)
        return ', '.join(partes) if partes else None
    
    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
    
    class Meta:
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
        ordering = ['-created_at']


class TaskEvidence(models.Model):
    """Modelo para Evidências de Conclusão de Tarefa"""
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='evidences')
    photo = models.ImageField(upload_to='evidences/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Evidência - {self.task.title}"
    
    class Meta:
        verbose_name = "Evidência"
        verbose_name_plural = "Evidências"


class Message(models.Model):
    """Modelo para Mensagens/Chat por Tarefa"""
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Mensagem de {self.sender.username} em {self.task.title}"
    
    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ['created_at']


class Notification(models.Model):
    """Notificações do sistema para os usuários"""

    TYPE_CHOICES = [
        ('tarefa_atribuida', 'Tarefa Atribuída'),
        ('tarefa_concluida', 'Tarefa Concluída'),
        ('tarefa_finalizada', 'Tarefa Finalizada'),
        ('nova_mensagem', 'Nova Mensagem'),
        ('tarefa_criada', 'Tarefa Criada'),
        ('sistema', 'Sistema'),
    ]

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    tipo = models.CharField(max_length=30, choices=TYPE_CHOICES, default='sistema')
    titulo = models.CharField(max_length=200)
    mensagem = models.TextField(blank=True)
    lida = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_tipo_display()}] {self.titulo} → {self.recipient.username}"

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
        ordering = ['-created_at']
