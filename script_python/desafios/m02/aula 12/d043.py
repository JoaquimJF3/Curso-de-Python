print('='*15, '\033[1;32mDESAFIO 43\033[m', '='*15)
peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O \033[1;36mIMC\033[m dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está \033[1;33mABAIXO DO PESO!\033[m')
elif 18.5 <= imc < 25:
    print('Parabéns, Você está na faixa de \033[1;32mPESO IDEAL!\033[m')
elif 25 <= imc < 30:
    print('Você está em \033[1;34mSOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('Você está em \033[1;31mOBESIDADE\033[m')
elif imc >= 40:
    print('Você está em \033[1;31mOBESIDADE MÓRBIDA\033[m, Cuidado!')
