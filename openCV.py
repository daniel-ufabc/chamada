import cv2

def detectorDeFaces(nome_imagem):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('uploads/{}'.format(nome_imagem))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    return faces

    '''
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    print(faces)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

def dimensoesImagem(nome_imagem):
    img = cv2.imread('uploads/{}'.format(nome_imagem))
    altura, largura, canais = img.shape
    return {'altura': altura, 'largura': largura}



