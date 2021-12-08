print('='*15, '\033[1;32mDESAFIO 52\033[m', '='*15)
num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1,):
    if num % c == 0:
        print('\033[1;33m', end=' ')
        tot += 1
    else:
        print('\033[1;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!!')
