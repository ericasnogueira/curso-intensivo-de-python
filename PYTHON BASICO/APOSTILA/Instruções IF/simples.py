"""
O código a seguir percorre uma lista de nomes de carros em um laço e
procura o valor "bmw". Sempre que o valor BMW, ele será exibido com letras maiúsculas,
e não apenas a inicial
"""
"""
O laço no exemplo inicialmente verifica se o valor atual de car é 'bmw', em caso
for verdadeiro o valor exibido com letras maiúsculas, caso o valor seja negativo
sera exibido com a primeira letra maiuscula
"""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

"""
Ignorando as diferenças entre letras maiusculas e minusculas ao verificar a igualdade

variavel.lower() == 
"""

#Verificando a diferença
"""
(!=) diferente de 
Armazenaremos o ingrediente pedido em uma pizza em uma variavel e entao exibimos uma 
mensagem se a pessoa pediu anchovas
"""
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')


#comparação numéricas

answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')


#Verificando se um valor está em uma lista
"""
Para descobrir se um valor em particular já está em uma lista, utilize a palavra 
reservada in
"""
#Observendo ser um ingrediente esta na lista que um cliente pediu na pizza

ingredientes = ['mushrooms' , 'onions', 'pineapple']
#verificando se está na lista
if 'mushrooms' in ingredientes:
    print('mushrooms está na lista')
else:
    print('Não está na lista')

if 'pepperoni' in ingredientes:
    print('pepperoni está na lista')
else:
    print('Não esta na lista')

print('#' * 25)

#verificando se um valor não está em uma lista  (not)
"""
Considere uma lista de usuarios que foi impedida de fazer comentarios em um forum.
Podemos verificar se um usuario foi banido antes de permitir que essa pessoa submeta 
um comentario
"""

#usuarios banidos
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
#se o valor de user NÃO tiver na lista banned, sera devolvido true e executara a lilha
#indentada
if user not in banned_users:
    print(f'{user.title()} , você pode postar uma resposta se desejar. ')