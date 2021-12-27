from typing import Pattern
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index_login'), 
    path('login/', views.login, name='login'), 
    path('sair/', views.sair, name='sair'), 
    path('cadastro/', views.cadastro, name='cadastro'), 
    path('controle/', views.controle, name='controle'), 
    # ATENçÃO: --- ↑ - Não esquecer da barra!!! 
    # Lembre-se que no: djAgPy\agendaContatos\urls.py 
    # Também deve ter a barra no final.
]
