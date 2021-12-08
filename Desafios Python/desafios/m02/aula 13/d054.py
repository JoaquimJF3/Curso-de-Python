print('=' * 15, '\033[1;32mDESAFIO 54\033[m', '=' * 15)
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        # print('Essa pessoa é MAIOR!!')
    else:
        totmenor += 1
        # print('Essa pessoa é MENOR!!')
print('Ao todo temos {} pessoas \033[1;32mMAIORES de IDADE\033[m'.format(totmaior))
print('E também temos {} pessoas \033[1;32mMENORES de IDADE\033[m'.format(totmenor))
