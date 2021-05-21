from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Cuenta
from .forms import ClienteCreateForm,FormUser

# Create your views here.

# class CuentaCreate(CreateView):
#     model = Cuenta
#     fields = '__all__'
#     initial = {'cuent_fecnac':'01/01/2019',}
#     success_url = reverse_lazy('inicio')

def CuentaCreate(request):
    form_user = FormUser(request.POST or None) # formulario user
    form_cliente = ClienteCreateForm(request.POST or None) # formulario cliente
    

    if form_user.is_valid() and form_cliente.is_valid(): #si esta los formularios validados
        user = form_user.save() 

        cliente = form_cliente.save(commit=False) # gurada el formulario pero no lo envia a la base de datos
        cliente.user = user # inicializa el campo user con los datos del form_user


        cliente.save() # guarda en la base de datos


        username = form_user.cleaned_data.get('username') # obtienen el username
        password = form_user.cleaned_data.get('password1')#obtienen la password
        user = authenticate(username = username, password = password) # los verifica, si existen 
        login(request,user) #inicia sesion automaticamente
        return redirect('inicio') # redireige al inicio de la pagina  
    context = {
    'form_user': form_user,
    'form_cliente':form_cliente
    }
    return render(request,'cliente/cuenta_form.html',context)


class CuentaUpdate(UpdateView):
    model = Cuenta
    fields = ['cuent_email','cuent_pass','cuent_nombre','cuent_desp','cuent_seg','cuent_pago']

class CuentaDelete(DeleteView):
    model = Cuenta
    success_url = reverse_lazy('Clientes')

from django.views import generic


class ProfileDetailView(generic.DetailView):
    model = Cuenta