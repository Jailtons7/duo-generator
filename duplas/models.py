from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    SEXOS = (
        ('M', 'Male'),
        ('F', 'Female'),
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


class Duos(models.Model):
    member_1 = models.ForeignKey(
        Members,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="first_member"
    )
    member_2 = models.ForeignKey(
        Members,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="second_member"
    )
    date = models.DateField(unique=True, verbose_name="Data")

    def __str__(self):
        return f'{self.member_1.name} e {self.member_2.name}'
