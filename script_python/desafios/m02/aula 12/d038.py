print('='*15, '\033[1;32mDESAFIO 38\033[m', '='*15)
p1 = int(input('Primeiro Número: '))
p2 = int(input('Segundo Número: '))
if p1 > p2:
    print('O PRIMEIRO valor é \033[1;36mMaior\033[m')
elif p2 > p1:
    print('O SEGUNDO valor é \033[1;36mMaior\033[m')
else:
    print('Os dois VALORES são \033[1;36mIGUAIS\033[m.')
