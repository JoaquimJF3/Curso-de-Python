print('='*15, '\033[1;32mDESAFIO 39\033[m', '='*15)
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se Alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o Alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} anos'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se Alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))
