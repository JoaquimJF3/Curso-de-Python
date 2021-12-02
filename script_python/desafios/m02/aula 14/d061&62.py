print('=' * 15, '\033[1;32mDESAFIO 61 & 62\033[m', '=' * 15)
print('Gerador de PA')
print('-='*20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão  finalizadas com \033[1;32m{}\033[m termos mostrados.'.format(total))
