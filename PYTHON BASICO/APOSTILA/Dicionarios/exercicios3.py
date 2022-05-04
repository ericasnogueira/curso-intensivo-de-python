#ENQUETE
"""
Crie uma lista de pessoas que devem participar da enquete sobre linguagens favorias. Incluindo alguns nomes que estejam
no dicionario e outros que não estão
"""
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', 'pedro': 'php' }
pessoas = ['pedro', 'lucas', 'dalfred', 'erica']

"""
Percorra a lista de pessoas que devem participar da enquete. Se elas ja tiverem repondido à enquete, mostre uma mensagem
de agradecendo-lhe por responder. Se ainda não participaram, apresente uma mensagem convidando-a a responder.
"""

for partipante in pessoas:
    if partipante in favorite_languages:
        print(f'Obrigado por participar {partipante}')
    if partipante not in favorite_languages.keys():
        print(f' Por favor {partipante} participe de nossa enquete')
