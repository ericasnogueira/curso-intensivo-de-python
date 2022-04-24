#modificando um valor da lista

motos = ['honda','yamaha','suziki']
print(motos)# mostrando a lista normal

print('-' * 55)
#alterando o primeiro item da lista
#pode mudar qualquer valor da lista
motos[0] = 'ducati' #alterando o primeiro item da lista
print(motos) #mostrando a lista modificada

print('-' * 60)
motos2 = ['honda','yamaha','suziki']

#adicionando um item no final da lista
motos2.append("nova moto ducati") #adicionando
print(motos2)# mostrando nova lista com item adicionado

print('-' *60)
print('LISTA VAZIA ')
print("ADICIONE HONDA, YAMAHA E SUZIKI NA LISTA VAZIA :")

motos3 = []#LISTA VAZIA
#adicionando na lista vazia
motos3.append("honda")
motos3.append("Yamaha")
motos3.append("suziki")
#lista com as motos adicionadas
print(motos3)
print('-' * 60)
print("inserindo elementos na lista em qualquer posição")
#Inserindo elementos em uma lista em qualquer posição
#lista vazia para inserir dados em qualquer posição
motos4 = []
motos4.insert(2,"honda")
motos4.insert(1,"suziki")
motos4.insert(0,"yamaha")

print(motos4)
print('-' * 60)
print("Removendo elementos de uma lista")
print(" --Removendo um item usando a instrução del")
# se a posição da lista for conhecida a função del podera ser utilizada

#mostrando lista 
motos5 = ['honda','yamaha','suziki']
print(motos5)# lista normal
del motos5[1]
print(motos5)# lista sem o item escolhido

print('-'* 60)
print("Removendo um item com o método pop()") #o método pop() remove o último da lista

motorcycles = ['honda','yamaha','suzuki'] #lista normal 
print(motorcycles) #mostrando lista normal

#lista criada para receber o ultimo item da lista motorcyles
poped_motorcycles = motorcycles.pop()# adicionado o ultimo item da lista e removendo ele da primeira lista
print(motorcycles) # mostrando a lista sem o ultimo item

print(poped_motorcycles)# mostrando o ultimo item da lista removido 
print('='* 60)
#Exemplo para pop  
"""
As motocicletas da lista estão armazenadas em ordem cronológica, de acordo com a época em fomos proproetários. Usandomo método pop(),
 pra exibir uma afirmação sobre a ultima motocicleta que compramos
"""
epoca_2010 = ['honda','yamaha','suzuki']# lista normal
epoca_2015 = ['yamaha','suzuki','honda'] #lista normal

print (f'EM 2010 compramos as motos :  ', epoca_2010)
print (f'EM 2010 compramos as motos :  ', epoca_2015)

#ultimas moto compradas
ultima_moto2010 = epoca_2010.pop()# removendo o ultimo item de epoca_2010 e adicionando ultima_moto2010
ultima_moto2015 = epoca_2015.pop()# removendo o ultimo item de epoca_2015 e adicionando ultima_moto2015

#mostrando como esta as listas epoca 2010 e 2015
print(epoca_2010)
print(epoca_2015)

#mostrando os ultimos item das listas nas variaveis ultima moto2010 e ultima moto 2015
print(ultima_moto2010 ,' ',  ultima_moto2015) 
print('As ultimas que eu comprei foi : ' + ultima_moto2010.title() , " em 2010 e " + ultima_moto2015.title(), " em 2015")

print('-='* 50)

print('Removendo itens de qualquer posição em uma lista com pop')

motosss = ['honda','yamaha','suzuki'] #lista com os itens
print(motosss) #mostrando as motos da lista
primeiro_iten = motosss.pop(0) # removendo o iten escolhido com pop
print('A primeira moto que foi removida foi :' + primeiro_iten.title() + '.')

"""
del ou pop :
    Quando quiser APAGAR um item de uma lista e esse item NÃO vair ser usado de modo algum, utilize a instrução DEL;
    Se quiser usar um item à medida que REMOVÊ-LO, utilize o método POP()
"""


print('-='* 50)

print('REMOVENDO UM ITEM DE ACORDO COM O VALOR')
 # quando NÃO sabe a posição do elemento na lista
#lista
lista = ['honda','yamaha','suzuki']
print(lista)

lista.remove('yamaha')# removendo
print(lista)# mostrando a lista sem o item que foi removido
