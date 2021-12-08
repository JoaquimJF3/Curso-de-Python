print('='*20, ' DESAFIO 10', '='*20)
real = float(input('Quanto Dinheiro você têm na Carteira? R$'))
dolar = real / 3.27
print('Com \033[1;32mR${:.2f}\033[m você pode comprar \033[1;32mUS${:.2f}\033[m'.format(real, dolar))
