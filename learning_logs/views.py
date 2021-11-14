from django.shortcuts import render


def index(request):
    """Processa e renderiza a página inicial"""
    return render(request, 'learning_logs/index.html')
