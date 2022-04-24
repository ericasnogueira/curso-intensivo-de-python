"""
Python refere-se a valores que não podem mudar com IMUTÁVEIS, e uma lista imutável é chamada de tupla
"""
#USAR QUANDO QUISER ARMAZENAR UM CONJUNTO DE VALORES QUE NÃO DEVA SER ALTERADO DURANTE A VIDA DE UM PROGRAMA
#exemplo
"""
Se tivermos um retângulo que sempre deva ter termidado tamanho, podemos garantir que seu tamanho não mudará colocando as dimensões
em uma tupla
"""

dimensions = (200, 50)
print(dimensions) #exibindo a tupla completa
print(dimensions[0]) #exibindo somente o primeiro elemento
print(dimensions[1])#exibindo o segundo elemento
print('%'*25)
#percorrendo todos os valores de uma tupla com um laço

for dimension in dimensions:
    print(dimension)

print('#0' * 25)

#sobrescrevendo uma tupla

dimension1 = (200,50)
print('Original : ')               #PYTHON NÃO GERA ERRO NENHUM , POIS SOBRESCREVER UMA VARIAVEL
for dimen in dimension1:
    print(dimen)
dimension1 = (400,100)

print('Modificada : ')

for dimens in dimension1:
    print(dimens)                
