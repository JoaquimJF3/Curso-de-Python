print('='*15, '\033[1;32mDESAFIO 51\033[m', '='*15)
print('='*35)
print('      10 TERMOS DE UMA PA')
print('='*35)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end=' -> ')
print('\033[1;31mACABOU!!\033[m')
