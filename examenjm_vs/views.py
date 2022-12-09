from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'dashboard.html')

def filtrosectores(request):
    return render(request, 'filtroporsectores.html')