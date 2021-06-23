from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('main/', views.main, name='main'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('duvidas_forms/', views.duvidas_formulario, name='duvidas_forms'),
]
