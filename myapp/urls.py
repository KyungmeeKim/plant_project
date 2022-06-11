from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.temp,name='temp'), # 8000/temp로 입력시 이동
    path('humid/', views.humid,name='humid'), # 8000/humid로 입력시 이동
    path('light/', views.light, name='light'),  # 8000/light로 입력시 이동
    path('snapshot/', views.snapshot, name='snapshot')
    path('water/', views.water, name='water')  # 8000/water로 입력시 이동 
]