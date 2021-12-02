print('='*20, 'DESAFIO 32', '='*20)
from datetime import date
ano_atual = int(input('Que ano quer analisar? Coloque 0 para analisar o Ano Atual: '))
if ano_atual == 0:
    ano_atual = date.today().year
if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano_atual))
else:
    print('O ano {} não é BISSEXTO'.format(ano_atual))
