from django.shortcuts import render
from django.template import loader
from .models import Duvidas

# Create your views here.

from django.http import HttpResponse


def index(request):
	context = {}
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
	
def dados_fgv(request):
	context = {}
	return render(request, 'dados_fgv.html', context)

def indicadores_fgv(request):
	context = {}
	return render(request, 'indicadores_fgv.html', context)


def community_dwelling(request):
	context = {}
	return render(request, 'community_dwelling.html', context)

def fgv(request):
	context = {}
	return render(request, 'fgv.html', context)

def psicometria(request):
	context = {}
	return render(request, 'psicometria.html', context)

def unasus(request):
	context = {}
	return render(request, 'unasus.html', context)

def rehab(request):
	context = {}
	return render(request, 'rehab.html', context)

def four_question(request):
	context = {}
	return render(request, 'four_question.html', context)

def implementation(request):
	context = {}
	return render(request, 'implementation.html', context)

def criterias(request):
	context = {}
	return render(request, 'criterias.html', context)

def tools_implementation(request):
	context = {}
	return render(request, 'tools_implementation.html', context)