#Cores de alienígenas
"""
Suponha que um alienígena acabou de ser atingido em um jogo. Crie uma variavel chamada alien_color e atribua-lhe um valor
igual a 'green','yellow' ou 'red'
"""
alien_color = ['verde', 'amarelo', 'vermelho']

#testando ser a cor do alien é verde e for aparecer uma mensagem de 5 pontos
if 'verde' in alien_color:
    print('Jogador ganhou 5 pontos')

print('#' *25)

#um teste if passe e outro falhe(não tera nenhuma saida)
if 'vermelho' in alien_color:
    print('passou')
if 'azul' in alien_color:
    print('passou 2')

print('#' *25)

"""
Cores de alieníginas #2:

"""
# escolha uma cor para o alien e escreva uma cadeia if - else
# se a cor for verde, mensagem de 5 pontos, se não for verde, mensagem de 10 pontos.
cor = alien_color[1] # cor amarela
if cor == 'verde':
    print('Jogador ganhou 5 pontos')
else:
    print('Jogador ganhou 10 pontos')

print('#' *25)

#transformar a cadeia em if-elif-else


#versao verde
if 'verde' in alien_color :
    print('verde ganhou 5 pontos')
elif 'amarelo' in alien_color:
    print('ganhou 10')
else:
    print('Ganhou 15 pontos')

#versao amarelo
if 'azul' in alien_color :
    print('ganhou 5 pontos')
elif 'amarelo' in alien_color:
    print('amarelo ganhou 10')
else:
    print('Ganhou 15 pontos')

#versao vermelho

if 'vermelho' in alien_color :
    print('vermelho ganhou 15 pontos')
elif 'amarelo' in alien_color:
    print('ganhou 10')
else:
    print('Ganhou 5 pontos')
