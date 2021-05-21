from django.shortcuts import render
from .models import VG
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .forms import VGCreateForm

# Create your views here.
class IndexView(generic.ListView):
    model = VG
    template_name = 'game/vg_list.html'
    def get_queryset(self):
        return VG.objects.all() 

class SwitchGame(generic.ListView):
    model = VG
    template_name = 'game/vg_list.html'
    def get_queryset(self):
        return VG.objects.filter(vg_plat__plat_nom__iexact='Nintendo Switch')

class PS4Game(generic.ListView):
    model = VG
    template_name = 'game/vg_list.html'
    def get_queryset(self):
        return VG.objects.filter(vg_plat__plat_nom__iexact='PlayStation 4')

class XBOGame(generic.ListView):
    model = VG
    template_name = 'game/vg_list.html'
    def get_queryset(self):
        return VG.objects.filter(vg_plat__plat_nom__iexact='Xbox One')

class DetailView(generic.DetailView):
    model = VG

def VGCreate(request):
    form = VGCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit = True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
   
    context = {
        'title':"Crear",
        'form':form
    }
    return render(request,'game/vg_crear.html',context)

def VGSearch(request, id=None):

    queryset= VG.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(vg_id__icontains=query)
    context = {
        "object_list" : queryset,
        "title" : "Busca"
    }
    return render(request, "game/vg_buscar.html",context)


def VGUpdate(request, pk =None):
    instance = get_object_or_404(VG, vg_id = pk)
    form = VGCreateForm(request.POST or None, request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=True)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Editar",
        "instance":instance,
        "form" : form
    }
    return render(request, "game/vg_crear.html",context)


def VGDelete(request, pk= None):
    instance = get_object_or_404(VG, vg_id = pk)
    instance.delete()
    return redirect("game:serchVG")
