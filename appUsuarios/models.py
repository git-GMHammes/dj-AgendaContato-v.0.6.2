from django.db import models
from appContatos.models import DbTabContatos
from django import forms
# Create your models here.
#


class FormContato(forms.ModelForm):
    class Meta:
        model = DbTabContatos
        exclude = ('bolExibir', )
# Agora vc irá para o arquivo: \djAgPy\appUsuarios\views.py
# metodo def controle(request):
# deverá importar a Classe acima
# from .models import FormContato
