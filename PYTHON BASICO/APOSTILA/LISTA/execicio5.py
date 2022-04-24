#   MINHAS PIZZA, SUAS PIZZAS

"""
Faça uma cópia da lista de pizza e chame-a de friend_pizza.

"""



minha_pizza =  ['pizza','falafel','carrot cake']

#fazendo a cópia da lista 

friend_pizza = minha_pizza[:]

#adicionando uma nova pizza na lista original 
minha_pizza.append('peperoni')
#adicionando uma nova pizza na lista do amigo
friend_pizza.append('calabresa')

#provando que são duas lista diferentes
print(f"Minha lista de pizza : {minha_pizza}")
print(f"Lista de pizza do amigo :{friend_pizza} ")

print('-' * 20)
print('minhas pizzas favoritas são :')
#Usando for para exibir a primeira lista
for minha in minha_pizza:
    print(minha)
print('-'*20)

print('As pizzas favoritas de meu amigo são : ')
for amigo in friend_pizza:
    print(amigo)