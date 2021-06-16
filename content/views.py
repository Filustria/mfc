from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse


def index(request):
	context = {"Nome": "Thais"}
	template = loader.get_template('index.html')
	return HttpResponse(template.render(context, request))

def help(request):
	context = {}
	print(request.__dict__)
	return render(request, 'help.html', context)