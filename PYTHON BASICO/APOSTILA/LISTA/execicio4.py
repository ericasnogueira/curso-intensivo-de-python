"""
Exiba a mensagem Os três primeiros itens da lista são : Em seguida, use uma fatia para exibi os três primeiros
intesn
"""

my_foods =  ['pizza', 'falafel', 'carrot cake', 'cannoli','ice cream']
print(f'Os três primeiros itens da lista são : {my_foods[0:3]}')
print(len(my_foods)) # descobrindo quantos itens na lista
"""
Três itens do meio da lista são : Use uma fatia para exibir três itens do meio da lista

"""
# boto o 4  mas ele diminui e fica como 1: 3 
print(f'Três itens do meio da lista são : {my_foods[1:4]}')

"""
Exiba a mensagem Os três último itens da lista são : Use uma fatia para exibir os três últimos itens
da lista.
"""

print(f"Os três últimos itens da lista são : {my_foods[-3:]}")