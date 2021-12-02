print('=' * 20, 'DESAFIO 31', '=' * 20)
distância = float(input('Qual é a distância da sua Viagem: '))
print('Você está prestes a comecar uma Viagem de {}km.'.format(distância))
if distância <= 200:  # Condição Composta
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
