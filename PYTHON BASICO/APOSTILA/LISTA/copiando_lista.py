"""
Exemplo:  temos uma lista de  nossos alimentos prediletos e queremos criar uma lista separada
 de comidas que um amigo gosta. Esse amigo gosta de tudo que está em nossa lista até agora,
  portanto podemos criar sua lista copiando a nossa:
"""
my_foods = ['pizza','falafel','carrot cake'] # lista de alimentos que gostamos
print(f"Minha comidas favoritas : ", my_foods)

#lista da comida copiada
friend_food = my_foods[:]# fazendo a copia da lista se, especificar qualquer índice e armazenando a cópia na lista do amigo 
print(f"Comida favorita do amigo : ", friend_food)

#acrescentaresmo um alimento em cada lista e mostraresmo que cada lista mantém um registro proprio
#das comidas favoritas de cada pessoa:

my_foods.append('cannoli') #adicionando na minha lista
friend_food.append('ice cream')# adicionando na lista do amigo

print(f' Minhas comidas favoritas : ',my_foods)#mostrando a nova lista com o item adicionado
print(f'Comidas do amigo :', friend_food)#mostrando a nova lista do amigo