print('='*15, '\033[1;32mDESAFIO 36\033[m', '='*15)
casa = float(input('Qual é o valor da Casa? R$ '))
salário = float(input('Salário do Comprador? R$ '))
anos = int(input('Quantos anos de Financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print(' a Prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
