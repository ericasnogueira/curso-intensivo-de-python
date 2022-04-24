""""
Pode ser usado para exibir uma sequêcia de números.
"""

#ex:
#não ira aparece o 5
for value in range(1,5):
    print(value)

"""
Para exibir o 5 dever usar range(1,6)
"""
for valor in range(1,6):
    print(valor)

"""
USANDO RANGE() PARA CRIAR LISTA DE NÚMEROS

"""
#quando colocamos lis() em torno da função range(), a saída será uma lista de números
#ex
numero = list(range(1,10)) 
print(numero)
print('% ' *20)
#usando range para ignorar alguns numeros em um dado intervalo.
#ex: numeros pares
#comecando do 2 e somando 2 a esse valor (o VALOR 2 é somado repetidamente até o valor final)
pares = list(range(2,11,2))
print(pares)

print('#' *22)
#colocar os dez primeiros quadrados perfeitos em uma lista
squares = [] #lista vazia
for valor1 in range(1,11):
    square = valor1 ** 2
    squares.append(square)
    print(squares)
print('%' *20)
#código mais limpo que o anterior

squares1 = [ ]#lista vazia
for valor2 in range(1,11): #percorrendo de 1 a 10
    squares1.append(valor2 ** 2) #adicionando na lista vazia o quadrado dos numeros percorridos
    print(squares1) #mostrando a lista com os numeros  

"""
ENCONTRANDO NUMEROS ESPECIFICOS COMO, VALOR MÍNIMO,MÁXIMO E A SOMA DE UMA LISTA DE NÚMERO
"""
#EX:
numeros = [1,2,3,4,5,6,7,8,9,0]

print(min(numeros)) #minimo

print(max(numeros))#maximo
print(sum(numeros))#soma

"""
LIST COMPREHENSIONS
    permite gerar a mesmas linhas de código com apenas uma linha de código
    (Uma list comprehensions combina o laço FOR e a criação de novos elemntos automaticamente em uma linha ,
     e concatena cada novo elemento automaticamente)
"""
#ex:
squad = [value1 **2 for value1 in range(1,11)] #o resultado sera só em uma linha tambem

print(squad)