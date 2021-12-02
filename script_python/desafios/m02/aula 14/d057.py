print('=' * 15, '\033[1;32mDESAFIO 57\033[m', '=' * 15)
sexo = str(input('informe o seu Sexo [F/M]: ')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados ínvalidos. Por Favor, informe seu Sexo: ')).upper()[0].strip()
print('Sexo {} registrado com Sucesso'.format(sexo))
