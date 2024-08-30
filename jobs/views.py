from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Jobs
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse, FileResponse


def encontrar_jobs(request):
  preco_minimo = request.GET.get('preco_minimo')
  preco_maximo = request.GET.get('preco_maximo')
  prazo_minimo = request.GET.get('prazo_minimo')
  prazo_maximo = request.GET.get('prazo_maximo')
  categoria = request.GET.get('categoria')
  jobs = Jobs.objects.filter(reservado=False)

  if preco_minimo:
    jobs = jobs.filter(preco__gte=preco_minimo)
  if preco_maximo:
    jobs = jobs.filter(preco__lte=preco_maximo)
  if prazo_minimo:
    jobs = jobs.filter(prazo_entrega__gte=prazo_minimo)
  if prazo_maximo:
    jobs = jobs.filter(prazo_entrega__lte=prazo_maximo)
  if categoria:
    jobs = jobs.filter(categoria=categoria)

  jobs = jobs.order_by('prazo_entrega') # Ordena os jobs pelo prazo de entrega.

  return render(request, 'encontrar_jobs.html', {'jobs': jobs})


def aceitar_job(request, id_job):
  job = Jobs.objects.get(id=id_job)
  job.profissional = request.user
  job.reservado = True
  job.save()

  return redirect('encontrar_jobs')


def perfil(request):
  if request.method == 'GET':
    jobs = Jobs.objects.filter(profissional=request.user)
    return render(request, 'perfil.html', {'jobs': jobs})
  elif request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    first_name = request.POST.get('primeiro_nome')
    last_name = request.POST.get('ultimo_nome')

    usuario = User.objects.filter(username=username).exclude(id=request.user.id)

    if usuario.exists():
      messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username!')
      return redirect('perfil')

    try:
      request.user.username = username
      request.user.email = email
      request.user.first_name = first_name
      request.user.last_name = last_name
      request.user.save()
      messages.add_message(request, constants.SUCCESS, 'Dados alterados com sucesso!')
    except:
      messages.add_message(request, constants.ERROR, 'Algo deu errado...tente novamente ou contate um administrador!')

    return redirect('perfil')


def enviar_projeto(request):
  id_job = request.POST.get('id_job')
  arquivos = request.FILES.get('arquivos')
  job = Jobs.objects.get(id)

  pass
