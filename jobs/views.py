from django.shortcuts import render, redirect
from .models import Jobs

def encontrar_jobs(request):
  jobs = Jobs.objects.all()
  if request.method == 'GET':
    return render(request, 'encontrar_jobs.html')  
