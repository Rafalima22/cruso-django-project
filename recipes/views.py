
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('home')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
