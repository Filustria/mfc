from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('main/', views.main, name='main'),
    path('duvidas/', views.duvidas, name='duvidas'),
    path('duvidas_forms/', views.duvidas_formulario, name='duvidas_forms'),
    path('dados_fgv/', views.dados_fgv, name='dados_fgv'),
    path('indicadores_fgv/', views.indicadores_fgv, name='indicadores_fgv'),
    path('community_dwelling/', views.community_dwelling, name='community_dwelling'),
    path('fgv/', views.fgv, name='fgv'),
    path('psicometria/', views.psicometria, name='psicometria'),
    path('unasus/', views.unasus, name='unasus'),
    path('rehab/', views.rehab, name='rehab'),
    path('four_question/', views.four_question, name='four_question'),
    path('implementation/', views.implementation, name='implementation'),
    path('criterias/', views.criterias, name='criterias'),
    path('tools_implementation/', views.tools_implementation, name='tools_implementation'),
]
