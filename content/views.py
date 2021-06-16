from django.shortcuts import render
from django.template import loader
from .models import Membros

# Create your views here.

from django.http import HttpResponse


def index(request):
	membros = Membros.objects.all()
	lista = ["aaa", "bbb", "ccc", 2, 4, "lala", ["aaa", "bb"]]
	context = {"Nome": "Thais", "lista" : lista, "membros" : membros}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def help(request):
	context = {}
	return render(request, 'help.html', context)