from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    # página de login
    path('login/', UserLoginView.as_view(), name='login'),
    
    # página de logout
    path('logout/', logout_view, name='logout'),
    
    # página de cadastro
    path('register/', register, name='register')
]
