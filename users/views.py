from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse


class UserLoginView(LoginView):
    """Faz login do usuário"""
    template_name = "users/login.html"

def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Faz o cadastro de um novo usuário"""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redireciona para a página inicial
            authenticated_user = authenticate(username=new_user.username,
                                            password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)