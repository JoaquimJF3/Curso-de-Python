print('='*15, '\033[1;32mDESAFIO 50\033[m', '='*15)
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números PARES e a Soma foi {}'.format(cont, soma))
