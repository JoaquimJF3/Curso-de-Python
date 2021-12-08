print('=' * 15, '\033[1;32mDESAFIO 67\033[m', '=' * 15)
while True:
    n = int(input('Quer ver a Tabuada de qual valor: '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADA. Volte Sempre!!')
