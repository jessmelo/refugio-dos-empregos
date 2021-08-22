from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    vagas = {
         "vaga1": [{
               "titulo": "Analista de Testes Jr.",
               "cidade": "São Paulo - SP",
               "empresa": "PagSeguro PagBank"
         }] ,
         "vaga2":  [{
               "titulo": "Analista de Testes Jr.",
               "cidade": "São Paulo - SP",
               "empresa": "PagSeguro PagBank"
         }]  
     }

    return render(request, "index.html", response)