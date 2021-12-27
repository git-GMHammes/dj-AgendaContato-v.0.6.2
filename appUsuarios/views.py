# --- ↓ Para redirecionar a página - ↘
from django.shortcuts import render, redirect
# - Para verificar as autenticações - ↓
from django.contrib import messages, auth
from django.core.validators import validate_email
# --- Para validação de e-mail utilize ↑
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContato
# ↑ Importação veio do ↑ arquivo: \djAgPy\appUsuarios\models.py
#
# Create your views here.


def login(request):
    # ↓ Verifica se não foi enviado POST
    if request.method != 'POST':
        return render(request, 'appUsuarios/usuariologin.html')
    #
    logUsuario = request.POST.get('strUsuario')
    logSenha = request.POST.get('strSenha')
    # Executando a autenticação
    user = auth.authenticate(request, username=logUsuario, password=logSenha)
    if not user:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'appUsuarios/usuariologin.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Usuário logado com sucesso.')
        return redirect('controle')


def sair(request):
    auth.logout(request)
    return redirect('controle')


def cadastro(request):
    # messages.success(request, 'Enviado com sucesso')
    # print(request.POST)
    # exibir o ↗ request do POST
    if request.method != 'POST':
        return render(request, 'appUsuarios/usuariocadastro.html')
    strNome = request.POST.get('strNome')
    strSobrenome = request.POST.get('strSobrenome')
    strUsuario = request.POST.get('strUsuario')
    strEmail = request.POST.get('strEmail')
    strSenha = request.POST.get('strSenha')
    strRepeteSenha = request.POST.get('strRepeteSenha')
    # ↙ ---- Os campos nao podem estar em branco ---- ↘
    if not strNome or not strSobrenome or not strSobrenome \
            or not strUsuario or not strEmail or not strSenha \
            or not strRepeteSenha:
        messages.error(request, 'Não pode enviar campo vazio!')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # ---- ↖ ---- Os campos nao podem estar em branco ---- ↗
    # ↙ Para validar o e-mail
    try:
        validate_email(strEmail)
    except:
        messages.error(request, 'E-mail inválido')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # ---- ↖ Para validar o e-mail ------------------------ ↗
    # ↙ Validar quantidade de caracter
    if len(strUsuario) < 6:
        messages.error(request, 'Usuário deve ter pelo menos 6 caracteres')
        return render(request, 'appUsuarios/usuariocadastro.html')
    if len(strSenha) < 6:
        messages.error(request, 'Senha deve ter pelo menos 6 caracteres')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # --- ↑ Validar quantidade de caracter ------- ↗
    # ↙ Validar senhas ao repetir
    if strSenha != strRepeteSenha:
        messages.error(request, 'Senhas diferentes ao repetir')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # --- ↑ Validar senhas ao repetir ------- ↗
    # ↙ Validar usuário existente
    if User.objects.filter(username=strUsuario).exists():
        messages.error(request, 'Usuário existente. Tente outro usuário')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # --- ↑ Validar senhas ao repetir ------- ↗
    # ↙ Validar usuário existente
    if User.objects.filter(email=strEmail).exists():
        messages.error(request, 'E-mail existente. Tente outro E-mail')
        return render(request, 'appUsuarios/usuariocadastro.html')
    # --- ↑ Validar senhas ao repetir ------- ↗
    messages.success(request, 'Cadastro realizado com sucesso')
    # ↓ Cadastro do usuário no DB ↓
    user = User.objects.create_user(
        username=strUsuario,
        email=strEmail,
        password=strSenha,
        first_name=strNome,
        last_name=strSobrenome
    )
    user.save()
    # ↑ Cadastro do usuário no DB ↑
    return redirect('login')


@login_required(redirect_field_name='login')
def controle(request):
    # ↓ Validar se foi enviado um metodo diferente de POST
    if request.method != 'POST':
        # ↓ Vai para o dicionário abaixo
        form = FormContato()
        # Veio da ↑ importação
        # ---------------------------- pode utilizar qualquer argumento aqui ↓
        return render(request, 'appUsuarios/usuariocontrole.html', {'form': form})
    #
    form = FormContato(request.POST, request.FILES)
    #
    if not form.is_valid():
        messages.error(request, "Erro ao enviar formuário!")
        form = form = FormContato(request.POST)
        return render(request, 'appUsuarios/usuariocontrole.html', {'form': form})
    #
    varDescricao = request.POST.get('texDescricao')
    #
    # ↓ Validar se campo possui mais de 5 caracteres
    if len(varDescricao) < 5:
        messages.error(
            request, "Campo descrição deve possuir mais de 5 caracteres!")
        form = form = FormContato(request.POST)
        return render(request, 'appUsuarios/usuariocontrole.html', {'form': form})
    #
    form.save()
    messages.success(
        request, f'Contato {request.POST.get("strNome")}, salvo com sucesso!')
    return redirect('controle')
