"""
Percorra as chaves e valores do dicionario, quando tiver certeza de que seu laço funciona, acrescente mais cinco
termos de python ao seu dicionario. Ao executar seu programa novamente, essas cinco palavrass e significados novos
deverão ser automaticamente incluidos na saída
"""
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

#percorrendo o dicionario/ mostrando as chaves e seus valores
for favorite,lan in favorite_languages.items():
    print(f'{favorite} = {lan}')
print('#' * 25 )
#acrescentando mais cinco itens no dicionario

favorite_languages['lucas'] = 'js'
favorite_languages['pedro'] = 'php'
favorite_languages['erica'] = 'java'
favorite_languages['jõao'] = 'Go'
favorite_languages['dalfred'] = 'c++'
print(favorite_languages)  # mostrando  o diconario completo

#percorrendo o dicionario com os novos valores
for linguagem, valores in favorite_languages.items():
    print(f' {linguagem} e a sua liguagem e {valores}')


print('#' * 25 )

#RIOS
"""
Crie um dicionario que contanha três rios importantes e o país que cada rio corta. 
"""

rios = {'nilo': 'egito', 'mississipi': 'Estados Unidos', 'huang-Ho': 'china'}

#Use um laço para exibir uma frase sobre cada rio.

for rio, pais in rios.items():
    print(f'O {rio} corre pelo(a) {pais}')
print('@'*25)
#use o laço para exibir o nome da cada rio no dicioanrio

for rio1 in rios:
    print(f' o  rio {rio1}')
print('@'*25)
#Use um laço para exibir o nome de cada país incluido no dicionario
for pais1 in rios.values():
    print(f'O país {pais1}')

