from django.contrib import admin
from .models import *

class ListandoHospitais(admin.ModelAdmin):
    list_display = ("cnes", "nome", "uf", "categoria")
    ordering = ["nome",]
    search_fields = ("nome",)
    list_filter = ("categoria", "uf")
    list_per_page = 10

class ListandoAvaliacoes(admin.ModelAdmin):
    list_display = ("hospital", "risco", "duracao", "avaliacao", "data")
    ordering = ["-data",]
    list_filter = ("risco",)
    list_per_page = 10

class ListandoDados(admin.ModelAdmin):
    list_display = ("usuario",)
    list_per_page = 10

admin.site.register(Hospital, ListandoHospitais)
admin.site.register(Avaliacao, ListandoAvaliacoes)
admin.site.register(Dados, ListandoDados)
admin.site.register(Doencas)
admin.site.register(Sintomas)
admin.site.register(Diagnostico)
admin.site.register(Cirurgia)
admin.site.register(Internacao)
admin.site.register(Condicao_familiar)
admin.site.register(Medicamento)