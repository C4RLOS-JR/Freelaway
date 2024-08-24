from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      return redirect('/jobs')
    return render(request, 'cadastro.html')
  elif request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')

    if len(username.strip())==0 or len(password.strip())==0:
      messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
      return redirect('cadastro')
      return redirect('cadastro')
    if password != confirm_password:
      messages.add_message(request, constants.ERROR, 'As senhas não são iguais!')
      return redirect('cadastro')
    
    user = User.objects.filter(username=username)

    if user.exists():
      messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome!')
      return redirect('cadastro')

    try:
      novo_usuario = User.objects.create_user(
        username = username,
        password = password
      )
      novo_usuario.save()
      
      messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
      return redirect('logar')
    
    except:
      messages.add_message(request, constants.ERROR, 'Algo deu errado...tente novamente ou contate um administrador!')
      return redirect('cadastro')


def logar(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      return redirect('/jobs')
    return render(request, 'login.html')

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
      
    usuario = auth.authenticate(username=username, password=password)

    if not usuario:
      messages.add_message(request, constants.ERROR, 'Nome do usuário ou senha inválidos!')
      return redirect('logar')
    
    messages.add_message(request, constants.SUCCESS, 'Login efetuado com sucesso!')
    auth.login(request, usuario)

    return redirect('/jobs')
  
def sair(request):
  auth.logout(request)
  return redirect('logar')
