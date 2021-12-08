print('=' * 15, '\033[1;32mDESAFIO 74\033[m', '=' * 15)
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
# print(f'Eu sorteei o valor {n}')
print('OS valores sorteados foram: ', end='')
for n in números:
    print(f'\033[1;33m{n}\033[m ', end='')
print(f'\nO maior valor sorteado foi \033[1;34m{max(números)}\033[m')
print(f'O menor valor sorteado foi \033[1;34m{min(números)}\033[m')
