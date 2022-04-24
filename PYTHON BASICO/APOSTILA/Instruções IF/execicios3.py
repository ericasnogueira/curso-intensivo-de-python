#ESTÁGIOS DA VIDA
"""
Escreva uma cadeia if-elif-else que determine o estágio da vida de uma pessoa. Defina um valor para a variavel
idade e então
"""
idade = 65

#se a pessoa tiver menos 2 anos, mostre uma mensagem dizendo que ela é um bebê

if idade < 2:
    print('É um bebê')
elif idade < 4:
    print('É uma criança')
elif idade < 13:
    print('É um(a) garoto(a)')
elif idade < 20:
    print('é um(a) adolescente')
elif idade < 65:
    print('É um adulto')
elif idade >= 65:
    print('É um idoso')

print('#' * 65)


#Fruta favorita

favorite_fruits = ['abacaxi', 'banana', 'cacau']

if 'banana' in favorite_fruits:
    print('voce gosta de banana')
if 'abacaxi' in favorite_fruits:
    print('Voce gosta de abacaxi')
if 'cacau' in favorite_fruits:
    print('Voce gosta de cacau ')
if 'amora' in favorite_fruits:
    print('voce gosta de amora')
if 'mamao' in favorite_fruits:
    print('voce gosta de mamao')



