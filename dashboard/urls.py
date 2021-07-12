from django.urls import path
from . import views


urlpatterns = [
    path('eventos/', views.eventos, name='eventos'),    
    path('evento/<str:evento_id>', views.evento, name='evento'),    
    path('', views.dashboard, name='dashboard'),
]
