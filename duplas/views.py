from datetime import date

from django.views.generic import ListView
from django.shortcuts import render
from duplas.models import Duplas, Profile
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
            index = 0
            for dia in range(today.day, dias_mes + 1):
                if br.is_working_day(date(today.year, today.month, dia)):
                    # Salva as duplas com o dia da limpeza no banco de dados
                    try:
                        Duplas.objects.create(
                            integrante_1=Profile.objects.get(pk=duplas[index][0]),
                            integrante_2=Profile.objects.get(pk=duplas[index][1]),
                            data=date(today.year, today.month, dia)
                        )
                        index += 1
                    except IndexError:
                        # Se der erro de index volta para o início da tupla com as duplas
                        index = 0
        return render(request, self.template_name)
