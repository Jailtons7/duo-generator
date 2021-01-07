from django.db import models
from django.contrib.auth.models import User


class Integrante(models.Model):
    SEXOS = (
        ('', 'Selecione'),
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    name = models.CharField(max_length=127, verbose_name="Nome")
    surname = models.CharField(max_length=127, verbose_name="Sobrenome", null=True, blank=True)
    gender = models.CharField(max_length=20, verbose_name="Sexo", choices=SEXOS)
    active = models.BooleanField(verbose_name='Ativo', default=True)

    def __str__(self):
        if self.surname:
            return f'{self.name} {self.surname}'
        return f'{self.name}'

    def get_full_name(self):
        return self.__str__()


class Duplas(models.Model):
    integrante_1 = models.ForeignKey(
        Integrante,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="primeiro_integrante"
    )
    integrante_2 = models.ForeignKey(
        Integrante,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="segundo_integrante"
    )
    date = models.DateField(unique=True, verbose_name="Data")

    def __str__(self):
        return f'{self.integrante_1.name} e {self.integrante_2.name}'
