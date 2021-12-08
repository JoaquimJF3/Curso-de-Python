print('=' * 15, '\033[1;32mDESAFIO 60\033[m', '=' * 15)
from math import factorial
n = int(input('Digite um número para Calcular seu Fatorial: '))
f = factorial(n)
print('O Fatorial de {} é {}.'.format(n, f))
