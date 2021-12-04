from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def say_hello(request):
    return HttpResponse('Hello world')


def random1(request):
    return HttpResponse(f'<h1>{random.randint(1,10)}</h1>')

def rand_choice(request):
    lst = ['Islam', 'Beka', 'Esen', 'Adahan', 'Batyr']
    return HttpResponse(f"<h1>{random.choice(lst)} LOX</h1>")