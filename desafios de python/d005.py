print('-=-'*5, '\033[1;32;40mDESAFIO 005\033[m', '-=-'*5)
nota1 = float(input('Primeira Nota do Aluno: '))
nota2 = float(input('Segunda Nota do Aluno: '))
média = (nota1 + nota2) / 2
print('A sua média foi {}'.format(média))
if média >= 8.5:
    print('PARABÉNS!!')
elif média <= 6.5 and média == 7:
    print('RECUPERAÇÃO!')
elif média == 5:
    print('REPROVADO!')