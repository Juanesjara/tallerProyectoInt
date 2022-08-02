from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'JuanessJara'})

def about(resquest):
    return render( resquest, "about.html")