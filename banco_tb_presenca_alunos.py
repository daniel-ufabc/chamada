from conecta import conecta
from funcoes_auxiliares import dicionario
from banco_tb_coordenadas import mudaStatusCoordenada

def buscaPresenca(id_usuario, id_chamada):
    presenca = (id_usuario, id_chamada)
    query = "SELECT * FROM tb_presenca_alunos WHERE id_usuario=%s AND id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, presenca)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def marcaPresenca(id_usuario, id_chamada, id_coordenada):
    presenca = (id_usuario, id_chamada, id_coordenada)
    query = "INSERT INTO tb_presenca_alunos(id_usuario, id_chamada, id_coordenada) values (%s, %s, %s)"
    mudaStatusCoordenada(id_coordenada)
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, presenca)
    mydb.commit()



