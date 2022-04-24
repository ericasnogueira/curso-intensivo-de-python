#Modificando valores em um dicionario
"""
Para modificar um valor no dicionario, especifique o nome do dicionario com a chave entre colchetes e o o novo
valor que você quer associar a essa chve.
"""
alien_0 = {'cor': 'green', 'pontos': 5}

print(alien_0)
# mudando a cor do alien de verde para amarelo

alien_0['cor'] = 'amarelo'
#mostrando a nova cor
print(alien_0)

print(f"A nova cor do alien é : {alien_0['cor']}")
print('#' * 25)
#Exemplo mais interessante
"""
 vamos monitorar a posição de
um alienígena que pode se deslocar com velocidades diferentes.
Armazenaremos um valor que representa a velocidade atual do
alienígena e, então, usaremos esse valor para determinar a distância que
o alienígena deve se mover para a direita
"""
alien_1 = {'x-position ': 0, 'y-position': 25, 'speed': 'medium' }
print(f"Original x-position : {str(alien_1['x-position '])}")

#move o alien para a direta
#determina a distancia que o alien deve ser deslocado de acordo com sua velocidade atual
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #este deve ser um alien rapido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_1['x-position '] = alien_1['x-position '] + x_increment

print(f"Nova posição : {str(alien_1['x-position '])}")

"""
Explicando o código:
 Começamos a definindo um alien com uma posição x e y iniciais, e a velocidade igual a 'medium'. Omitimosa cor e os 
 valores da pontuação por questões de simplicidade, mas esse exemplo funcionaria da mesma maneira se tivessemos 
 incluido esses pares chave-valor. Alem disso, exibimos o valor original de x_position para ver a distancia com que o 
 alien se desloca para a direita
 
 A cadeia if-elif-else determina a distancia que o alien deve mover para a direita, esse valor é armazanado na variavel
 x_increment. Se a velocidade do alien for 'slow', ele se deslocara de uma unidade para direita, se a velocidade for 
 'medium' se deslocara de duas unidades para a direita e se for 'fast' se deslocara de três unidades a direita.
 
 Despois do calcuo, o incremento é somado ao valor de x_position e o resultado e armazenado no x_position do dicionario
 
"""

