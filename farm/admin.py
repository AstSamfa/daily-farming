from django.contrib import admin

from farm.models import Cultivo, Requisito, Cuidado, ColeccionCultivo

admin.site.register(Requisito)
admin.site.register(Cuidado)
admin.site.register(Cultivo)
admin.site.register(ColeccionCultivo)
