from django.shortcuts import render
from dashboard.models import Evento
from django.http import Http404
import json


def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)


def eventos(request):
    eventos = Evento.objects.filter(tipo='HOSPT')
    data = [
        {"name" : e.nome, 
        "value" : e.ocorrencias,
        "ocorrencias" : e.ocorrencias,
        "ponto" : e.ponto,
        "upper" : e.upper,
        "lower" : e.lower,
        "y" : e.risco,
        "z" : e.oportunidades
        } for e in eventos[:10]]
    context = {'eventos': eventos, 'data' : json.dumps(data)}
    return render(request, 'eventos.html', context)


def evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
        evento.menos_ponto = round((1 - evento.ponto)*100, 1)
    except Evento.DoesNotExist:
        raise Http404("Evento does not exist")
    context = {'evento': evento}
    return render(request, 'evento.html', context)
