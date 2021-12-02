print('='*20, 'DESAFIO 7', '='*20)
n1 = float(input('Primeira Nota do Aluno: '))
n2 = float(input('Segunda Nota do Aluno: '))
m = (n1+n2) / 2
print('A média entre \033[1;35m{:.1f} e {:.1f} é igual a {:.1f}\033[m'.format(n1, n2, m))
