print('-=-'*5, '\033[1;32;40mDESAFIO 006\033[m', '-=-'*5)
from random import randint
computador = randint(0, 10)
jogador = int(input('Em qual número foi? '))
while jogador != computador:
    jogador = int(input('Em qual número foi? '))
    if jogador == computador:
        print('Acertou!!')
    elif jogador < computador:
        print('Mais. Tente mais uma vez.')
    elif jogador > computador:
        print('Menos. Tente mais uma vez')
# print('Acertaste com {} tentativas'.format(cont))
