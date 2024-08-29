from django.shortcuts import render, redirect
from .models import Jobs

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

  jobs = jobs.order_by('prazo_entrega') # Ordena os 

  return render(request, 'encontrar_jobs.html', {'jobs': jobs})


def aceitar_job(request, id_job):
  job = Jobs.objects.get(id=id_job)
  job.profissional = request.user
  job.reservado = True
  job.save()

  return redirect('encontrar_jobs')


def perfil(request):
  if request.method == 'GET':
    return render(request, 'perfil.html')
