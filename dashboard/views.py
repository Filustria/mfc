from django.shortcuts import render
from dashboard.models import Evento
from django.http import Http404


def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)


def eventos(request):
    eventos = Evento.objects.all()
    context = {'eventos': eventos}
    return render(request, 'eventos.html', context)


def evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
    except Evento.DoesNotExist:
        raise Http404("Evento does not exist")
    context = {'evento': evento}
    return render(request, 'evento.html', context)
