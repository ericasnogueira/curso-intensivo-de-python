usuarios = ['admin', 'erica', 'suho', 'toby', 'bob']

for usuario in usuarios:
    print('Olá ', usuario, ', gostaria de ver um relatório de status ?')
    print('#'*20)
print('=' *15)

#sem usuario / verificando se a lista está vazia
lista_vazia = []
if not usuarios: #se NÃO tiver usuario (itens da lista)
    print('lista vazia, precisamos encontrar alguns usuários')
else:
    print('Lista não esta vazia , usuarios : ', usuarios)

print('@' * 25)

#removendo todos os nomes da lista ususarios e certifique-se de que a mensagem correta seja exibida
#excluindo todos
usuarios.clear() # apagando todos os usuarios da lista usuarios

if not usuarios:
    print('Precisamos entrontrar alguns usuarios .')
else:
    print('Já tem usuarios')
