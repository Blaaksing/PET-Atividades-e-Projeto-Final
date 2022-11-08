import numpy as np
import cv2 as cv

#Variável cap que está recebendo a URL da camera do telefone
cap = cv.VideoCapture('http://192.168.1.3:4747/video')

#Se a captura não puder ser aberta, exibe a seguinte mensagem de erro
if not cap.isOpened():

    # Mensagem de erro
    print("A câmera não pode ser aberta.")
    exit()

# Enquanto a camera estiver ativa, irá executar os seguintes passos
while True:

    # A captura está sendo lida e armazenada no frame. Ret é a variavel de "Sucesso"
    ret, frame = cap.read()

    # Metodo usado para salvar as imagens em suas respectivas cores
    # s é a variável em que quero armazenar o caractere de entrada
    s = cv.waitKey(1)

    # Se a tecla pressionada for "s" (minusculo), o programa faz as capturas em PNG, simultaneamente, mas em arquivos diferentes
    # Em cinza, nas cores originais, em azul, em verde e em vermelho, respectivamente
    if s == ord("s"):
        cv.imwrite('capturaGray.png', gray)
        cv.imwrite('capturaOriginal.png', original)
        cv.imwrite('capturaBlue.png', B)
        cv.imwrite('capturaGreen.png', G)
        cv.imwrite('capturaRed.png', R)

    # Se a variável de sucesso for um fracasso, o programa exibe a seguinte mensagem de erro
    if not ret:

        # Mensagem de erro
        print("Quadro não recebido.")
        break

    # Altura, largura e camada da imagem. Esse metodo retorna o formato de um array.
    # A variável 'zeros' recebe a forma do frame como primeiro parâmetro, e o segundo parametro retorna o tipo do array
    # Por possuir altura e largura, o programa traduz como uma imagem de duas dimensões
    # R,G,B faz a divisao da janela em 3 variáveis, onde cada uma irá receber o valor de cada esquema de cor.
    height,width,layer = np.shape(frame)
    zeros = np.zeros((height,width),np.uint8)
    R,G,B = cv.split(frame)

    # Valores de mesclagem e conversão de cores sendo atribuidos para as variáveis a seguir
    B = cv.merge([B,zeros,zeros])
    G = cv.merge([zeros,G,zeros])
    R = cv.merge([zeros,zeros,R])
    original = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Exibir as janelas. O titulo é recebido como primeiro parâmetro
    # E o segundo parâmetro é atribuido ao canal de cores desejado
    cv.imshow("Escala de Cinza", gray)
    cv.imshow('Imagem Original', original)
    cv.imshow('Escala de Azul', B)
    cv.imshow('Escala de Verde', G)
    cv.imshow('Escala de Vermelho', R)

    # Sair do programa se a tecla "q" (minuscula) for pressionada
    if cv.waitKey(1) == ord('q'):
        break

# Abortar operação de captura e fechar todas as janelas, respectivamente.
cap.release()
cv.destroyAllWindows()

# Fim