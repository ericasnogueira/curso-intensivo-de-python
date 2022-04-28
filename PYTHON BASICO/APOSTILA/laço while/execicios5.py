"""
Usando a lista sandwich_orders, garanta que o sanduiche de 'pastrami' apareça na lista três vezes.
acrescente um codigo proximo ao inicio do programa para exibir uma mensagem informando que a lanchonete esta
sem pastrami e ,estao, use o laço while para remover todas as ocorrencias de 'pastrami' de sandwich_orders.
Garanta que nenhum sanduiche de pastrami acabe em finished_sandwiches .
"""

sandwich_orders = ['pastrami', 'atum', 'carne', 'pastrami' ,'calabresa e carne', 'calabresa', 'pastrami']
finished_sandwich = []

#mostrando que o pastrami esta na lista
print(sandwich_orders)

print('¨¨¨¨¨¨¨¨Estamos sem pastrmi¨¨¨¨¨¨¨¨')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#mostrando que pastrami não esta na lista
print(sandwich_orders)

while sandwich_orders:
    fazendo = sandwich_orders.pop() # removendo os itens da variavel san.. e adicionando em fazendo
    print(f' preparando o sanduiche de : {fazendo.title()}') #mostrando a mensagem com os itens ja na variavel

    #adicionando os itens na variavel vazia
    finished_sandwich.append(fazendo)

print('@' * 25)

for prepadaro in finished_sandwich:
    print(f'O sanduiche {prepadaro} esta pronto.')

