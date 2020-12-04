from django.views.generic import ListView
from django.shortcuts import render
from duplas.models import Duplas
from .duo_generator import gerar_duplas


class DuplasListView(ListView):
    model = Duplas
    template_name = 'duplas/duplas.html'

    def get(self, request, *args, **kwargs):
        novas_duplas = request.GET.get('novas_duplas')
        if novas_duplas:
            gerar_duplas()
        return render(request, self.template_name)
