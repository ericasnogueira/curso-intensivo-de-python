"""
Pode ser usado quantos quiser
"""
#Ex:
"""
Se o parque de diversões implementasse um desconto para idosos,
você poderia acrescentar mais um teste condicional no código
a fim de determinar se uma pessoa está qualificada a receber
esse desconto. Suponha que qualquer pessoa com 65 anos ou mais
pague metade do preço normal da entrada, isto é, 5 dólares:
"""
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
#para pessoas com 65 anos ou mais
else:
    price = 5
print('Seu ingresso de entrade é R$', str(price),'.')
#sobre o codigo acima
"""
O segundo bloco elif faz uma verificação para garantir que a pessoa
tenha pelo menos de 65 anos antes de lhe cobrar o preço da entrada
inteira
"""
print('#'*25)
#OMITINDO O BLOCO ELSE
"""
Python não exige um bloco else no final de uma cadeia if-elif.
Às vezes, um bloco else é útil, outras vezes,é mais claro usar
uma instrução elif adicional que capture a condição específica de interesse
"""

idade = 12
if idade < 4:
    preco = 0
elif idade <18:
    preco = 5
elif idade < 65:
    preco = 10
elif idade >= 65:
    preco =  5
print('Seu ingresso é : R$', str(preco), '.')
"""
O ultimo elif atribui um preço de 5 dálares quando a pessoa tiver 65 anos ou mais, o que é um pouco mais claro que o 
bloco else, com essa mudança,todo bloco de código deve passar por um teste específico para executado.
"""
print('-'*25)

#TESTANDO VÁRIAS CONDIÇÕES
"""
É importante verificar todas as condições de interesse, devemos usar uma série de instruções if simples,
sem blocos elif ou else, ela ira fazer sentido quando queremos mais de uma condição verdadeira(True) e queremos 
que em todas as condições sejam verdadeiras
"""
#EXEMPLO

"""
Vamos considerar um exemplo de pizzaria. Se alguém pedir pizza com dois ingredientes, será necessário garantir que esses
dois ingredientes sejam incluidos em sua pizza.
"""
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adicionando mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adicionando pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adicionando extra cheese')
print('Terminei a sua pizza')
"""
Explicando o código:
O primeiro if verificar se a pessoa pediu por mushrooms na pizza, em caso de afirmativo, uma mensagem será exibida para
confimar esse ingrediente. O teste para o segundo if corresponde a um if simples e não para um elif ou else, então ele
sera executado independentemente de o teste anterior ter passado ou não, o ultimo if verifica se o cheese foi pedido,
não importando o resultado dos outros dois, esses três testes independente são realizados sempre que o programa é 
executado.
"""
#O código não funcionaria se tivesse elif ou else, já que ele pararia na primeira opção verdadeira (True)

"""
Em suma, se quiser que apenas um bloco de código seja executado, utilize uma cadeia if-elif-else. Se mais de um bloco
de código deve executar, utilizando uma série de instruções if independentes.
"""