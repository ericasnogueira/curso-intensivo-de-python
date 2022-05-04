#PESSOA
"""
Use um dicionario para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome , o sobrenome,
a idade e a cidade em que ela viva. Você deverá ter chaves como first_name, last_name, age e city.
Mostre cada informação armazenada em seu dicionario

"""
pessoa = {'nome ': 'Erica', 'sobrenome': 'Nogueira', 'idade' : 21 , 'cidade': 'Imperatriz'}

print(pessoa)

#acessando valores pela chave
#nome
print(pessoa['nome '])
#sobrenome
print(pessoa['sobrenome'])
#idade
print(pessoa['idade'])
#cidade
print(pessoa['cidade'])

print(f"Ola meu nome e {pessoa['nome ']} {pessoa['sobrenome']}, tenho {pessoa['idade']} anos e moro em {pessoa['cidade']}")
print('*' * 25)
#NÚMEROS FAVORITOS
"""
Use um dicionairo para armazenar os números favoritos de algumass pessoas. Pense em cinco numeros e use-os como chave em seu
dicionario. Pense em um numero favorito para cada pessoa e armazene cada um como um valor em seu dicionario. Exiba o nome de cada
pessoa e seu número favorito
"""
numero_favorito = {'erica': 10, 'beto': 15, 'toby': 17, 'branquela': 4, 'stevi': 44}
#exibindo de todos
print(numero_favorito)

#numero favorito 
print(f"O numero favorito da erica e {numero_favorito['erica']}")
print(f"O numero favorito do beto e {numero_favorito['beto']}")
print(f"O numero favorito do toby e {numero_favorito['toby']}")
print(f"O numero favorito da  branquela e {numero_favorito['branquela']}")
print(f"O numero favorito do stevi e {numero_favorito['stevi']}")

