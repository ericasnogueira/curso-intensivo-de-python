"""
Conhecendo o mundo :
5 lugares que gostia de ir
"""
locais = ['espanha','japao','eua','inglaterra','coreia']

print(f'ordem pura : {locais}')
print('1' *40)

#ordem alfabetica com o sorted

print(f'Ordem sorted : {sorted(locais)}')
print(f"Mostrando sua ordem normal : {locais}")

print('2' *40)

#ordem sorted reverse
locais2 = ['espanha','japao','eua','inglaterra','coreia']
print(f'Ordem sorted reverse :{sorted(locais2, reverse=True)} ')
print(f' Ordem original : {locais2}')

print('3' *40)

# reverse
locais3 = ['espanha','japao','eua','inglaterra','coreia']
locais3.reverse()
print(f'locais com reverse : {locais3}')
print('Voltando ao normal :')
locais3.reverse()
print(f'Ordem pura {locais3}')


#ordem alfabetica

print('4' *40)

locais4 = ['espanha','japao','eua','inglaterra','coreia']

locais4.sort()
print(f'ordem alfabecita com sort : {locais4}')

#ordem alfabetica inversa

print('5' *40)
locais5 = ['espanha','japao','eua','inglaterra','coreia']

locais5.sort(reverse=True)
print(f'ordem alfabetica inversa com sort : {locais5}')


print('6' *40)

"""
CONVIDADOS PARA O JANTAR 

"""
#len

convidados = ['Jorge','victor','julio']
convidados1 = ['Gabriel', 'Jorge', 'eduardo', 'victor', 'erica', 'Tomas']
convidados2= ['Gabriel', 'Jorge', 'eduardo', 'victor', 'erica', 'Tomas','julio']

print(f'O numero de convidados é {len(convidados)}  pessoas ')
print(f'O numero de convidados é {len(convidados1)}  pessoas ')
print(f'O numero de convidados é {len(convidados2)}  pessoas ')

#erro de indice
convidadosd = ['Jorge','victor','julio']
print(convidadosd[-1])     
print(len(convidadosd))