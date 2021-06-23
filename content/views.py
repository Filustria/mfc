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

def duvidas_formulario(request):
	if request.method == 'GET':
		return render(request, 'duvidas_formulario.html', {})
	elif request.method == 'POST':
		d = Duvidas(Duvida=request.POST["Duvida"], 
			Descricao=request.POST["Descricao"], 
			Tipo_de_duvida=request.POST["Tipo_de_duvida"], 
			dificuldade=request.POST["dificuldade"], 
			novidade=request.POST["novidade"])
		d.save()
		duvidas = Duvidas.objects.all()
		context = {"duvidas" : duvidas}
		return render(request, 'duvidas.html', context)
	

