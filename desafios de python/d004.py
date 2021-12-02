print('-=-'*5, '\033[1;32;40mDESAFIO 004\033[m', '-=-'*5)
n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O Dobro de {} é {}.'.format(n, dobro))
print('O Triplo de {} é {}.'.format(n, triplo))
print('A Raiz Quadrada de {} é igual a {:.2f}!'.format(n, raiz))
