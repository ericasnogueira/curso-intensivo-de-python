car = 'subaru'
if car == 'Subaru':
    print('carro é igual')
else:
    print('carro não é igual')

if car == 'subaru':
    print('carro é')
else:
    print('não é')

if car.lower() == 'subaru':
    # carro é igual por causa do lower que vai ignora se é maiusculo ou não
    print('carro é maiusculo')
else:
    print('Não é maiusculo')