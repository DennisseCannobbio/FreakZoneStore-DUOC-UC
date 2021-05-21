from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Cuenta,Region


class FormUser(UserCreationForm): #formulario para User

    username = forms.CharField(label='Nombre de Usuario',required = True,
            widget=forms.TextInput(
                    attrs={
                        "placeholder":"Introduzca su nombre de usuario",
                        "size":25
                    }

                )
            )
    email = forms.CharField(label='E-mail',required = True,
            widget=forms.TextInput(
                    attrs={
                        "placeholder":"Introduzca su E-mail"
                    }

                )
            )
    first_name = forms.CharField(label='Nombre',required = True,
            widget=forms.TextInput(
                    attrs={
                        "placeholder":"Introduzca su nombre"
                    }

                )
            )
    last_name = forms.CharField(label='Apellido',required = True,
            widget=forms.TextInput(
                    attrs={
                        "placeholder":"Introduzca su apellido"
                    }

                )
            )
    password1 =forms.CharField(label='Contraseña',required=True ,
                    widget=forms.PasswordInput(
                            attrs={
                                "minlength":8,
                                "placeholder":"Mínimo 8 Carácteres"
                            }
                        )
                    )
    password2 =forms.CharField(label='Contraseña (Conifrmacion)',required=True ,
                    widget=forms.PasswordInput(
                            attrs={
                                "minlength":8,
                                "placeholder":"Mínimo 8 Carácteres"
                            }
                        )
                    )


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

    def clean_password_val(self): # funcion para verificar contraseña
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ClienteCreateForm(forms.ModelForm): #formulario para cliente

    cuent_rut = forms.CharField(label='RUT',required=True ,
            widget=forms.TextInput(
                    attrs={
                        "minlength":7,
                        "maxlength":9,
                        "placeholder":"XXXXXXXXX-X"
                    }
            )
        )
    cuent_fecnac =forms.DateField(label='Fecha de nacimiento',required=True ,
                    widget=forms.DateInput(
                            attrs={
                                "type":"date",
                                "placeholder":"aaaa-mm-dd"
                            }
                        )
                    )
    desp_telef =forms.IntegerField(label='Telefono',required=True ,
                    widget=forms.TextInput(
                            attrs={
                                "maxlength":10,
                                "placeholder":"Máximo 10 caracteres"
                            }
                        )
                    )
    desp_region =forms.ModelChoiceField(queryset=Region.objects.all(),label='Region',required=True)
    com_nombre =forms.CharField(label='Comuna',required=True ,
                    widget=forms.TextInput(
                            attrs={
                                "placeholder":"Introdusca su comuna"
                            }
                        )
                    )
    desp_direccion =forms.CharField(label='Direccion',required=True ,
                    widget=forms.TextInput(
                            attrs={
                                "size":100,
                                "placeholder":"Introduzca su direccion"
                            }
                        )
                    )

    class Meta:
        model = Cuenta
        fields = [
            'cuent_rut',
            'cuent_fecnac',
            'desp_telef',
            'desp_region',
            'com_nombre',
            'desp_direccion'
        ]

# class ClienteCreateForm(forms.ModelForm):
#     cuent_rut =forms.CharField(label='RUT',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "minlength":7,
#                                 "maxlength":9,
#                                 "placeholder":"XXXXXXXXX-X"
#                             }
#                     )
#                 )
#     cuent_nombre =forms.CharField(label='Nombre',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "maxlength":25,
#                                 "placeholder":"Nombre"
#                             }
#                         )
#                     )
#     cuent_email =forms.CharField(label='E-Mail',required=True ,
#                     widget=forms.EmailInput(
#                             attrs={
#                                 "minlength":5,
#                                 "placeholder":"alguien@example.com"
#                             }
#                         )
#                     )
#     cuent_pass =forms.CharField(label='Contraseña',required=True ,
#                     widget=forms.PasswordInput(
#                             attrs={
#                                 "minlength":8,
#                                 "placeholder":"Minimo 8 Caracteres"
#                             }
#                         )
#                     )
#     cuent_ape =forms.CharField(label='Apellido',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "maxlength":25,
#                                 "placeholder":"Apellido"
#                             }
#                         )
#                     )
#     cuent_fecnac =forms.DateField(label='Fecha de nacimiento',required=True ,
#                     widget=forms.DateInput(
#                             attrs={
#                                 "type":"date",
#                                 "placeholder":"aaaa-mm-dd"
#                             }
#                         )
#                     )
#     desp_telef =forms.IntegerField(label='Telefono',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "maxlength":15,
#                                 "placeholder":"Maximo 15 Caracteres"
#                             }
#                         )
#                     )
#     desp_region =forms.ModelChoiceField(queryset=Region.objects.all(),
#                     label='Region',required=True)

#     com_nombre =forms.CharField(label='Comuna',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "placeholder":"Su Comuna"
#                             }
#                         )
#                     )
#     desp_direccion =forms.CharField(label='Direccion',required=True ,
#                     widget=forms.TextInput(
#                             attrs={
#                                 "size":50,
#                                 "placeholder":"Su direccion"
#                             }
#                         )
#                     )
#     class Meta:
#         model = Cuenta
#         fields = [
#             'cuent_rut',
#             'cuent_pass',
#             'cuent_nombre',
#             'cuent_ape',
#             'cuent_fecnac',
#             'cuent_email',
#             'desp_telef',
#             'desp_region',
#             'com_nombre',
#             'desp_direccion'
#         ]