from django.contrib import admin
from . models import Genre,IdiomaTx,IdiomaAu,VG,VGInstance,Dev,Pub,Rating,Plat,Banner

# Register your models here.
admin.site.register(Genre)
admin.site.register(IdiomaTx)
admin.site.register(IdiomaAu)
admin.site.register(VG)
admin.site.register(VGInstance)
admin.site.register(Dev)
admin.site.register(Pub)
admin.site.register(Rating)
admin.site.register(Plat)
admin.site.register(Banner)