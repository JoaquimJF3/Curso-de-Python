n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A Soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' || ')
print('A Divisão Inteira é {} e a Potência é {}'.format(di, e))
