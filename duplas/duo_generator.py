import random
from datetime import date

from workalendar.america import Brazil

from duplas.models import Profile, Duplas

MESES_30 = [4, 6, 9, 11]
MESES_31 = [1, 3, 5, 7, 8, 10, 12]


def get_dias(data: date) -> int:
    """
    Retorna a quantidade de dias no mês conforme a data.
    Posteriormente será necessário considerar anos bissextos.
    """
    mes = data.month
    if mes in MESES_30:
        return 30
    elif mes in MESES_31:
        return 31
    else:
        return 28


def gerar_duplas() -> None:
    """
    Função usada para salvar as duplas no banco de dados.
    As duplas são criadas aleatoriamente com os perfis ativos.
    """
    perfis_m = Profile.objects.filter(user__is_active=True, sexo='M')
    random_perfis_m = set(random.choices(perfis_m.values_list('user_id', flat=True), k=perfis_m.count()))
    perfis_f = Profile.objects.filter(user__is_active=True, sexo='F')
    random_perfis_f = set(random.choices(perfis_f.values_list('user_id', flat=True), k=perfis_f.count()))
    perfis_aleatorios = random_perfis_m.update(random_perfis_f)

    for _ in range(len(perfis)):
        pks = perfis.values_list('user_id', flat=True)
        if pks:
            pk_1 = random.choices(pks)
            del pks[pks.index(pk_1)]
            perfis = perfis.exclude(user_id=pk_1)
            if pks:
                pk_2 = random.choices(pks)
                del pks[pks.index(pk_2)]
                perfis = perfis.exclude(user_id=pk_2)


    today = date.today()
    dia_hoje = today.day
    ultimo_dia = get_dias(data=today)
    for dia in range(dia_hoje, ultimo_dia + 1):
        data_ = date(today.year, today.month, dia)
        br = Brazil()
        if br.is_working_day(data_):

            integrante_1 = perfis.get(user_id=pk_1)
            Duplas.objects.create(
                integrante_1=dupla['integrante_1'],
                integrante_2=dupla['integrante_2'],
                data=data_
            )
