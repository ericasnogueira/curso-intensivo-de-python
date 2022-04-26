#Numeros favoritos:
"""
Modifique para que cada pessoa possa ter mais de um numero favorito, em seguinda, apresente o nome de cada pessoa,
justamente com seus numeros favoritos
"""
numero_favorito = {'erica': [10, 4],
                   'beto': [15, 44],
                   'toby': [17, 56],
                   'branquela': [4, 23],
                   'stevi': [4, 135], }

for nome, numero in numero_favorito.items():
    print(f'{nome} tem como os numero favoritos : ')
    for numeros in numero:
        print(f'\t {numeros}')