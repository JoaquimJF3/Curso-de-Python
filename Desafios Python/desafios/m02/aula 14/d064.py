print('=' * 15, '\033[1;32mDESAFIO 64\033[m', '=' * 15)
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a Soma entre eles foi {}.'.format(cont, soma))
