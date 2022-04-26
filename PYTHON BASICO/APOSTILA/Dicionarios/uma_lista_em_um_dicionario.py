#ex:
"""
Dois tipos de infomações são armazenados para cada pizza: O tipo de massa e a lista de ingredientes.
A lista de ingrediente é o valor associado à CHAVE 'toppings'. Para usar os itens da lista, fornecemos o nome do
dicionario e a chave'toppings', como fáriamos com qualquer valor do dicionario. Em vez de devolver um unico valor,
teremos uma lista de ingredientes
"""

#armazena informações sobre a pizza que esta sendo pedida
                               #chave/lista
pizza = {'crosta': 'espessa', 'coberturas': ['cogumelos', 'extra cheese'], }

#resumo do pedido
print(f"você pediu {pizza['crosta']}-crosta pizza com os seguites coberturas/recheios :")

for topping in pizza['coberturas']:
    print('\t' + topping)

"""
EXPLICANDO O CÓDIGO :
 Na variavel pizza começamos com um dicionario que armazena informações sobre o pedido da pizza, umas das chaves do 
 dicionario é 'coberturas(toppings no livro)' tem como o seu valor uma lista que armazena todos os ingredientes 
 solicitados, no primeiro print resumimos o pedido antes de preparar a pizza. Para exibir os ingredientes , usamos 
 o laço for para acessar a lista de ingredientes, usando a chave 'cobertura',e obtemos a lista de ingredientes do 
 dicionario
 
"""
print('#' * 25)

"""
Podemos aninhar uma lista em um dicionario sempre que quiser que mais de um valor seja associado a uma unica
chave do dicionario
"""
#EXEMPLO DE FAVORITA LINGUAGENS

favorite_languages = {'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],'phil': ['python', 'haskell'], }



for name, languages in favorite_languages.items():
    print(f'\n {name.title()} sua linguagem é ')

    for language in languages:
        print(f"\t {language.title()} ")

"""
EXPLICANDO O CÓDIGO: 
No dicionario cada valor associado a cada nome é uma lista, algumas pessoas tem uma ou mais de uma linguagem favorita
quando percorremos no primeiro for com o laço, usamos uma variavel de nome laguages para ARMAZENAR cada valor do 
dicionario, pois seu valor é uma lista, dentro do laço usamos outro for para percorrer a lista de linguagens
favoritas das pessoas. Agora cada pessoa pode listar quantas linguagens favoritas quiserem
"""


