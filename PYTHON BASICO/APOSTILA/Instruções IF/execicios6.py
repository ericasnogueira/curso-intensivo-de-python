"""
Numeros Ordinais indicam a sua posição em uma lista.
Armazene os números de 1 a 9 em uma lista
percorra a lista com um laço
use uma cadeia if-elif-else no laço para exibir a terminação apropriada para cada numero ordinal. Sua saida
devera conter "1st 2nd 3rd 4th 5th
6th 7th 8th 9th ", e cada resultado deve estar em uma linha separada
"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numeros:
    if n == 1:
        print(f'{n}st')
    elif n == 2:
        print(f'{n}nd')
    elif n == 3:
        print(f'{n}rd')
    else:
        print(f'{n}th')