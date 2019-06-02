from conecta import conecta
from funcoes_auxiliares import dicionario

def cadastraNovafoto(nome_arquivo, id_usuario, id_chamada):
    foto = (nome_arquivo, id_usuario, id_chamada)
    query = "INSERT INTO tb_fotos(nome_arquivo, id_usuario, id_chamada) values (%s, %s, %s)"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, foto)
    mydb.commit()

def atualizaDimensao(largura, altura, nome_arquivo):
    foto = (largura, altura, nome_arquivo)
    query = "UPDATE tb_fotos SET largura=%s, altura=%s WHERE nome_arquivo=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, foto)
    mydb.commit()

def buscaFoto(nome_arquivo):
    foto = (nome_arquivo,)
    query = "SELECT * FROM tb_fotos WHERE nome_arquivo=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, foto)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def buscaFotoIdChamada(id_chamada):
    foto = (id_chamada,)
    query = "SELECT * FROM tb_fotos WHERE id_chamada=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, foto)
    resposta = dicionario(mycursor.description, mycursor.fetchall())
    return resposta

def deletaFotoIdFoto(id_foto):
    foto = (id_foto,)
    query = "DELETE FROM tb_fotos WHERE id_foto=%s"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, foto)
    mydb.commit()

print(buscaFotoIdChamada(73))

