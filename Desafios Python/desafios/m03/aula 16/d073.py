print('=' * 15, '\033[1;32mDESAFIO 73\033[m', '=' * 15)
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 136)
print(f'Lista de Times: {times}')
print('-=' * 136)
print(f'Os 5 Primeiros Colocados são: {times[0:5]}')
print('-='* 45)
print(f'Os 4 Últimos Colocados são: {times[-4:]}')
print('-='* 45)
print(f'Times em Ordem Alfabética: {sorted(times)}')
print('-=' * 136)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')