print('=' * 15, '\033[1;32mDESAFIO 55\033[m', '=' * 15)
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR Peso lido foi de {}Kg'.format(maior))
print('O MENOR Peso lido foi de {}Kg'.format(menor))
