#Cidades:
"""
crie um dicionario chamado citie. Use os nomes de três cidades com chaves em seu dicionario.Crie um dicionario
com informações sobre cada cidade e inclua o pais em que a cidade está localizada, a população aproximada e um fato
sobre ela , as chaves do dicionario de cada cidade devem ser algo como country,population e fact. Apresente o nome
de cada cidade e todas as informações armazanadas
"""
#dicionario
citie = {
        'londres': {'country': 'inglaterra', 'population': 8.922, 'fact': 'seu centro abriga as sedes do Parlamento'},
        'manchester': {'country': 'inglaterra', 'population': 2.822, 'fact': 'É a cidade de noroeste com uma rica herança industrial'},
        'paris': {'country': 'frança', 'population': 2.161, 'fact': 'é um centro de arte,moda,gastronomia e cultura'}
        }
for nome, inf in citie.items():
    # variavel armazenando os valores dos dicionarios
    localizacao = inf['country']
    popula = inf['population']
    fato = inf['fact']
    print(f' A cidade = {nome.title()} : ')
    print(f'\t país : {localizacao.title()} ')
    print(f'\t população : {popula} milhões')
    print(f'\t fato : {fato}')