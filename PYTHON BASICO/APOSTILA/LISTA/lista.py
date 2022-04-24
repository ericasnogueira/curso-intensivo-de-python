#lista de tipos de bicicletas
#              0         1         2        3
bicicletas= ['trek','cannondale','redline','specialized']
#             -4          -3            -2           -1
#imprimindo toda a lista 
print(bicicletas)

#imprimindo sem [] ou ''
print(bicicletas[0])# imprimindo o primeiro item da lista 
#primeira letra do elemento maiuscula
print(bicicletas[0].title())

#uma maneira de acessar o ultimo item da lista  facilmente
print(bicicletas[-1])
print(bicicletas[-2])

#usando concatenação para criar uma mensagem com lista
#botando o item da lista escolhida em maiusculo tambem só a primeira letra
print("minha primeira bicicleta foi " + bicicletas[-3].title())