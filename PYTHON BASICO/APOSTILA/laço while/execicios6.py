#Ferias do sonhos
"""
Escreva um programa que faça uma enquete sobre as ferias dos sonhos dos usuarios.
"""

resultados = {}

fla = True

while fla:
    nome = input('qual é o seu nome ? ')
    lugar = input('Se pudesse visitar um lugar do mundo, para qual seria ? ')

    #armazenado as respostas na variavel resultados
    resultados[nome]= lugar

    res = input('Gostaria de participar novamente ? (s/n)')

    if res == 'n':
        fla = False

print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
print('Mostrando o resultado da enquete : ')
print(resultados)
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

