"""
Para acrescentar um novo par chave-valor, especifique o nome do dicionario, seguido da nova chave entre colchetes,
juntamente com o novo valor

"""
alien_0 = {'color': 'green', 'pontos ': '5'}

print(alien_0)
#adicionando chave-valor no dicionario
alien_0['x-posicão'] = 0
alien_0['y-posicão'] = 25

print(alien_0)
"""
Python não se importa com a ordem em que armazenamos cada par chave-valor, ele só se importa com a conexao entre cada 
chave e seu valor.
"""
print('#' *25)
# COMEÇANDO COM UM DICIONARIO VAZIO

"""
Para começar a preencher um dicionário vazio, defina-o o nome do dicionario com chaves vazio e depois acrescenta 
cada par-chave em sua própria linha.
EX : O modo de criaar o dicionario alien_1 usando esta abordagem/
"""
alien_1= {}

#adicionado
alien_1['Color']= 'green'
alien_1['pontos'] = 5
print(alien_1)




