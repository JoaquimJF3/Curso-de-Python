print('='*20, 'DESAFIO 29', '='*20)
velocidade = float(input('Qual é a Velocidade atual do seu Veiculo: '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um Bom Dia! Dirija com Segurança Senhor!')