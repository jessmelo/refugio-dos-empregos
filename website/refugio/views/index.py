from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = {
         "hello" : "Hello, world. You're at the Refúgio dos Empregos index."
    }

    return render(request, "index.html", response)