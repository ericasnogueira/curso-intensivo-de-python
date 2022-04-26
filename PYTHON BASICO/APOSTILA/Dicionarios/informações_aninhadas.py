"""
Quando queremos armazenar um conjunto de dicionarios em uma LISTA ou uma lista com valor em um dicionario. Isso é
ANINHAR informações. Podemos aninhar um conjunto de dicionarios em uma lista, uma lista e itens em um dicionaro
ou até mesmo um dicionario em outro dicionario.

    é comum armazenar vários dicionarios em uma lista quando cada dicionario tiver diversos tipos de informações sobre
    um objeto.
"""

#UMA LISTA DE DICIONARIOS
"""
Como podemos administrar um frota de alien, é criando uma lista de alien, em que cada alien seja representado por um
dicionario com informações sobre ele 
"""

#dicionarios
alien_0 = {'cor': 'verde', 'pontos':  5}
alien_1 = {'cor': 'amarelo', 'pontos':  10}
alien_2 = {'cor': 'vermelho', 'pontos':  15}
#lista com 3 dicionarios
aliens = [alien_0, alien_1, alien_2]

for alien55 in aliens:
    print(alien55)
"""
EXPLICANDO O CÓDIGO : 
    Foi criado 3 dicionarios, cada um representando um alien diferente. Depois criamos a lista com os dicionarios. Por 
    fim, em for percorremos a lista com um laço e exibimos cada alien
"""
print('#' * 25 )
