#USANDO VÁRIAS LISTAS
"""
O exemplo mostrara duas listas. A primeira é uma lista de ingredientes disponiveis na pizzaria, e a segunda
é a lista de ingredientes que o usuario pedia. Dessa vez, cada item na variavel ingredientes é verificado em relação
à lista de ingredientes disponiveis antes de ser adicionado à pizza :
"""
ingredientes_dispo = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

ingre_pedido = ['mushrooms', 'french fries', 'extra cheese']

for pedido in ingre_pedido:
    if pedido in ingredientes_dispo :
        print('Adicionando : ', pedido)
    else:
        print('Desculpe, mas não temos esse ingrediente : ', pedido)
print('Sua pizza está pronta')

#Explicando o código
"""
Em for percorremos a lista de ingredientes solicitados em um laço. nesse laço, inicialmente verificamos se cada item
solicitado está na lista de ingredientes disponivel. Se estiver, adicionamos esse ingrediente na pizza. Se o ingrediente
solicitado não estiver na lista, o bloco else será executado, ele exibe uma mensagem informando ao usuario quais 
ingredientes não estão disponivel
"""