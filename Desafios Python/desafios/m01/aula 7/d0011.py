print('='*20, 'DESAFIO 11', '='*20)
lar = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
area = lar * alt
print('Sua parede tem a dimensão de \033[1;33m{}x{}\033[m e a sua área é de '
      '\033[1;33m{:.2f}m\033[m.'.format(lar, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de \033[1;33m{:.2f}l\033[m de tinta.'.format(tinta))
