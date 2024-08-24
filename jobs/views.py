from django.shortcuts import render, redirect
from .models import Jobs

def encontrar_jobs(request):
  if request.method == 'GET':
    jobs = Jobs.objects.all()
    
