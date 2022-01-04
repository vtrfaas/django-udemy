from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

#A função home é a que usa templates
def home(request):
    #return render(request, 'generator/home.html', {'password':'fdfsfsdfsdfsdf'})
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvxwyz')
    #Por padrão o request vem como String, e por padrão senão houver parametros na requisição o valor é 12
    length = int(request.GET.get('length', 12))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXWYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
