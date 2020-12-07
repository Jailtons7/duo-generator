from datetime import date

from django.views.generic import ListView
from django.shortcuts import render
from duplas.models import Duplas
from .duo_generator import generate_duos, get_days
from workalendar.america import Brazil


class DuplasListView(ListView):
    model = Duplas
    template_name = 'duplas/duplas.html'

    def get(self, request, *args, **kwargs):
        novas_duplas = request.GET.get('novas_duplas')
        if novas_duplas:
            today = date.today()
            duplas = generate_duos()
            dias_mes = get_days(today.month)
            br = Brazil()
            for dia in range(today.day, dias_mes + 1):
                if br.is_working_day(today.year, today.month, dia):
                    """ Salvar as duplas no dia da limpeza no banco de dados """
                pass
        return render(request, self.template_name)
