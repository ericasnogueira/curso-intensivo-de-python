#LUGARES FAVORITOS
"""
Crie um dicionario chamado favorite_places. Pense em três lugares para usar como chaves do dicionario e armazene de um
a três lugares favoritos para cada pessoa. Percorra o dicionario com um laço e apresente o nome de cada pessoa e seus
lugares favoritos
"""
favorite_places = {
    'erica': ['nova zelândia', 'paris', 'bora bora'],
    'alexandre': ['havaí', 'tahiti', 'londres'],
    'pedro': ['roma', 'phuket', 'tóquio']
}
#percorrendo o dicionario
for nome, lugares in favorite_places.items():
    print(f'{nome.title()} e seus lugares favoritos são : ')
    for local in lugares: # outro for para tirar as {}  das palavras dos locais 
        print(f'\t {local.title()}')
    print('#' * 25)




