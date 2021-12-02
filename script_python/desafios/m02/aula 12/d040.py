print('='*20, '\033[1;32mDESAFIO 40\033[m', '='*20)
nota1 = float(input('Digite a primeira Nota: '))
nota2 = float(input('Digite a segunda Nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O Aluno está em RECUPERAÇÃO!')
elif média < 5:
    print('Você está REPROVADO')
elif média >= 7:
    print('VocÊ está APROVADO!')
