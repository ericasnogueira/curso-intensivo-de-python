"""
Use o terceiro argumento da função range() para criar uma lista de numero imparas de 1 e 20. Utilize um laço for
para exibir os numeros.
"""
#se eu quiser um numero par ou impar e so comeca por um numero par ou impar




for impar in range(1,20,2):
    print(impar)
print('#' *25)
"""
Crie uma lista de multiplos de 3, de 3 a 30. Use um laço for para exibir os numeros de sua lista .
"""
multiplo = []

#pegando os multiplos e adicionando na lista
for m in range(3,31): # contando ate 30
    print(m) # mostrando os numeros de 3 a 30
    print('-' * 6)
    a =  m * 3 # multiplicando os numeros de 3 a 30 por 3
    multiplo.append(a) #adicionando os multiplos de 3 na sua variavel
#mostrando as multiplos
print(f'Os multiplos de 3 a 30 são : ', multiplo) #mostrando os multiplos


print('!' * 20)
"""
Crie uma lista dos dez primeiros cubos, e utilize um laço for para exibir o valor de cada cubo 

"""
cubos = [ ]
print(f'O valor de cada cubo : ')

for c in range(1,11):
    res = c **3
    cubos.append(res)
    print(f'3 ** {c} = {res}')

#so o resultado da potência 3 na lista
print(cubos)

print('!' * 20)

"""
Comprehension de cubos :
use uma list comprehension para gerar uma lista dos dez primeiros cubos
"""
cubos3 = [valor1 ** 3 for valor1 in range(1,11)]
print(cubos3)