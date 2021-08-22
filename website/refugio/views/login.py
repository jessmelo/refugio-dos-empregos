from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("Hello, world. You're at the Refúgio dos Empregos login.")