from django.shortcuts import render

def dashboard(request):
	context = {}
	return render(request, 'dashboard.html', context)
    
def eventos(request):
	context = {}
	return render(request, 'eventos.html', context)
