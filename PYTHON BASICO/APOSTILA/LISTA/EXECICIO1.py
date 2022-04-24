"""
Nomes: Amazene os nomes em uma lista chamada names. Exiba o nome de cada pessoa acessando
cada elemento da lista, um de cada vez
"""
names = ['Lucas T','João','Tobias','Beto']

print(names[0])
print(names[1])
print(names[2])
print(names[3])

print('=' * 50)

"""
Comece com a lista usada anteriomente, mas em vez de simplesmente exibir o nome de cada um, apresente uma
mensagem a elas. O texto de cada mensagem dever ser o mesmo, porem cada mensagem deve estar personalizado
com o nome da pessoa.

"""

print(" Olá me chamo ", names[0])
print(" Olá me chamo ", names[1])
print(" Olá me chamo ", names[2])
print(" Olá me chamo ", names[3])


print('=' * 50)

"""
Pense em seu meio de transporte favorito, como motocicleta ou carro, e crie uma lista que armazene vários exemplos.
Utilize sua lista para exibir uma série de frases sobre esses itens, como "Gostoria de ter uma moto honda"
"""

Tranport_F = ['carro', 'bicicleta']

print("Gostaria de ir de ", Tranport_F[0].title()," para o serviço todo dia")
print("Tenho uma",Tranport_F[1].title() ," mas não ando muito nela")