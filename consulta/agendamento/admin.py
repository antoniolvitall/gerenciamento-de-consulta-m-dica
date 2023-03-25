from agendamento.models import Consulta, Profissional
from django.contrib import admin


class Profissionais(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nomesocial','cns', 'CARGO')
    list_display_links = ('id', 'nomesocial')
    search_fields = ('nomesocial',)
    list_per_page = 10

admin.site.register(Profissional, Profissionais)

class Consultas(admin.ModelAdmin):
    list_display = ('data_consulta')