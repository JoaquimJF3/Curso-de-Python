print('='*20, ' DESAFIO 8', '='*20)
m = float(input('Uma distância em Metros: '))
cm = m * 100
mm = m * 1000
print('A médida de \033[7;30m{}m corresponde a {}cm e {:.0f}mm\033[m'.format(m, cm, mm))
