import random
import logging
from datetime import date

from workalendar.america import Brazil

from duplas.models import Profile, Duplas

MONTHS_30 = [4, 6, 9, 11]
MONTHS_31 = [1, 3, 5, 7, 8, 10, 12]


def get_days(month: int) -> int:
    """
    Retorna a quantidade de dias no mês conforme a data.
    Posteriormente será necessário considerar anos bissextos.
    """
    if month in MONTHS_30:
        return 30
    elif month in MONTHS_31:
        return 31
    elif month == 2:
        return 28
    else:
        logging.error(f'{month} is an invalid month')
        return 0


def generate_duos() -> tuple:
    """
    Função usada para criar as duplas do mês.
    As duplas são formadas aleatoriamente com os perfis ativos (preferencialmente 1 homem + 1 mulher).
    """
    m_profiles = Profile.objects.filter(user__is_active=True, sexo='M')
    f_profiles = Profile.objects.filter(user__is_active=True, sexo='F')

    m_random = random.choices(m_profiles.values_list('user_id', flat=True), k=m_profiles.count())
    f_random = random.choices(f_profiles.values_list('user_id', flat=True), k=f_profiles.count())

    perfis = m_random + f_random

    duplas = ()
    for index in range((len(perfis) + 1) // 2):
        duplas += ((perfis[index], perfis[-index-1]),)

    return duplas
