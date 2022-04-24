"""
Pizzaria exibi uma mensagem sempre que um ingrediente é adicionado à sua pizza à medida que ela é preparada.

O cógigo para isso é bem eficiente se acriarmos uma lista de ingredientes solicitados pelo clientes e usarmos um laço
para anuciar cada ingrediente à medida que ele é acrescentado à pizza

"""

requeste_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for adicional in requeste_toppings:
    print(f'Foi adicionado : ', adicional)
print('Pizza pronta')
print('#' * 25)
#e se a pizza ficasse sem pimentões verdes

for adicional1 in requeste_toppings:
    if 'green peppers' in adicional1:
        print('Desculpe mais está em falta')
    else:
        print('adicionando : ', adicional1)
print('\npizza pronta')
"""
Explicando o código 
Desta vez verificamos cada item solicitado antes de adicioná-lo à pizza. O codigo em if verifica de a pessoa 
pediu pimentões, em caso de afirmativo exibimos uma mensagem informando por que ela não pode ter. O bloco em else
garate que todos os demais ingredientes serão adicionados à pizza
"""
print('#' * 25)
#VERIFICANDO SE UMA LISTA NÃO ESTÁ VAZIA
"""
Vamos verificar se a lista de ingredientes solicitados está vazia antes de prepararmos a pizza. Se a lista estiver vazia,
perguntaremos ao usuario se ele realmente quer uma pizza simples.
"""
adicionais = []

if adicionais:
    for sabores in adicionais:
        print('Adicionando : ', sabores)
        print('\n sua pizza está terminada')
else:
    print('tem certeza que quer uma pizza simples ? ')

"""
Explicando o código :
no if fazemos uma verificação rapida, quando o nome da lista é usado em uma instrução if, python devolve True se a lista
contiver pelo menos um item; uma lista vazia é avaliada como False. A variavel da lista passar no teste condicional, 
executamos o mesmo laço for do exemplo anterior. Se o teste condicional falhar, exibimos uma mensagem perguntando
ao cliente se ele realmente quer uma pizza simples, sem ingredientes adiconais
"""
"""
Se a lista não estiver vazia, a saída mostrará cada ingrediente solicitado adicionado à pizza
"""