print('='*15, '\033[1;35mAULA 12 - CONDIÇÃO ANINHADAS\033[m', '='*15)
nome = str(input('Qual é o seu nome? '))
if nome == 'Joaquim' or nome == 'Gustavo':
    print('Que nome \033[1;34m bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem Popular no Brasil.')
elif nome in 'Ana Berta Claudia Jessica Juliana':
    print('Belo nome \033[1;32mFeminino!\033[m')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
