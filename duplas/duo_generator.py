from datetime import date

from workalendar.america import Brazil

from duplas.models import Profile, Duplas

MESES_30 = [4, 6, 9, 11]
MESES_31 = [1, 3, 5, 7, 8, 10, 12]


def get_dias(data):
    mes = data.month
    if mes in MESES_30:
        dias = 30
    elif mes in MESES_31:
        dias = 31
    else:
        dias = 28
    return dias


def gerar_duplas():
    perfis = Profile.objects.filter(user__is_active=True)
    today = date.today()
    dia_hoje = today.day
    ultimo_dia = get_dias(data=today)
    for dia in range(dia_hoje, ultimo_dia + 1):
        data_ = date(today.year, today.month, dia)
        br = Brazil()
        if br.is_working_day(data_):
            """ Gerar as duplas aqui """
            Duplas.objects.create(
                integrante_1=dupla['integrante_1'],
                integrante_2=dupla['integrante_2'],
                data=data_
            )
