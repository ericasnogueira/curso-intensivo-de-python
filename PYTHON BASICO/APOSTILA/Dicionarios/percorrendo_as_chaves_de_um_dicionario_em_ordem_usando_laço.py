"""
Uma maneira de fazer os itens serem devolvidos em determinada sequência é ordenar as chaves à medida que são devolvidas
no laço for.
    Podemos usar a função sorted() para obter uma cópia ordenada das chaves
"""

linguagens = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

for nome in sorted(linguagens.keys()):
    print(f'{nome.title()}, obrigado por participar da enquete')

"""
Explicando o código :
    Esse for é como os outros for, exceto pela a função sorted() está em torno do método dicionario.keys().
    Com isso o python pegar todas as chaves do dicionario e ordenar essa lista antes de percorrê-la com o laço.
        A saida mostra os nomes de todos os que responderam à enquete.
"""
print("#" * 25)
# PERCORRENDO TODOS OS VALORES DE UM DICIONARIO COM UM LAÇO
"""
Quando só queremos os valores contido no dicionario, o método value() poder ser usado para devolver uma lista de valores
sem as suas chaves
"""
"""
Ex: Queremos uma lista de todas as linguagens escolhidas em nossa enquete sobre linguagens de programção, sem o nome 
da pessoa que escolheu cada linguagem.
"""

lin_escolhidas = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

print('As linguagens escolhidas foram : ')

for escolhidas in lin_escolhidas.values():
    print(escolhidas.title())

"""
EXPLICANDO O CÓDIGO:
    A instrução for, nesse caso ira extrair cada valor do dicionario e o armazena na variavel escolhidas. Quando
    esses valores são exibidos, temos uma lista de todas as linguagens.

    Esse abordagem de values ela extrai os valores mesmo sem verificar se há repetições
"""
print('@' * 25 )
"""
Para ter um resultado sem repetições pode ser usado um CONJUNTO(set), um conjunto é semelhante a uma lista, exceto que 
cada item de um conjunto deve ser UNICO 

"""
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

print('As seguintes liguagens foram mencionadas : ')

for language in set(favorite_languages.values()):
    print(language.title())

"""
Quando colocamos o set() em torno de uma lista que contenha itens duplicados, ele identifica os itens únicos na lista 
e cria um conjunto a partir desses itens.
    No for usamos o set() para extrair as linguagens unicas no dicionario
     
"""