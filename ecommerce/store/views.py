from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    return HttpResponse('<h1>Home</h1')

def aboutPage(request):
    return render(request, 'about.html') 
    return HttpResponse('<h1>aboutPage</h1')
