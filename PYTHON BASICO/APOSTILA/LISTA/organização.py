#Ordenando lista de forma permante com o método SORT()



cars = ['bmw','audi','toyota','subaru']
print(cars)
# ordem alfabetica

cars.sort()# se botasse cars.sort(reverse=True) ia ser em ordem alfabetica so que de tras para frente
print(cars)

print('@' *55)

#Ordenando uma lisata temporariamente com a função SORTED()
    #A função sorted() permite exibir a lista em uma ordem em particular, mas não afeta a ordem da lista
    #pode ser usada como reverse=True 
    #   ... print(sorted(lista, reverse=True))


cars2 = ['bmw','audi','toyota','subaru']
print(f'Essa é a ordem original da lista 2 : {cars2}')

print(f"Essa é a ordem com sorted :{sorted(cars2)} ") 

print(f"Mostrando que a lista continua na sua forma original : {cars2}")

print('@' *55)


"""
IXIBINDO UMA LISTA EM ORDEM INVERSA
"""
#ex: ordenando os carros de acordo com a època em que fomos seus proprietarios, reorganizando a lista em ordem
#cronológica inversa:

"""
O método reverse() muda a ordem da lista permanente, mas pode ser restaurada aplicando o reverse() uma 
segunda vez
"""

cars3 =  ['bmw','audi','toyota','subaru']
print(cars3)

cars3.reverse() # do ultimo para o primeiro
#.reverse() - ele inverte a ordem da lista
print(cars3)
print('=' *55)

#ex: de reverse() permante e reventendo a ordem 

nome = ['erica','silva','nogueira']

print(f'Nome original : {nome}')

print("aplicando o reverse : ")
nome.reverse()
print(f"Nome em reverse() : {nome}")

#revertendo o reverse
nome.reverse()
print(f"Nome voltando para forma orinal : {nome}")


print('x' *55)

#DESCOBRINDO O TAMANHO DE UMA LISTA 
    #usando a função len()


cars4 =  ['bmw','audi','toyota','subaru']

print(len(cars4))
