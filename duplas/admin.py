from django.contrib import admin
from duplas.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'sexo')
    list_display = ('user', 'sexo')
