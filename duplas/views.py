from django.views.generic import ListView
from duplas.models import Duplas


class DuplasListView(ListView):
    model = Duplas
    template_name = 'duplas/duplas.html'
