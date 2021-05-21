from django.urls import path
from .views import *

app_name='game'

urlpatterns = [
    path('',IndexView.as_view(), name='allgame'),
    path('nsw/', SwitchGame.as_view(), name='nswgame'),
    path('ps4/', PS4Game.as_view(), name='ps4game'),
    path('xbo/', XBOGame.as_view(), name='xbogame'),
    path('<str:pk>/', DetailView.as_view(), name='details'),
    #path(r'^', VGUpdate, name='Editar'),
    path(r'mantenedor/editar/<pk>/', VGUpdate, name='editar'),
    path('mantenedor/create/', VGCreate, name='createVG'),
    path('mantenedor/buscar/', VGSearch, name='serchVG'),
    path(r'mantenedor/Eliminar/<pk>/', VGDelete, name='eliminar'),
]
