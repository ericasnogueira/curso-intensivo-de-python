#EX:
"""
Se tiver varios usuarios em um site, cada um com o nome unico, os nomes dos usuarios
podem ser usados como CHAVE do dicionario.
"""
"""
No exemplo iremos  armazenar três informações sobre cada usuário:
seu primeiro nome, o sobrenome e a localidade. iremos acessar as 
informações percorrendo os nomes dos usuários em um laço e o
dicionário de informações associado a cada nome de usuário
"""

usuarios = {
            'aeinstei': {'first' : 'albert', 'last': 'einstein', 'location': 'priceton', },
            'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris', },
            }

for username, user_info in usuarios.items():
    print(f'\n Username : {username}')
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print(f"\t Full name : {full_name.title()}")
    print(f"\t Location : {location.title()}")

"""
EXPLICANDO O CÓDIGO :
Iniciamos definindo o dicionario usuarios com DUAS CHAVES, uma para cada nome, o VALOR associado a cada chave é um 
dicionario que inclui o primeiro nome, o sobrenome e a localidade de cada um, no FOR percorremos o dicionario
usuarios com o laço, arzenamos cada CHAVE na variavel username e o dicionario associado a cada nome na variavel
usur_info, depois que entrarmos no laço principal, exibimos o nome do usuario no print
em FULL_NAME começamos a acessar o dicionario interno, a variavel USER_INFO que contem o dicionario com as tres chaves
"first , last e location", usamos cada chave para gerar um nome completo e a localalidade
"""
