tab = int(input('Digite um número pra ver Tabuada: '))
for c in range(1, 13):
    mul = tab * c
    print('{} X {:2} = {:3}'.format(tab, c, mul))
