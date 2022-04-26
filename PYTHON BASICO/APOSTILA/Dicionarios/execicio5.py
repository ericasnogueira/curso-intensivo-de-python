#ANIMAIS DE ESTIMÇÃO
"""
Crie varios dicionarios, em que o nome de cada dicionario seja o nome de um animal de estimação. Em que cada dicionario,
inclua o tipo do animal e o nomde do dono, armazena esses dicionarios em uma lista chamada pets. em seguida, percorra
sua lista com uma laço e à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação
"""

animal = {'tipo': 'cachorro', 'raça': 'poodle', 'nome': 'Tob','dono': 'erica'}
animal2 = {'tipo': 'gato', 'raça': 'Angorá Turco', 'nome': 'branquela' ,'dono': 'erica'}
animal3 = {'tipo': 'gato', 'raça': 'vira-lata', 'nome': 'beto falcao' ,'dono': 'erica'}

#lista vazia

pets =  [ ]
#adicionando dicionario

pets.append(animal)
pets.append(animal2)
pets.append(animal3)

print(pets)

#percorrendo a lista
for animais in pets:
    tipo = animais['tipo'].title()
    raca = animais['raça'].title()
    nome = animais['nome'].title()
    dono = animais['dono'].title()

    print(f'O {tipo} tem como a raça {raca}, e o seu nome é  {nome} o dono é {dono}')








