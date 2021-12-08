print('=' * 15, '\033[1;35mAULA 16 - Tuplas[Testes]\033[m', '=' * 15)
# Tuplas são IMUTÁVEIS
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in lanche:  # Modo Fácil e Rápido (Clássico)
    print(f'Eu vou Comer {comida} ')
for cont in range(0, len(lanche)):  # Mostrando a posição dos elementos
    print(f'Eu vou Comer {lanche[cont]} na posição {cont}')
'''lanche[1] = 'Refrigerante' -> Erro
print(lanche)
print(len(lanche))'''
for pos, comida in enumerate(lanche):  # Posição dos elementos e usando duas variaveis
    print(f'Eu vou Comer {comida} na posição {pos}')
print('Comi pra Caramba!')
