#PESSOAS
"""
Crie dois novos dicionarios que representem pessoas diferentes e armazene os três dicionarios
em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorre a lista, a
apresente tudo que voce sobre a pessoa
"""

#lista vazia
people = []

pessoa1 = {'nome': 'Erica', 'sobrenome': 'Nogueira', 'idade': 21, 'cidade': 'Imperatriz'}
pessoa2 = {'nome': 'Pedro', 'sobrenome': 'Rodrigues', 'idade': 19, 'cidade': 'Imperatriz'}
pessoa3 = {'nome': 'Alexandre', 'sobrenome': 'Nogueira', 'idade': 27, 'cidade': 'Imperatriz'}

#adicionadno os dicioanrios na lista
people.append(pessoa1)
people.append(pessoa2)
people.append(pessoa3)
print(people)

for item in people:
    #pegando e imprimmindo o nome completo
    nome = item.get('nome')
    fullname = item.get('sobrenome')
    print(f'\n Nome : {nome} {fullname} ')
    #pegando e imprimindoa idade
    idade = item.get('idade')
    print(f'\t Idade : {idade}')
    #pegando e imprimindo a cidade
    cidade = item.get('cidade')
    print(f'\t Cidade : {cidade}')

    print('=')
    #pode fazer assim tambem
    name = item['nome'].title() + " " + item['sobrenome'].title()
    age = str(item['idade'])
    city = item['cidade']. title()

    print(f'{name} de {city} com {age} anos ')



