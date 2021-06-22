from django.shortcuts import render
from django.template import loader
from .models import Membros
from .models import Duvidas

# Create your views here.

from django.http import HttpResponse


def index(request):
	membros = Membros.objects.all()
	lista = ["aaa", "bbb", "ccc", 2, 4, "lala", ["aaa", "bb"]]
	context = {"Nome": "Pessoa", "lista" : lista, "membros" : membros}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def help(request):
	context = {}
	return render(request, 'help.html', context)

def main(request):
	context = {}
	return render(request, 'main.html', context)

def duvidas(request):
	duvidas = Duvidas.objects.all()
	context = {"duvidas" : duvidas}
	return render(request, 'duvidas.html', context)