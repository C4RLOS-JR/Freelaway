from django.shortcuts import render, redirect
from .models import Jobs

def encontrar_jobs(request):
  preco_minimo = request.POST.get('preco_minimo')
  preco_maximo = request.POST.get('preco_maximo')
  prazo_minimo = request.POST.get('prazo_minimo')
  prazo_maximo = request.POST.get('prazo_maximo')
  categoria = request.POST.get('categoria')
  jobs = Jobs.objects.all()

  if preco_minimo:
    jobs = jobs.filter(preco__gte=preco_minimo)
  if preco_maximo:
    jobs = jobs.filter(preco__lte=preco_minimo)
  if prazo_minimo:
    jobs = jobs.filter(prazo_entrega__gte=prazo_minimo)
  if prazo_maximo:
    jobs = jobs.filter(prazo_entrega__lte=prazo_maximo)
  if categoria:
    jobs = jobs.filter(categoria=categoria)

  return render(request, 'encontrar_jobs.html', {'jobs': jobs})
