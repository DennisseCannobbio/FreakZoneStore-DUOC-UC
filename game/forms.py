from django import forms

from .models import VG,Dev,Genre,IdiomaAu,IdiomaTx,Plat,Pub,Rating

class VGCreateForm(forms.ModelForm):
    vg_id = forms.CharField(label="ID", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese la id del videojuego",
                            "minlength":3
                        }
                )   
            )
    vg_nom = forms.CharField(label="Nombre Producto", required=True,
                widget=forms.TextInput(
                        attrs={
                            "placeholder":"Ingrese el nombre del videojuego",
                            "minlength":5
                        }
                )   
            )
    vg_price = forms.IntegerField(label="Precio", required =True,
                    widget=forms.NumberInput(
                        attrs={
                            "placeholder":"Precio Videojuego"
                        }
                    )
                )
    vg_descr = forms.CharField(label="Descripcion", required=True,
                widget=forms.Textarea(
                        attrs={
                            "placeholder":"Ingrese el nombre del videojuego",
                            "minlength":5,
                            "maxlength":3000
                        }
                )   
            )
    vg_prev = forms.BooleanField(label="Preventa", required=False)
    vg_online = forms.BooleanField(label="Multijugador Online", required=False)
    vg_online_plyr = forms.IntegerField(label="Jugadores Online", required =True,
                    widget=forms.NumberInput(
                        attrs={
                            "placeholder":"Numero de jugadores Online"
                        }
                    )
                )
    vg_local_plyr = forms.IntegerField(label="Jugadores Locales", required =True,
                    widget=forms.NumberInput(
                        attrs={
                            "placeholder":"Numero de jugadores Local"
                        }
                    )
                )

    vg_dev = forms.ModelChoiceField(queryset=Dev.objects.all(),label="Desarrolladora",required=True)
    vg_pub = forms.ModelChoiceField(queryset=Pub.objects.all(),label="Distribuidora",required=True)
    vg_rating = forms.ModelChoiceField(queryset=Rating.objects.all(),label="Rating Edad",required=True)
    vg_plat = forms.ModelChoiceField(queryset=Plat.objects.all(),label="Plataforma",required=True)
    
    vg_gen = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),label="Plataforma",required=True)
    vg_tx_lang = forms.ModelMultipleChoiceField(queryset=IdiomaTx.objects.all(),label="Idiomas Texto",required=True)
    vg_audio_lang = forms.ModelMultipleChoiceField(queryset=IdiomaAu.objects.all(),label="Idioma Audio",required=True)
    
    vg_main_img = forms.ImageField(label="Imagen principal")
    vg_img2 = forms.ImageField(label="Imagen secundaria")
    vg_img3 = forms.ImageField(label="Imagen secundaria")
    vg_img4 = forms.ImageField(label="Imagen secundaria")
    class Meta:
        model = VG
        fields =[
            'vg_id',
            'vg_nom',
            'vg_price',
            'vg_descr',
            'vg_prev',
            'vg_online',
            'vg_online_plyr',
            'vg_local_plyr',
            'vg_dev',
            'vg_pub',
            'vg_rating',
            'vg_plat',
            'vg_gen',
            'vg_tx_lang',
            'vg_audio_lang',
            'vg_main_img',
            'vg_img2',
            'vg_img3',
            'vg_img4'
        ]