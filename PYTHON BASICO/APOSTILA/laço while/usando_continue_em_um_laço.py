"""
Em vez de sair totalmente do programa como break, podemos usar CONTINUE para começa desde o 
inicio.

"""
"""
Consideramos um laço que conte de 1 a 10, mas apresente apenas os numeros impares do 
intervalo
"""

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue

    print(number)

"""
Explicando o código :
Em number definimos com 0, como ele é menor que 10, ira entrar no while. Uma vez 
no laço, incrementamos com o contador em number +=1 , com isso number passa a ser 1,
a instrução if verifica o modulo number e 2, se ele for 0 a instrução continue diz para o 
programa ignora o restante do laço e volta para o inicio, se o numero atual não for 
divisivel por 2, o restante do laço sera executada e exibira o numero atual.
"""
print("@" * 25)
"""
EVITANDO LOOPS INFINITOS : 
    Todo laço while precisa de uma maneira de interromper para não ficar executando indefinidamente
Ex: o laço a seguir ira fazer a contagem de 1 a 5

"""
x = 1
while x < 5:
    print(x)
    x +=1  #NUNCA ESQUECE DO SEU INCREMENTO

"""
Garanta que pelo menos uma parte do código while tenha um laço false ou fazer uma instrução break
ser alcançada
"""























