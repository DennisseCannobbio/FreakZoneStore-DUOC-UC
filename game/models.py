from django.db import models
from django.urls import reverse
import uuid

#Videogames
# Create your models here.
class Genre(models.Model):
    #campos
    gen_desc=models.CharField(max_length=100,help_text="Ingrese Descripcion del genero")

    #metodos
    def __str__(self):
        return self.gen_desc

class IdiomaTx(models.Model):
    #campos
    lang_desc=models.CharField(max_length=100,help_text="Ingrese Descripcion del idioma")

    #metodos
    def __str__(self):
        return self.lang_desc

class IdiomaAu(models.Model):
    #campos
    lang_desc=models.CharField(max_length=100,help_text="Ingrese Descripcion del idioma")

    #metodos
    def __str__(self):
        return self.lang_desc

class VG(models.Model):

    #campos
    vg_id=models.CharField(max_length=10,help_text="Ingrese ID del Juego",primary_key="True")
    vg_nom=models.CharField(max_length=100,help_text="Ingrese Nombre del Juego")
    vg_price=models.IntegerField(help_text="Ingrese el precio del juego (Ej: $ 999 999).")
    vg_descr=models.TextField(max_length=3000, help_text="Ingrese la descripcion del juego.")
    vg_prev=models.BooleanField(null=True)
    vg_online=models.BooleanField(null=True)
    vg_online_plyr=models.IntegerField(help_text="Ingrese La cantidad de jugadores online.")
    vg_local_plyr=models.IntegerField(help_text="Ingrese La cantidad de jugadores local (Ej: 1).")

    vg_main_img=models.ImageField(upload_to="gallery", null=True)
    vg_img2=models.ImageField(upload_to="gallery", null=True)
    vg_img3=models.ImageField(upload_to="gallery", null=True)
    vg_img4=models.ImageField(upload_to="gallery", null=True)

    vg_dev=models.ForeignKey('Dev', on_delete=models.SET_NULL, null=True)
    vg_pub=models.ForeignKey('Pub', on_delete=models.SET_NULL, null=True)
    vg_rating=models.ForeignKey('Rating', on_delete=models.SET_NULL, null=True)
    vg_plat=models.ForeignKey('Plat', on_delete=models.SET_NULL, null=True)
    
    vg_gen=models.ManyToManyField(Genre)
    vg_tx_lang=models.ManyToManyField(IdiomaTx)
    vg_audio_lang=models.ManyToManyField(IdiomaAu)

    vg_banner=models.ImageField(upload_to="gallery", null=True, blank=True)

    #metodos
    def __str__(self):
        return self.vg_nom

    def get_absolute_url(self):
        return reverse('game:details', args=[str(self.vg_id)])

class VGInstance(models.Model):
    inst_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID para esta unidad')
    inst_vg = models.ForeignKey('VG', on_delete=models.SET_NULL, null=True)
    inst_on_stock = models.BooleanField(null=True)

    class Meta:
        ordering = ['inst_id']

    def __str__(self):
        return f'{self.inst_id} ({self.inst_vg.vg_nom})'


class Dev(models.Model):

    #campos
    dev_nom=models.CharField(max_length=100,help_text="Ingrese Nombre del Desarrollador")

    #metodos
    def __str__(self):
        return self.dev_nom

class Pub(models.Model):
    #campos
    pub_nom=models.CharField(max_length=100,help_text="Ingrese Nombre del Distribuidor")

    #metodos
    def __str__(self):
        return self.pub_nom

class Rating(models.Model):
    #campos
    ratng_desc=models.CharField(max_length=100,help_text="Ingrese Descripcion de la calificacion")

    #metodos
    def __str__(self):
        return self.ratng_desc

class Plat(models.Model):
    #campos
    plat_nom=models.CharField(max_length=100,help_text="Ingrese Nombre de la plataforma")

    #metodos
    def __str__(self):
        return self.plat_nom

class Banner(models.Model):
    __instance = None
    ban_id=models.CharField(max_length=10,help_text="Ingrese ID del Banner",primary_key="True")
    ban_vg=models.ManyToManyField(VG)
    
    def __str__(self):
        return self.ban_id
    