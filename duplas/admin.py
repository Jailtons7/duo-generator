from django.contrib import admin
from duplas.models import Members


@admin.register(Members)
class IntegranteAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'gender', 'active')
    list_display = fields
