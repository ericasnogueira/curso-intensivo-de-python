"""
E se quisermos remover da lista todas as instancias de um valor ?
"""
"""
Temos uma lista de animais de estimação com valor 'cat' repetido varias vezes, para remover todas as instâncias desse
valor, podemos executar um laço while ate 'cat' não estar mais na lista
"""
pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

#enquanto cat tiver em pets
while 'cat' in pets:
    pets.remove('cat')

print(pets)

"""
Explicando o código :
    apos mostrar a lista , entra no laço while depois encontra o valor cat na lista, retorna na lista novamente e
    encontra cat de novo, cada instância de cat é removida ate que valor não esteje mais na lista , nesse momento 
    ele para o laço e exibi o ultimo print
"""





