print('='*20, 'DESAFIO 5', '='*20)
n = int(input('Digite um número: '))
an = n - 1
su = n + 1
print('Analisando o valor \033[1;32m{}\033[m, seu Antecessor é '
      '\033[1;34m{} e o seu Sucessor é {}\033[m!'.format(n, an, su))
