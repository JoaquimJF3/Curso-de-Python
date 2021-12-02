print('='*15, '\033[1;34mMenu\033[m', '='*15)
from time import sleep
cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'verde': '\033[1;32m',
         'amarelo': '\033[1;33m',
         'magenta': '\033[1;35m',
         'vermelho': '\033[1;31m',
         'pretoebranco': '\033[7;30m'}
nome1 = str(input('Como se Chamas: '))
print('É um prazer em Conhecer você, Senhor {}?'.format(nome1))
op = 0
while op != 5:
    print('''======= {}Menu Principal{} ====== \n[ 1 ] Calculos Matemáticos\n[ 2 ] Quiz Otaku\n[ 3 ] Quiz Programador\n[ 4 ] Mini Jogo de Adivinha\n[ 5 ] Pra Sair...'''.format(cores[             'azul'], cores['limpa'])) # Menu Principal
    op = int(input('Oque desejas fazer: '.format(cores['azul'], cores['limpa'])))
    if op == 1:
        print('''===== {}Calculos Matemáticos{} ===== \n[ 1 ] Calcular o Dobro de um Número\n[ 2 ] calcular o Triplo de um Número\n[ 3 ] Calcular Raiz Quadrada
        \n[ 4 ] Verificar a Média de um Aluno\n[ 5 ] Voltar pro Menu Principal'''.format(cores['azul'], cores['limpa'])) # Menu 1
        nome2 = str(input('Digite o seu Nome: '))
        cm = int(input('Que Operação desejas fazer {}: '.format(nome2)))
        if cm == 1:
            print('{}Calculando o DOBRO do Valor{}'.format(cores['verde'], cores['limpa']))
            n = int(input('Digite um Valor: '))
            d = n * 2
            sleep(1)
            print('O Dobro de {} é {}'.format(n, d))
        elif cm == 2:
            print('{}Calculando o TRIPLO do Valor{}'.format(cores['verde'], cores['limpa']))
            n = int(input('Digite um Valor: '))
            t = n * 3
            sleep(1)
            print('O Triplo de {} é {}'.format(n, t))
        elif cm == 3:
            print('{}Calculando a Raiz Quadrada do Valor{}'.format(cores['verde'], cores['limpa']))
            n = int(input('Digite um Valor: '))
            r = n ** (1/2)
            sleep(1)
            print('A Raiz Quadrada de {} é {:.2f}'.format(n, r))
        elif cm == 4:
            print('{}Calculando a Média do Aluno{}'.format(cores['verde'], cores['limpa']))
            n1 = float(input('Digite a primeira Nota: '))
            n2 = float(input('Digite a segunda Nota: '))
            m = (n1 + n2) / 2
            sleep(1)
            if 7 > m >= 5:
                print('A sua média é {}, contudo estás em RECUPERAÇÃO!'.format(m))
            elif m < 5:
                print('A sua média é {}, contudo estás REPROVADO!'.format(m))
            elif m >= 7:
                print('A sua média é {}, contudo estás APROVADO!'.format(m))
            print('========== {}TERMINOU A SUA VERIFICAÇÃO{} =========='.format(cores['azul'], cores['limpa']))
        elif cm == 5:
            print('Finalizando...')
        # Fim do Menu 1
    elif op == 2:
        qt = 0
        while qt != 9:
            print('''========== {}Quiz Otaku{} ==========\n[ 1 ] Naruto\n[ 2 ] One Piece\n[ 3 ] Dragon Ball\n[ 9 ] Pra Sair...'''.format(cores['azul'], cores['limpa'])) # Menu 2
            qt = int(input('Qual Quiz desejas fazer: '))
            if qt == 1:
                print('{}BEM-VINDO AO QUIZ SOU NARUTINHO{}'.format(cores['amarelo'], cores['limpa']))
                sleep(1)
                print('''1ª- Quem é o Pai de Naruto Uzumaki?\n[ 1 ] Sarutobi Hiruzen\n[ 2 ] Minato Namikaze\n[ 3 ] Jiraiya-Sama\n[ 4 ] Iruka Sensei''')
                rp1 = int(input('R: '))
                sleep(1)
                if rp1 == 2:
                    print('Parabéns Acertaste!')
                else:
                    print('Falaste como NARUTINHO. *_*')
                sleep(1)
                print('''2ª- Qual é o nome da Bijuu de Naruto Uzumaki\n[ 1 ] Matatabi\n[ 2 ] Chukaku\n[ 3 ] Kurama\n[ 4 ] Ichobu''')
                rp2 = int(input('R: '))
                sleep(1)
                if rp2 == 3:
                    print('Acertaste, Parabéns!')
                else:
                    print('Falaste como NARUTINHO. ;(')
            elif qt == 2:
                print('{}BEM-VINDO AO QUIZ DE ONE PIECE{}'.format(cores['amarelo'], cores['limpa']))
                sleep(1)
                print('''1ª- Quem é o Pai de Monkey D. Luffy?\n[ 1 ] Monkey D. Garp\n[ 2 ] Portgas D. Ace\n[ 3 ] Silver Rayleigh\n[ 4 ] Monkey D. Dragon\n[ 5 ] Gold D. Roger''')
                rp1 = int(input('R: '))
                sleep(1)
                if rp1 == 4:
                    print('Acertaste Pirata!')
                else:
                    print('Pirata Morto!')
                sleep(1)
                print('''2ª- Quem foi o Primeiro Membro do {}Bando dos CHAPÉUS DE PALHA{}?\n[ 1 ] Vinsmoke Sanji\n[ 2 ] Tony Tony Chopper\n[ 3 ] Roronoa Zoro\n[ 4 ] Nami\n[ 5 ] Nico Robin'''.format(cores['magenta'], cores['limpa']))
                rp2 = int(input('R: '))
                sleep(1)
                if rp2 == 3:
                    print('Acertaste Pirata\n'
                          'Roronoa Zoro Caçador de Pirata e Melhor Espadachim do Mundo')
                else:
                    print('Morto pela Santoryu de Roronoa Zoro!')
            elif qt == 3:
                print('{}BEM-VINDO AO QUIZ DE DRAGON BALL{}'.format(cores['amarelo'], cores['limpa']))
                sleep(1)
                print('''1ª- Quem é o Lendário Super Sayajin Green?\n[ 1 ] Vegetta\n[ 2 ] Broly\n[ 3 ] Jiren''')
                rp1 = int(input('R: '))
                sleep(1)
                if rp1 == 2:
                    print('Acertaste Sayajin Lendário')
                else:
                    print('Morto pelo Lendário Sayajin Green Broly!')
                print('''2ª- Como se chama o deus da DESTRUIÇÃO?\n[ 1 ]Zen'Oh\n[ 2 ] Bills\n[ 3 ] Omni-Man''')
                rp2 = int(input('R: '))
                if rp2 == 2:
                    print('Acertaste deus da DESTRUIÇÃO {}BILLS{}'.format(cores['vermelho'], cores['limpa']))
                else:
                    print('Erraste seu Kuririn') # Fim do Menu 2
    elif op == 3:
        qp = 0
        while qp != 6:
            print('''========== {}Quiz Programador{} ==========\n[ 1 ] Linguagens\n[ 2 ] Criadores\n[ 3 ] Programas\n[ 6 ] Pra Sair...'''.format(cores['azul'], cores['limpa'])) # Menu 3
            qp = int(input('Qual Quiz desejas fazer: '))
            if qp == 1:
                print('{}BEM-VINDO AO QUIZ DAS LINGUAGENS{}'.format(cores['amarelo'], cores['limpa']))
                print('''1ª- Qual é a Linguagem responsável na criação de Interação num Site?\n[ 1 ] Python\n[ 2 ] Ruby\n[ 3 ] C#\n[ 4 ] JavaScript\n[ 5 ] PHP''')
                rp1 = int(input('R: '))
                sleep(1)
                if rp1 == 4:
                    print('Acertaste! Pequeno Programador')
                else:
                    print('Falaste Miserávelmente!')
                print('''2ª- Qual é a Linguagem responsável na Validação de Formulários?\n[ 1 ] Python\n[ 2 ] GitHub\n[ 3 ] PHP\n[ 4 ] MySQL''')
                rp2 = int(input('R: '))
                sleep(1)
                if rp2 == 3:
                    print('Acertaste pequeno ELEFANTINHO!')
                else:
                    print('ELEFANTE Morto!') # Fim do Menu 3
            elif qp == 2:
                print('{}BEM-VINDO AO QUIZ DOS CRIADORES{}'.format(cores['amarelo'], cores['limpa']))
                print('''1ª- Quem criou a Linguagem PHP?\n[ 1 ] Guido Van Hossum\n[ 2 ] Rasmus Lerdorf\n[ 3 ] Brendan Eich''')
                rp1 = int(input('R: '))
                sleep(1)
                if rp1 == 2:
                    print('Acertaste!')
                else:
                    print('Errado!')
                print(
                    '''1ª- Quem criou a Linguagem Python?\n[ 1 ] Guido Van Hossum\n[ 2 ] Rasmus Lerdorf\n[ 3 ] Brendan Eich''')
                rp2 = int(input('R: '))
                sleep(1)
                if rp2 == 1:
                    print('Acertaste!')
                else:
                    print('Errado!')
    # elif op == 4:
    elif op == 5:
        sleep(1)
        print('Saindo do Programa...')
        sleep(1)
        print('-=-'*20)
        sleep(1)
        print('='*20, '{}Volte Sempre!{} ========================'.format(cores['vermelho'], cores['limpa']))
        print('-=-'*20)
