from django.contrib import admin
from .models import Mimodelo, Gato

# Register your models here.

class MimodeloAdmin(admin.ModelAdmin):
    list_display= (
        "nombre",
        "forma",
        "relleno",
        "ingredientes",
        "precio",
        "color",
    )

class GatoAdmin(admin.ModelAdmin):
    list_display= (

        "id",
        "raza",
        "color",
        "tamanio",
    )

    sortable_by = ('id',)
    search_fields = ('color', 'raza')
    list_filter = ('tamanio', 'color')
    list_per_page = 10




admin.site.register(Mimodelo, MimodeloAdmin)
admin.site.register(Gato, GatoAdmin)