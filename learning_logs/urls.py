"""Define padrões de URL para learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
    
    # Mostra todos os assuntos
    path('topics/', views.topics, name='topics'),
]
