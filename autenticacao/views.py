from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages
from .models import Cadastro

def cadastro(request):
  if request.method == 'GET':
    return render(request, 'cadastro.html')

  elif request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if (len(username.strip())==0) or (len(password.strip())==0) or (len(confirm_password.strip())==0):
      messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
      return redirect('cadastro')
    if password != confirm_password:
      messages.add_message(request, constants.ERROR, 'As senhas não conferem!')
      return redirect('cadastro')
    
    novo_usuario = Cadastro(
      username = username,
      password = password,
      confirm_password = confirm_password
    )
    # novo_usuario.save()
    
    messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso...faça o login para entrar!')
    return redirect('logar')

def logar(request):
  if request.method == 'GET':
    return render(request, 'login.html')

  return HttpResponse('login')
