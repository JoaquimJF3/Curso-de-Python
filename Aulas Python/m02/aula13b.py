print('='*15, '\033[1;35mAULA 13 - ESTRUTURA DE REPETIÇÃO[For]\033[m', '='*15)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM...')

# # # # # # # # # # # # # # #

s = 0
for nt in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
