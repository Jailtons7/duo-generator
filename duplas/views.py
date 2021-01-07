# imports from built-in module
from datetime import date

# imports from django
from django.views.generic import ListView
from django.db.utils import IntegrityError
from django.contrib import messages

# imports from third party applications
from workalendar.america import Brazil

# imports from this application
from duplas.models import Duplas, Integrante
from .duo_generator import generate_duos, get_days


class DuplasListView(ListView):
    context_object_name = 'duplas_list'
    template_name = 'duplas/duplas.html'

    def create_duos(self) -> None:
        """ Método usado para alocar cada dupla em um dia útil do mês """
        if self.request.GET.get('novas_duplas'):
            today = date.today()
            duplas = generate_duos()
            dias_mes = get_days(today.month)
            br = Brazil()
            index = 0
            for dia in range(today.day, dias_mes + 1):
                if br.is_working_day(date(today.year, today.month, dia)):
                    # Salve as duplas com o dia da limpeza no banco de dados
                    try:
                        Duplas.objects.create(
                            integrante_1=Integrante.objects.get(id=duplas[index][0]),
                            integrante_2=Integrante.objects.get(id=duplas[index][1]),
                            date=date(today.year, today.month, dia)
                        )
                        index += 1
                    except IndexError:
                        # Se der erro de index volte para o início da tupla com as duplas e redefina o index
                        Duplas.objects.create(
                            integrante_1=Integrante.objects.get(id=duplas[0][0]),
                            integrante_2=Integrante.objects.get(id=duplas[0][1]),
                            date=date(today.year, today.month, dia)
                        )
                        index = 1
                    except IntegrityError:
                        messages.add_message(
                            self.request,
                            messages.INFO,
                            "As duplas deste mês já foram criadas"
                        )
                        break

    def get_queryset(self):
        return Duplas.objects.all().order_by('id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(*kwargs, **kwargs)
        self.request.GET.get('novas_duplas') and self.create_duos()
        context['title'] = 'Duplas do mês'
        return context
