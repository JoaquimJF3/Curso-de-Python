print('=' * 15, '\033[1;32mDESAFIO 59\033[m', '=' * 15)
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opção = int(input('>>>>> Qual é a sua opção: '))
    if opção == 1:
        r = n1 + n2
        print('A soma entre \033[1;34m{}\033[m + \033[1;34m{}\033[m '
              'é igual a \033[1;34m{}\033[m'.format(n1, n2, r))
    elif opção == 2:
        r = n1 * n2
        print('A Multiplicação entre \033[1;34m{}\033[m x \033[1;34m{}\033[m '
              'é igual a \033[1;34m{}\033[m'.format(n1, n2, r))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre \033[1;34m{}\033[m e \033[1;34m{}\033[m '
              'o maior valor é \033[1;34m{}\033[m'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('\033[1;33mFinalizando...\033[m')
    else:
        print('Opção inválida. Tente novamente')
    print('=-='*15)
    sleep(1.5)
print('Fim do Programa! Volte Sempre!')
