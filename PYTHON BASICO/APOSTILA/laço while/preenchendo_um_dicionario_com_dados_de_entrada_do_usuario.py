"""
Um programa de enquete em que cada passagem pelo while solicita o nome do participante e uma resposta,
armazena os dados coletados em um dicionario.
"""

respostas = {}
#define uma flag para indicar que a enquete esta ativa
polling_active = True

while polling_active :
    #pede o nome da pessoas e a resposta
    name =input('Qual é o seu nome ?')
    resposta = input('Gosta do clime de hoje ?')

    #armazena a resposta no dicionario
    respostas[name] = resposta

    #descobre se outra pessoa ira responde a enquete

    repeat = input('Voce gostaria de responde nossa enquete ? (yes/no)')

    if repeat == 'no':
        polling_active = False

#enquete foi concluida. Mostre os resultados
print("\n-----Os resultado------")
for name,resposta in respostas.items():
    print(f" {name} gostou do clima : {resposta}.")



"""
EXPLICANDO O CODIGO : 
    incialmente definimos um dicionario vazia(respostas) e criamos uma flag(polling_active) para indicar que a enquete
    esta ativa, enquanto a flag for true, sera executado o laço while, no codigo pergunta para o usuario o nome e se ele
    gosta do clima do dia , onde a sua resposta é armazenada no dicionario respostas, depois é feita outra pergunta
    se ele que reponde a enquete,caso ele responda yes o programa ira entrar no laço novamente, se for no, a flag sera
    definida com false e o laço ira para de ser executado e os resultado sera exibido
"""