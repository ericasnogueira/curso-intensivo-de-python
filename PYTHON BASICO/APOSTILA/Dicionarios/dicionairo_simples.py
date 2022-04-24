# Dicionario simples
"""
Considerando um jogo de alienigenas que possam ter cores e valores de pontuação diferentes.
O dicionario ira armazena informações sobre alieniginas em particular

"""
alien_0 = {'color': 'green', 'pontos ': '5'}
print(alien_0)# mostrando todo o dicioanrio
print(alien_0['color']) # mostando só a cor
print(alien_0['pontos ']) # mostrando a quantidade de pontos

# Acessando valores em um dicionario
"""
Para obter o valor associado a uma chave, especifique o nome do dicionario e coloque a chave entre colchetes
"""
alien_1 = {'cor': 'green'}
print(alien_1['cor'])
print('#' * 25)
#Ex:
"""
Um jogador atingir esse alien, podemos consultar quantos pontos ele deve ganhar
"""

alien_2 = {'cor':'verde','pontos':5}

new_points = alien_2['pontos'] #adicionando os pontos na nova variavel

print('vocé ganhou ', str(new_points) , ' pontos')
"""
Explicando o codigo : Despois que definimos o dicionario, a nova variavel extrai o valor associado à chave 'pontos'
do dicionairo, o valor então é armazenado na variavel. No print converte esse valor inteiro em string e exibe
a frase sobre a quantidade de pontos o jogador ganhou
"""