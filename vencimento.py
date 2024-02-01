from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

valor_total = float(input('Digite o valor do empréstimo: R$ '))
delta_tempo = int(input('Digite em quantos meses irá quitar o empréstimo: '))
quantidade_parcelas = 1

vencimento = datetime.now()

while quantidade_parcelas <= delta_tempo:
    vencimento += relativedelta(months=+1)
    print(f'Parcela: {quantidade_parcelas} = Valor R$ {valor_total / delta_tempo:,.2f} com vencimento {vencimento.strftime('%d/%m/%Y')}.')
    quantidade_parcelas += 1