print('='*15, '\033[1;32mDESAFIO 49\033[m', '='*15)
# TABUADA v.2.0
tab = int(input('Digite um número para ver sua Tabuada: '))
for c in range(1, 13):
    re = tab * c
    print('{} x {:2} = {:3}'.format(tab, c, re))
