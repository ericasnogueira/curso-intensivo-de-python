#INGREDIENTES PARA UMA PIZZA
"""
Escreva um laço que peça ao usuario para fornecer uma série de ingredientes para uma pizza
até que o valor 'quit' seja fornecido. À medida que cada ingrediente é especificado, aprsente
mensagem informando que acrescentara esse ingrediente a pizza
"""
print('Ola , digite o ingrediente para colocamos na sua pizza : ')

while True:


    ingrediente = input()
    if ingrediente == 'quit':
        print('Programa fechando... ')
        print('programa fechado com sucesso')
        break
    else:
        print("     se quiser sair do programa só digite 'quit'  ")
        print(f'O ingrediente {ingrediente} foi adicionado ')
        print('Digite outro ingrediente ')




