print('=' * 15, '\033[1;32mDESAFIO 56\033[m', '=' * 15)
somaidade = 0
médiaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('A média de Idade do grupo é de {} anos.'.format(médiaidade))
print('O HOMEM mais Velho têm {} anos e se chama {}.'.format(maioridadeh, nomevelho))
print('Ao todo são {} MULHERES com Menos de 20 anos.'.format(totmulher20))
