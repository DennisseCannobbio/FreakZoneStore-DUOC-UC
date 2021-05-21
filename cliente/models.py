from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User # importe el modelo user de admin
import uuid

# Create your models here.
#Register
class Cuenta(models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE) #relacion 1 es a 1
    cuent_rut=models.CharField(max_length=9, help_text="Ingrese rut Ej: 12345678-9", primary_key="True")
    # cuent_email=models.EmailField(max_length=30, help_text="Ingrese email EJ: hola@gmail.com")
    # cuent_pass=models.CharField(max_length=30, help_text="Ingrese contraseña")
    # cuent_nombre=models.CharField(max_length=50, help_text="Ingrese su nombre")
    # cuent_ape=models.CharField(max_length=50, help_text="Ingrese su apellido",default=None)
    cuent_fecnac=models.DateField(default=None,null=True)

    desp_telef=models.CharField(max_length=10, help_text="Ingrese su número de teléfono", default=None, null=True)
    desp_region=models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    com_nombre=models.CharField(max_length=10, help_text="Ingrese el nombre de su comuna",default=None, null=True)
    desp_direccion=models.TextField(max_length=100, help_text="Ingrese su dirección",default=None, null=True)

    #metodos
    def __str__(self):
        return self.cuent_rut

    def get_absolute_url(self):
        return reverse('cliente:profile', args = [str(self.cuent_rut)])

class Region(models.Model):
    reg_id=models.CharField(max_length=5, help_text="Ingrese el id de la region", primary_key="True")
    reg_nombre=models.CharField(max_length=50, help_text="Ingrese nombre de la región")

    #metodos
    def __str__(self):
        return self.reg_id