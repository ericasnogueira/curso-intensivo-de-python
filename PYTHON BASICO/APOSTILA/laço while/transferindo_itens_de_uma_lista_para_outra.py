"""
Uma lista de usuarios recem-registrados em um site, porem não verificados, depois de conferir esses usuarios, como
transferi-los para uma lista separada de usuarios confirmados? uma maneira seria usar o while para extrair os
usuarios da lista de não confirmados a medida que verificamos e adiciona-los na lista de usuarios confirmados.
"""

#usuarios que precisam ser verificados
unconfirmed_user = ['alice','brie','candace']

#lista vazia para armazenar os usuarios confirmados
confirmed_users = []

#verifica cada usuario até que não haja mais usuarios não confirmados
#transfere cada usuario verificado para a lista de usuarios confirmados

while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f'Verificação user : {current_user.title()}')

    confirmed_users.append(current_user)
#exibi todos os usuarios confirmados
print('\n usuarios confirmados : ')
for confirmed_users in confirmed_users:
    print(confirmed_users.title())


"""
EXPLICANDO O CÓDIGO: 
     começamos uma lista com os não confirmados e uma lista vazia para armazenar os confirmados, no laço while
     executa enquato a lista unconfirmde não estiver vazia, no laço a função pop() em remove os usuarios não verificados
     ate o final da lista unconfirmde, nisso como candace é o ultimo elemento da lista, seu nome é o primeiro a ser
     removido e armazenada na lista current_users e assim por diante, quando não tiver mais ninguem na lista de não
     confirmados o laço para
"""




