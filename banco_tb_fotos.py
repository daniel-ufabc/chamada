from conecta import conecta
from funcoes_auxiliares import dicionario

def cadastraNovafoto(nome_arquivo, id_usuario):
    foto = (nome_arquivo, id_usuario)
    query = "INSERT INTO tb_fotos(nome_arquivo, id_usuario) values (%s, %s)"
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

