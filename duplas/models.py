from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    SEXOS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    sexo = models.CharField(max_length=22, choices=SEXOS)


class Duplas(models.Model):
    integrante_1 = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="primeiro_integrante"
    )
    integrante_2 = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="segundo_integrante"
    )
    data = models.DateField()

    def __str__(self):
        return f'{self.integrante_1.name} e {self.integrante_2.name}'
