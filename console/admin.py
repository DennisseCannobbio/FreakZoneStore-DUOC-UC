from django.contrib import admin
from .models import Conn , CS , CSInstance, Plat
# Register your models here.

admin.site.register(Conn)
admin.site.register(CS)
admin.site.register(CSInstance)
admin.site.register(Plat)