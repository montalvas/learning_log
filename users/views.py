from django.shortcuts import render
from django.contrib.auth import logout
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