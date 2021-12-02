print('='*15, '\033[1;32mDESAFIO 44\033[m', '='*15)
print('='*15, '\033[7;34mLOJAS FERNANDES\033[m', '='*15)
preço = float(input('Preço das Compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/CHEQUE
[ 2 ] à vista CARTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x ou mais no CARTÃO''')
opção = int(input('Qual é a Opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua Compra será Parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua Compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA DE PAGAMENTO\033[m. Tente Novamente')
print('Sua Compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
