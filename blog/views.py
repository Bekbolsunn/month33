from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def say_hello(request):
    return HttpResponse(f'Hello world')


def random1(request):
    return HttpResponse(f'<h1>Привет</h1>')


def rand_choice(request):
    return HttpResponse(f"<h1>Здравстуйте</h1>")
