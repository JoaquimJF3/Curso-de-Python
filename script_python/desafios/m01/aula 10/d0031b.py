print('='*20, 'DESAFIO 31b', '='*20)
distância = float(input('Qual é a distância da sua Viagem: '))
print('Você está prestes a comecar uma Viagem de {}km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45  # Condição Simples
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
