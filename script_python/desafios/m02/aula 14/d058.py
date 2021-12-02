print('=' * 15, '\033[1;32mDESAFIO 58\033[m', '=' * 15)
from random import randint
from time import sleep
computador = randint(0, 10)
print('Sou seu Computador... \nAcabei de pensar em um número entre 0 e 10.'
      '\nSerá que você consegue adivinhar qual foi?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpite += 1
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais. tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} Tentativas!! Parabéns!'.format(palpite))
