# Criar um arquivo igual o 'urls.py' do projeto
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
]
