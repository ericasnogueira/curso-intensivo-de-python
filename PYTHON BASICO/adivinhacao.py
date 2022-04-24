#importando as bibliotecas 
import random


print("*"* 33)
print("Bem vindo ao jogo de Adivinhação")
print("*" * 33)

#gerando o numero secreto aleatorio()
numero_secreto = round(random.randrange(1,100)) #
total_de_tentativas = 0
#representando a rodada
rodada = 1

#numero secreto que foi gerado aleatoriamente
print(numero_secreto)

#perguntando o nivel desejado

print("Qual nível de dificuldade ?")
print("(1) Fácil \n(2) Médio\n(3) Difícil")

nivel = int(input("Difine o nível :"))

if nivel == 1:
    total_de_tentativas = 20
elif nivel ==2:
    total_de_tentativas = 10
else :
    total_de_tentativas = 5

#comecando por 1 indo ate 3 que é o total de tentativas
#mas podia ser total de tentivas + 1 sem precisar bota o 0 e sim o 1
for rodada in range (1,total_de_tentativas + 1):# ta 0 pq se fosse 1 só seria duas tentativas
    #aparecer quantas tentativas tem ainda 
    print(f"tentativa {rodada} de {total_de_tentativas} ")

    # se não tiver o int ele ira considera como str
    chute = int(input("Digite um Numero entre 1 e 100: ")) #inserindo dados na variável chute
    print(f"Você chutou {chute}")

    #não aceitando numeros negativos e nem numeros maior que 100 
    # ou um ou outro 
    if chute < 1  or chute > 100:
        print("Você deve digitar um numero entre 1 e 100")
        continue # aparece a mensagem e volta para o começo

    # adicionando as variáveis assim para ficar mais organizado
    acertou = numero_secreto == chute 
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Você acertou')
        break
    else:
        #falando se foi para cima ou para baixo 
        if (maior): #numero maior que o numero secreto
            print("você errou ! O seu chute foi maior do que o numero secreto")
        elif (menor): #numero menor que o numero secreto
            print("Você errou ! o seu chute foi menor do que o numero secreto ")

    # para terminar o while e não ficar em infinitamente 
    #total_de_tentativas = total_de_tentativas - 1
    

print("FIM DO J0G0")
print('*' *33)