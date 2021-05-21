from django.db import models
from django.urls import reverse
import uuid

class Conn(models.Model):
    #campos
    conn_desc=models.CharField(max_length=100,help_text="Ingrese Descripcion de la conectividad")
    
    def __str__(self):
        return self.conn_desc

class CS(models.Model):
    #campos
    cs_id=models.CharField(max_length=10,help_text="Ingrese ID de la Consola",primary_key="True")
    cs_nom=models.CharField(max_length=100,help_text="Ingrese Nombre de la Consola")
    cs_price=models.IntegerField(help_text="Ingrese el precio de la consola (Ej: $ 999 999).")
    cs_wght=models.IntegerField(help_text="Ingrese el peso de la consola en gramos.")
    cs_descr=models.TextField(max_length=3000, help_text="Ingrese la descripcion de la consola.")
    cs_res=models.CharField(max_length=50,help_text="Ingrese resoluciones soportadas")
    cs_color=models.CharField(max_length=50,help_text="Ingrese color(es).")
    cs_storage=models.CharField(max_length=50,help_text="Ingrese almacenamiento.")

    cs_main_img=models.ImageField(upload_to="gallery", null=True)

    cs_plat=models.ForeignKey('Plat', on_delete=models.SET_NULL, null=True)

    cs_conn=models.ManyToManyField(Conn)

    #metodos
    def __str__(self):
        return self.cs_nom

    def get_absolute_url(self):
        return reverse('console:details', args=[str(self.cs_id)])

class CSInstance(models.Model):
    cinst_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID para esta unidad')
    cinst_cs = models.ForeignKey('CS', on_delete=models.SET_NULL, null=True)
    cinst_on_stock = models.BooleanField(null=True)

    class Meta:
        ordering = ['cinst_id']

    def __str__(self):
        return f'{self.cinst_id} ({self.cinst_cs.cs_nom})'

class Plat(models.Model):
    #campos
    plat_nom=models.CharField(max_length=100,help_text="Ingrese Nombre de la plataforma")

    #metodos
    def __str__(self):
        return self.plat_nom