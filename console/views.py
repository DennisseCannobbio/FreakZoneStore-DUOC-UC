from django.shortcuts import render
from .models import CS
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
#from django .forms import CSCreateForm

# Create your views here.

class IndexView(generic.ListView):
    model = CS
    template_name = 'console/cs_list.html'
    def get_queryset(self):
        return CS.objects.all()

class PS4(generic.ListView):
    model = CS
    tempate_name = 'console/cs_list.html'
    def get_queryset(self):
        return CS.objects.filter(con_tipo__con_tipo__iexact='PlayStation 4')

class NS(generic.ListView):
    model = CS
    template_name = 'console/cs_list.html'
    def get_queryset(self):
        return CS.objects.filter(con_tipo__con_tipo__iexact='Nintendo Switch')

class XBOX(generic.ListView):
    model = CS
    template_name = 'console/cs_list.html'
    def get_queryset(self):
        return CS.objects.filter(con_tipo__con_tipo__iexact='Xbox One')

class DetailView(generic.DetailView):
    model = CS


