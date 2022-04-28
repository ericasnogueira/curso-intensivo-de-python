#Lanchonete :
"""
Crie uma lista chamada sandwich_orders e a preencha com os nome de varios sanduiches. Em seguinda, crie uma lista
vazia chamada finished_sandwiches. Pecorra a lista de pedidos de sanduiches com um laço e mostre uma mensagem para
cada pedido. A medida que cada sanduiche for preparado, transfira-o para lista de sanduiches prontos, depois que todos
estiverem prontos, mostre a mensagem que lista cada um deles preparados
"""
sandwich_orders = ['atum', 'carne', 'calabresa e carne', 'calabresa']
finished_sandwich = []

while sandwich_orders:
    fazendo = sandwich_orders.pop() # removendo os itens da variavel san.. e adicionando em fazendo
    print(f' preparando o sanduiche de : {fazendo.title()}') #mostrando a mensagem com os itens ja na variavel

    #adicionando os itens na variavel vazia
    finished_sandwich.append(fazendo)

print('@' * 25)

for prepadaro in finished_sandwich:
    print(f'O sanduiche {prepadaro} esta pronto.')