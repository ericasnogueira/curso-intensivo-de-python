#INGRESSOS PARA O CINEMA
"""
Um cinema cobra preços diferentes para ingressos de acordo com a idade de uma pessoa. Se um pessoa tiver
menos de 3 de idade , o ingresso sera gratuito. Se a pesssoa tiver entre 3 e 12 anos, o ingresso custara 10 dolares;
se tiver mais de 12 anos , o ingresso custara 15 dolares. Escreva um laço em que voce pegunta a idade aos usuarios e,
entao, informe-lhes o preço do ingresso do cinema

"""
print(" se quiser sair do programa digite 'quit'  ")



while True:


    print('qual é a sua idade: ')
    idade = input()

    if idade == 'quit':
        print('saindo do programa')
        break

    #tranformando idade em int
    idade = int(idade)

    if idade < 3:
        print('Ingresso gratuito')

    elif idade < 12:
        print('Ingresso sera 10 dolares')

    elif idade >= 12:
        print('O ingresso é 15 Dolares')
