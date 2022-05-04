"""
Verificando nomes de usuários: Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de
usuário único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta
que um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de
usuário já foi usado. Em caso afirmativo, mostre uma mensagem informando
que a pessoa deverá fornecer um novo nome. Se um nome de usuário não foi
usado, apresente uma mensagem dizendo que o nome do usuário está
disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças
entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá
ser aceito.

"""
usuarios = ['Admin', 'erica', 'suho', 'toby', 'bob']
no_usuarios = ['root', 'ocOmENTh', 'NGaNerSH', 'erica', 'admin']

#transformando a variavel usuarios em minusculo i = index
for i in range(len(usuarios)):
    usuarios[i] = usuarios[i].lower()
print(usuarios)
for nova in no_usuarios:

    if nova in usuarios:
        print(f'O nome : {nova} , já está em uso apresente um novo nome ')
    if nova not in usuarios:
        print(f' Nomes disponiveis :{nova} ')
