from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#A função home é a que usa templates
def home(request):
    #return render(request, 'generator/home.html', {'password':'fdfsfsdfsdfsdf'})
    return render(request, 'generator/home.html')

def password(request):
    return render(request, 'generator/password.html')
