from django.urls import path
from .views import *

app_name = 'console'

urlpatterns = [
    path('',IndexView.as_view(), name='allconsole'),
    path('<str:pk>/', DetailView.as_view(), name='details'),
]