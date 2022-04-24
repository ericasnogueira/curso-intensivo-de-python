"""
LISTA DE CONVIDADOS
Crie uma lista que inclua pelo menos 3 pessoas que serão convidadas para jantar. Em seguida, utilize sua lista oara exibir um mensagem para cada 
pessoa, convidado-a para jantar.
"""


convidados = ['Jorge','victor','julio']

print(convidados)
print(convidados[0], "Venha jantar ccom a gente. ")
print(convidados[1], "Venha jantar ccom a gente.")
print(convidados[2], "Venha jantar ccom a gente. ")

print('-=' * 55)

"""
ALTERANDO A LISTA DE CONVIDADOS 
Um dos convidados não podera comparecer ao jantas, chame outra pesssoa.
"""
print(convidados)#lista normal 
print('O ' , convidados[2] , " não podera comparecer ao jantar")
del convidados[2]
print(convidados)
convidados.append('erica')
print(convidados)
print(convidados[0], 'Esperamos você para o jantar ')
print(convidados[1], 'Esperamos você para o jantar ')
print(convidados[2], 'Esperamos você para o jantar ')


"""
MAIS CONVIDADOS
    Tem uma mesa para jantar maior,portanto agora tem mais espaço disponivel. masi 3 convidados

"""
print("="* 75)
print('Olá achei uma mesa maior, irei chamar mais pessoas para o jantar ' + convidados[0])
print('Olá achei uma mesa maior, irei chamar mais pessoas para o jantar ' + convidados[1])
print('Olá achei uma mesa maior, irei chamar mais pessoas para o jantar ' + convidados[2])

print(convidados) #lista dos atuais convidados

convidados.insert(0,'Gabriel') #adicionando no começo da lista
convidados.append("Tomas")#adicionando no final da lista 
print(convidados) #vendo lista com os novos convidados
convidados.insert(2,'eduardo')#adicionando no meio da lista 

print(convidados)# vendo a nova lista com os novos convidados

print(f'Olá {convidados[1]}, {convidados[3]} e {convidados[4]} achei uma mesa maior então chamei mais um pessoal para jantar')
print(f"Foram eles : {convidados[0]} , {convidados[-1]} e o {convidados[2]} " )

#chamando os novos convidados para jantar 

print(f"{convidados[0]}, venha jantar ")
print(f"{convidados[2]}, venha jantar ")
print(f"{convidados[-1]}, venha jantar ")

print('/' * 60)
"""
REDUZINDO A LISTA DE CONVIDADOS
    A mesa de jantar não cheara a tempo e tem espaço só para dois convidados
"""
print("Como a mesa não chegara a tempo só podera chamar dois para jantar")
#lista completa 
print(convidados)
#removendo e deixando somente dois 
print(f"Por conta de um imprevisto só podera ir dois convidados, sinto muito {convidados[-1]}")
convidados.pop(-1)
print(convidados)

print(f"Por conta de um imprevisto só podera ir dois convidados, sinto muito {convidados[4]}")
convidados.pop(4)
print(convidados)

print(f"Por conta de um imprevisto só podera ir dois convidados, sinto muito {convidados[2]}")
convidados.pop(2)
print(convidados)

print(f"Por conta de um imprevisto só podera ir dois convidados, sinto muito {convidados[0]}")
convidados.pop(0)

print(convidados)#quem ficou na lisa de convidados


#mensagem para quem ficou

print(f"Olá {convidados[1]}, você ainda esta na lista do jantar")
print(f"Olá {convidados[0]}, você ainda esta na lista do jantar")

print('$' *42)

#removendo as ultimas duas pessoas que ficaram na lista do jantar
print(convidados)# lista com os dois ultimos restantes da lista 

del convidados[1]
print(convidados)
del convidados[0]
print(convidados)#lista estara vazia ja que todos foram removidos dela 