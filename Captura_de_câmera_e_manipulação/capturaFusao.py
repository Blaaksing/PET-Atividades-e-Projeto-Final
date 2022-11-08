import sys

import cv2 as cv

# Construtor vazio
def nothing(x):
    pass

# Carregando as imagens. Respectivamente, uma foto minha e uma de um onibus
img1 = cv.imread(cv.samples.findFile("eu.jpeg"))
img2 = cv.imread(cv.samples.findFile("onibus.jpeg"))

# Se não existir arquivo de imagem na variável 'img1', o programa fecha
if img1 is None:
    sys.exit("A imagem não existe")

# Se não existir arquivo de imagem na variável 'img2', o programa fecha

if img2 is None:
    sys.exit("A imagem não existe")

# Fazendo a janela com a barra de fusao
cv.namedWindow('Imagem Nova')
cv.createTrackbar('Peso', 'Imagem Nova', 0, 10, nothing)

# Método para manter a trackbar funcionando enquanto as fotos existirem
while (1):

    if cv.waitKey(1) & 0xFF == 27:
        break

    # Valores dos pesos. "a" tem o valor iniciando em 0, sendo essa a imagem do onibus
    # Ao se aproximar de 10, a imagem passa a ter o meu rosto :)

    # O valor de 'a' muda de acordo com a posição da trackbar dividido por 10
    a = int(cv.getTrackbarPos('Peso', 'Imagem Nova')) / 10
    b = 1 - a
    c = 0

    # Funde e exibe a imagem na tela
    img3 = cv.addWeighted(img1, a, img2, b, c)
    cv.imshow("Imagem Nova", img3)

    # Método de salvar a imagem atualizada
    # Cada numero vai representar uma especie de 'slot' para o salvamento
    # É possível salvar ate 3 imagens usando as teclas 1, 2 e 3
    k = cv.waitKey(1)

    if k == ord('1'):
        cv.imwrite('Eunibus_1.png',img3)
    if k == ord('2'):
        cv.imwrite('Eunibus_2.png',img3)
    if k == ord('3'):
        cv.imwrite('Eunibus_3.png',img3)

# Destruir todos os processos
cv.destroyAllWindows()

# Fim