"""
Um jogo, vários eventos diferentes podem encerrá-lo, quando o jogador ficar sem espaçonavas, seu tempo se
esgotar ou as cidades que ele deveria proteher foram destruidas, o jogo devera termina, o jogo ira
termina se algum desses eventos acorrer. Se muitos eventos possiveis puderem occorrer para
o programa terminar
"""
"""
Para o programa deva executar somente enquanto muitas condições forem verdadeira, 
podemos definir uma variavel que determina se o programa como um todo deve estar ativo,
essa variavel e flag, ela atua como um sinal para programa, enquanto nosso programas
forem executar podemos botar a flag definida como true e pararem de executar quando
qualquer um dos varios eventos definir o valor da flag com false, assim a instrução
while gral precisa verificar apenas uma condição : se a flag é true, entao os outros 
eventos podem estar bem organizados no restante 
"""

"""
Ex: A flag é activo e controlara se o programa deve ou não continuar executando
"""
prompt = "\n diga-me alguma coisa, e irei repetir de volta"
prompt += "\n digite  'quit' para encerrar o programa "
message = ""


active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)

"""
EXPLICANDO O CODIGO : definimos a variavel active como True para que o program comece em 
estado ativo, fazendo isso simplifica o while, pois nenhuma comparação é feita na instrução]
a logica é tratada em outras partes do programa, enquanto a variavel active permanacer True.
    No if verifica o valor de message depois que fizer a entrada, caso seja quit e definida
    como false e o laço while termina, caso seja outro tipo que não seja quit o programa ira
    continua
"""







