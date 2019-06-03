import datetime

def dicionario(colunas, valores):
    resposta = []
    for valor in valores:
        dicionario = {}
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

def semanal(dia_semanal):
    if dia_semanal <= 7:
        return "I"
    else:
        return "II"

def removeEspaco(texto):
    return texto.replace(" ", "")

def nomeArquivo(id_chamada, nome_arquivo):
    extensao = nome_arquivo.split('.')
    extensao = extensao[len(extensao)-1]
    nome_final = "{}.{}".format(id_chamada, extensao)
    return nome_final

def ordenaChamadasAtivas(turma):
    return turma['data_chamada']


