from django.urls import path
from .views import *


app_name='cliente'

urlpatterns = [
    path('cuenta/create/',CuentaCreate, name='reg'),
    path('<str:pk>/', ProfileDetailView.as_view(), name = 'profile')
    #path('cuenta/create/',CuentaCreate.as_view(), name='reg')
]