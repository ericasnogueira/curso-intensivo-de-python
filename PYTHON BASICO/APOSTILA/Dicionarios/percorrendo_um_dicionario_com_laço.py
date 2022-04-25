"""
Podemos percorrer todos os pares chave-valor
de um dicionario usando suas chaves ou seus valores
"""

#PERCORRENDO TODOS OS PARES CHAVE-VALOR COM UM LAÇO
"""
Vamos considerar um novo dicionário projetado para armazenar
informações sobre um usuario em um site.
O dicionario a seguir armazenara o nome de usuario, o primeiro nome
e o sobrenome de uma pessoa
"""
user_0 = {'nome': 'efermi', 'nome-meio': 'enriro', 'sobrenome': 'fermi',}
#   chave   valor   dicioanrio
for chave, valor in user_0.items():
    print(f'CHAVE : {chave}')
    print(f'VALOR : {valor}')

"""
EXPLICANDO O CÓDIGO:
     No for para escrever um laço no dicionario devemos criar nome para duas variaveis
     que armazenarão a chave-valor. Podemos escolher qualquer nome que quiser para as variaveis.
    Depois das duas variaveis está o nome do dicionario e depois dele esta p método items(), que 
    devolve uma lista de pares chave-valor.
"""
print('#' *25 )
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil':'python'}


for nome, liguagem in favorite_languages.items():
    print(f'{nome}  a sua liguagem favorita e {liguagem}')

print('@'*25)

#PERCORRENDO TODAS AS CHAVES DE UM DICIONARIO COM LAÇO
"""
O método key() é conviniente quando não precisamos trabalhar com todos os valores
de um dicionario. 
EX: vamos percorrer o dicionario  com um laço e exibir os nomes de todos que respoderam 
a enquente
"""

for nomes in favorite_languages.keys():
    #somente o nome == chaves
    print(f'participou da enquente : {nomes.title()}')

"""
EXPLICANDO O CODIGO:
    em for extraimos todoas as chaves do dicionario e armazenamos, uma de cada vez,
    na variavel nomes
"""
print('-' *25)
#pode ser feito assim tambem
#mas assim vai vim pela quantidade de chaves e vem o dicionario completo
for names1 in favorite_languages:
    print(f"Olá novamente participante : {favorite_languages} ")

print('!' * 25)
"""
Podemos acessar qualquer valor associado a qualquer chve que interessar no laço usando a chave atual.
    EX: 
        Vamos exibir uma mensagem a dois amigos sobre a linguagem que ele escolheram.
        Percorreremos os nomes no dicionario com laço,porem, quando o nome for de um de nossos amigos
        apresentaremos uma mensagem sobre a linguagem favorita.
"""
#dicionario com amigos e as linguagens
amigos_linguagem = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
             # nomes  =  chave / linguagem = valor
#lista de amigos
amigos = ['phil', 'sarah']

#percorrendo o dicionario
#com o key pegando a chave que seria os nomes
for nome_1 in amigos_linguagem.keys():
    print(nome_1.title())# mostrandos os nomes
    if nome_1 in amigos:
        print(f" Olá {nome_1}, a sua linguagem favorita é {amigos_linguagem[nome_1].title()}")


"""    
    A lista amigos e de quem queremos exibir a mensagem. No laço exibimos os nomes de cada pessoa
    Em entao no if verificamos o nome com quem estamos trabalhando [nome_1], na lista de amigos , se estiver
     exibimos uma mensagem especial, incluindo a sua linguagem , para acessar a linguagem
     favorita em [amigos_linguagem[nome_1]] usamos o nome do dicionairo e o valor atual de nome_1 como chave.
     O nome de todos é exibido, porem da lista amigos recebem um mensagem especial 
    
"""
print('@' *25)
"""
Podemos usar o método keys() para descobrir se uma pessoa em particular participou da enquete por exemplo
"""
enquete = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }

# se 'erin' NÃO tiver em
if 'erin' not in enquete.keys():
    print('Erin , por favor entre em nossa enquete')
"""
O método keys() não serve apenas para laços: na verdade, ele devolve uma lista de todas
as chaves, e a linha em if simplismente verifica se 'erin' está no dicionario, como não está,
uma mensagem é exibida convidando-a a particpar da enquete
"""


