from conecta import conecta
from openCV import detectorDeFaces

def cadastraCoordenada(x, y, w, h, id_usuario, id_foto):
    coordenada = (x, y, w, h, id_usuario, id_foto)
    query = "INSERT INTO tb_coordenadas(x, y, w, h, id_usuario, id_foto) values (%s, %s, %s, %s, %s, %s)"
    mydb = conecta()
    mycursor = mydb.cursor()
    mycursor.execute(query, coordenada)
    mydb.commit()

def detectaFaces(nome_arquivo, id_usuario, id_foto):
    coordenadas = detectorDeFaces(nome_arquivo)
    print(coordenadas)
    for (x, y, w, h) in coordenadas:
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)
        cadastraCoordenada(x, y, w, h, id_usuario, id_foto)