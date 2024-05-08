from django.shortcuts import render
from django.http import HttpResponse

def recipes(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('Página sobre')

def contact(request):
    return HttpResponse('Página contato')
