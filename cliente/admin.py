from django.contrib import admin

# Register your models here.
from . models import Cuenta, Region

admin.site.register(Cuenta)
admin.site.register(Region)
