prompt = "\n diga-me alguma coisa, e irei repetir de volta"

prompt += "\n digite  'quit' para encerrar o programa "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)

"""
Explicando o código : 
    No primeiro prompt definimos o que ira informa quais são as duas opções ao usuario, fornecemos uma mensagem ou valor
    de saída (nesse caso, é quit), depois em message preparamos uma variavel para armazenar o valor que usuario ira 
    fornecer. em while python terar que comparar o valor da variavel com 'quit', mas o usuario não forneceu nenhuma
    entrada, como não tem nada para comparar ele não sera capaz de continuar executando o programa, em relação a esse 
    problema garantimos que a message(variavel) receba um valor inicial. O LAÇO WHILE SERA EXECUTADO ENQUNTO O VALOR
    DE MESSAGE NÃO FOR 'QUI'
"""
"""
message é apenas uma string vazia, então entramos no  laço. Em message = input(prompt), é  exibido
o prompt e espera o usuário fornecer uma entrada. O que quer que seja
fornecido será armazenado em message e exibido, sera avaliado novamente a condição na instrução while.
 Desde que o usuário não tenha fornecido a palavra 'quit', o prompt será exibido novamente e
Python esperará mais entradas. Quando o usuário finalmente digitar
'quit', o laço ira  para de executar e o programa termina
"""

