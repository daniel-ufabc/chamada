def dicionario(colunas, valores):
    resposta = []
    for valor in valores:
        dicionario= {}
        for i in range(len(colunas)):
            dicionario[colunas[i][0]] = valor[i]
        resposta.append(dicionario)
    return resposta

def limpaDicionario(dicionario):
    lista_remocao = []
    for chave in dicionario:
        lista_remocao.append(chave)
    for chave in lista_remocao:
        dicionario.pop(chave)


