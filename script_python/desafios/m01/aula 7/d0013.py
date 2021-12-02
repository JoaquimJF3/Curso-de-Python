print('='*20, 'DESAFIO 13', '='*20)
sal = float(input('Qual é o salário do Funcionário R$: '))
novsal = sal + (sal * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, '
      'passa a receber R${:.2f}'.format(sal, novsal))
