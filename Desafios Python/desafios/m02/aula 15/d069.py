print('='*15, '\033[1;32mDESAFIO 69\033[m', '='*15)
tot18 = totH = totM20 = 0
while True:
    print('-'*25, '\n    CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    print('-'*25)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com Mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} Homens Cadastrados')
print(f'E temos {totM20} Mulheres com Menos de 20 Anos')