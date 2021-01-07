from django.contrib import admin
from duplas.models import Integrante


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'gender', 'active')
    list_display = fields
