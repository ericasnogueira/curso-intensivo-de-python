"""
Use o for para exibir os numeros de 1 a 20, incluindo-as
"""
for exibição in range(1,21):
    print(exibição)
print('$' *20)
"""
Crie uma lista de um a 100 e, então, use um for para exibir os numeros.
"""
lista= [ ]
for cem in range(1,1000001):
    lista.append(cem)
print(lista)

print('$' *20)

"""
Crie uma lista de numeros de um a milhao e em,seguida use o min() e max() para garantir que sua lista realmente começa em um  termina
em um milhao. Além disso, utilize a função sum() para ver a rapizez com que python é capaz de somar um milhao de número

"""

#print(lista)
print('O numero minimo foi : ', min(lista))
print(f' O numero maximo foi : {max(lista)}')
print(f'A soma da lista foi : {sum(lista)}')





