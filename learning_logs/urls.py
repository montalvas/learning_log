"""Define padrões de URL para learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
    
    # Página de detalhes de um assunto específico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Página de cadastro de assunto
    path('topics/new_topic/', views.new_topic, name='new_topic'),
    
    # Página de cadastro de registro
    path('topics/new_entry/<int:topic_id>/', views.new_entry, name='new_entry')
]
