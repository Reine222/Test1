from django.shortcuts import render
from . models import *

# Create your views here.

def home(request):
    event = Evenement.objects.filter(statut=True)
    pieces = Type_pieces.objects.filter(statut=True)
    data = {
        'event': event,
        'pieces': pieces,
    }
    return render(request, 'pages/index.html', data)

# def home(request):
#     return render(request, 'pages/home.html')

# def home(request):
#     return render(request, 'pages/home.html')

# def home(request):
#     return render(request, 'pages/home.html')

# def home(request):
#     return render(request, 'pages/home.html')

# def home(request):
#     return render(request, 'pages/home.html')