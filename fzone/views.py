from django.shortcuts import render
from django.views import generic
from game.models import Banner

class ini(generic.ListView):
    model = Banner
    template_name = 'inicio.html'
    def get_queryset(self):
        return Banner.objects.all

def consolas(request):#Vista todas las consolas
    return render(
        request,
        'consolas.html',
        context={}
    )

def figuras(request):#Vista todas las figuras
    return render(
        request,
        'figuras.html',
        context={}
    )

def videojuegos(request):#Vista todos los videojuegos
    return render(
        request,
        'videojuegos.html',
        context={}
    )

def tcg(request):#Vista todo los TCG
    return render(
        request,
        'tcg.html',
        context={}
    )

def retro(request):#Vista Todo los retro
    return render(
        request,
        'consolasRetro.html',
        context={}
    )
