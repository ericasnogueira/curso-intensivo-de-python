"""
Para sair do laço independente do código ou do seu resultado
utilize a instrução break, com ele podemos controlar quais linhas
são ou não executadas, fazendo que o programa só rode o que queremos,
"""
"""
EX: considere o programa que ira pergunta aos usuarios os nomes de lugares que 
ja visitaram, Podemos intorromper o laço while no programa chamando o break assim que 
o usuario fornecer o valor 'quit'
"""

prompt = '\n por favor o nome da cidade que fez a visita :'
prompt += "\n (escreva 'quit' quando quiser sair)"

#enquanto for verdadeiro
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f'Ja visitei {city.title()} tambem !')


"""
EXPLICANDO O CODIGO : 
    Em while executara indefinidamente, a menos que alcance a intrução break.
    O laço do programa continuara pedindo ao usuario os nomes da cidades ate que 
    'quit' seja fornecida, quando digitar 'quit' a intrução break é executada,
    assim saindo do programa
"""