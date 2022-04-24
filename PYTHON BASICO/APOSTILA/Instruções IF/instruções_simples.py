"""
Queremos saber a idade de um pessoa e queremos saber se essa pessoa tem idade suficiente
para votar.
"""
idade = 19

if idade >= 16:# verifica se o valor em idade é maior ou igual a 16, é maior então pode votar
    print('Você pode votar')
    print('Já se registrou para votar ?')
print('/'* 25)
#INSTUÇÕES IF-ELSE
"""
Um bloco if-else é semelhante a uma instrução if simples, porém a instrução else permite
definir um ação ou  conjunto de ações executado quando o teste condicional falhar.
"""

"""
fazendo o mesmo exemmplo so que com a idade para não votar
"""
idade_1 = 15
if idade_1 >=16:
    print('Pode votar')
    print('Já se registrou para votar ?')
else:
    print('Não tem idade suficiente para votar')
    print('registre quando tiver 16 para votar')
print('#' * 25)
#SINTAXE IF-ELIF-ELSE
"""
Cada teste condicional é executudo em sequência, até que um deles passe, um teste passar, o código após esse teste
será executado e Python ignorará o restante dos testes.
"""
"""
EX: Considerando um parque de diversões que cobre preços diferentes para grupos etários diferentes :
-A entrada para qualquer pessoa com menos de 4 anos é gratuita;
- A entrada para qualquer pessoa com idade entre 4 e 18 custa 5 dólares;
-A entrada para qualquer pessoa com 18 anos ou mais custa 40 dólares;
"""

minha_idade = 12

if minha_idade < 4 :
    print('Pode entra, entrada gratuita')
elif minha_idade < 18 :
    print('Entrada 5 dólares ')
elif minha_idade > 18 :
    print('Entrada custa 40 dólares')
else:
    print('não foi possivel determina idade ')
#sobre o exemplo acima
"""
O primeiro elif na verdade é outro if,executando somente se o teste anterior falhar. Nesse ponto da cadeia,
sabemos que a pessoa tem pelos 4 anos de idade, pois o primeiro teste falhou. Se a pessoa tiver pelo menos 18,
 uma mensagem apropriada será exibida, e python ignorará o bloco seguinte, se o primeiro elif falhar, o python
 ira para o código seguinte
"""
#outro jeito :
age = 12
if age < 4 :
    price = 0
elif age <18:
    price = 5
else:
    price = 10
print('A entrada vai ser : ', str(price) , '.') # Uma instrução print separada utiliza esse valor para exibir uma mensagem
#informando o preço da entrada da pessoa
