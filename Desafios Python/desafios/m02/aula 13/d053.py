print('=' * 15, '\033[1;32mDESAFIO 53\033[m', '=' * 15)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
''' for letra in range(len(junto) -1, -1, -1):
   inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase não é um PALÍNDROMO!')
# print('Você digitou a frase {}'.format(junto))
