"""
Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e armazena-os em uma tupla

"""
comidas = ('Arroz', 'Carne', 'Feijão', 'Frango', 'Salada')

#Use um laço for para exibir cada prato oferecido pelo retaurante.

    #exibindo as comidas do restaurante
print('As comidas que servimos são :')
for comida in comidas:
    print(comida)

"""
# tente modifica um dos itens e certifique de que python rejeite a mudança

comidas[2] = 'farofa'
print(comidas) #rejeitada
"""


"""
O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente
um blobo de código que reescreva a tuplae, em seguida, use um laço for para exibir cada um dos itens do cardápio revisado
"""
print('¨¨' * 25)
#substituindo dois pratos

comidas = ('arroz com feijão', 'arroz com fava', 'Carne', 'Frango', 'Salada')
print('Novo cardápio é : ')
for cardapio in comidas:
    print(cardapio)
