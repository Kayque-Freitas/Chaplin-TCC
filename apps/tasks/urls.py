from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('list/', views.tasks_list_view, name='list'),
    path('create/', views.create_task_view, name='create'),
    path('settings/', views.settings_view, name='settings'),
    path('<int:pk>/', views.task_detail_view, name='detail'),
    path('<int:pk>/edit/', views.edit_task_view, name='edit'),
    path('<int:pk>/assign/', views.assign_task_view, name='assign'),
    path('<int:pk>/complete/', views.complete_task_view, name='complete'),
    path('<int:pk>/message/', views.add_message_view, name='add_message'),
]
