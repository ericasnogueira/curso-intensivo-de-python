#Outro exemplo envolvendo mais de 3 aliens
"""
Usaremos range() para criar uma frota de 30 aliens
"""

#cria uma lista vazia para armazenar alien
aliens = []

#criando 30 aliens verdes
for alien_numero in range(30):
    novo_alien = {'cor': 'verde', 'pontos': 5, 'velocidade': 'lento'}

    aliens.append(novo_alien)

#mostrar os 5 primeiros aliens
for alien in aliens[:5]:
    print(alien)
    print("...")

#mostrando a quantidade de alien criados
print(f'Total de numero de alien : {str(len(aliens))}')

"""
EXPLICANDO O CÓDIGO
    em range() devolve um conjunto de números, que simplismente diz a python quantas vezes queremos o laço se repita. 
    A cada vez que o laço é executado, criamos um novo alien na variavel novo_alien(linha 11) e a concatenamos 
    cada novo alien na lista aliens(linha 13). No ultimo for(linha 15) usamos uma fatia para exibir os cindo primeiros
    , e depois no print(linha 20) exibimos o tamanho da lista para provar que realmente foi gerado 30 aliens
"""
