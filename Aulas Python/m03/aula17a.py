print('=' * 15, '\033[1;35mAULA 17 - Listas[Testes]\033[m', '=' * 15)
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)  # Adicionando elementos
num.sort()  # Ordenando os elementos
num.sort(reverse=True)  # Invertendo a ordem dos elementos
num.insert(2, 2)  # Inserindo elementos em qualquer posição
num.pop()  # eliminando valores do final
# num.pop(2)   eliminando valores declarados
if 4 in num:
    num.remove(4)
else:
    print('NÃO ACHEI O NÚMERO 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')  # Ver todas as posições
