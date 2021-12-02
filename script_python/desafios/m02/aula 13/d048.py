print('='*15, '\033[1;32mDESAFIO 48\033[m', '='*15)
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores solicidados é \033[1;35m{}\033[m'.format(cont, soma))
