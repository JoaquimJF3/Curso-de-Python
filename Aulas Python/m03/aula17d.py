print('=' * 15, '\033[1;35mAULA 17 - Listas[Testes]\033[m', '=' * 15)
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da Lista')
