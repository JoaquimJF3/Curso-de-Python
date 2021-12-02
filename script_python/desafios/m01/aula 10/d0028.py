print('=' * 20, 'DESAFIO 28', '=' * 20)
print('-=-' * 30)
from random import randint
from time import sleep
computador = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 30)
jogador = int(input('Qual é o número que Pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABÉNS! Você Conseguiu me Vencer!')
else:
    print('GANHEI! Eu pensei no número \033[1;32m{}\033[m '
          'e não no \033[1;34m{}\033[m!'.format(computador, jogador))
