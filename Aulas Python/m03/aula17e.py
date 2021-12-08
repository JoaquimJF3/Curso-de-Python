print('=' * 15, '\033[1;35mAULA 17 - Listas[Testes]\033[m', '=' * 15)
a = [2, 3, 4, 7]
# b = a   Fazendo ligação entre lista
b = a[:]  # Criando uma cópia do A dentro do B
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
