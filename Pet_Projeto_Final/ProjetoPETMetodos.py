# Importando as bibliotecas necessárias
from datetime import datetime

import cv2 as cv
import numpy as np
from playsound import playsound


# Identificar o evento do mouse em algum local da imagem
# RefPt é a variável de ponto de referência
def click_and_crop(event, x, y, flags, param):
    global refPt, cropping

    # Se o botão esquerdo do mouse for pressionado, o corte é dado como verdadeiro
    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    # Se o botão esquerdo do mouse não for pressionado, é encerrada a operação de corte, e exibe a área de referência
    elif event == cv.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv.rectangle(img3, refPt[0], refPt[1], (0, 0, 255), 2)
        cv.imshow("Escolha a regiao a ser monitorada e aperte C", img3)

# Aplicando o filtro passa baixas na imagem recortada em escala de cinza
# E subtraindo pela imagem com a passa baixa
def filtros_genericos(roi):
    blur = cv.blur(roi, (5, 5))
    sub = cv.subtract(roi, blur)
    return sub

# Aplicando o limiar na imagem com os filtros genéricos e contando os pixels brancos da imagem limiarizada
def filtros_imagem1(roi):
    ret, thresh1 = cv.threshold(filtros_genericos(roi), 44, 255, cv.THRESH_BINARY)
    area = np.sum(thresh1 == 255)
    return area

# Aplicando o laplaciano na imagem com os filtros genéricos,
# Aplicando o limiar no laplaciano e contando os pixels brancos da imagem resultante
def filtros_imagem2(roi):
    laplacian = cv.Laplacian(filtros_genericos(roi), cv.CV_64F)
    ret, thresh2 = cv.threshold(laplacian, 44, 255, cv.THRESH_BINARY)
    perimetro = np.sum(thresh2 == 255)
    return perimetro

# Método de seleção da área de monitoramento
def selecionar_area_para_monitoramento(img1):
    # Modificando acesso da imagem 1, atribuindo valor a uma nova variável, para que todos os metodos tenham acesso
    global img3
    img3 = img1
    refPt = []
    cropping = False
    clone = img1.copy()
    cv.namedWindow("Escolha a regiao a ser monitorada e aperte C")
    cv.setMouseCallback("Escolha a regiao a ser monitorada e aperte C", click_and_crop)

    # O loop é executado até que a tecla 'q' seja pressionada
    while True:
        # Exibe a tela de referência para a escolha da área a ser selecionada
        cv.imshow("Escolha a regiao a ser monitorada e aperte C", img1)
        key = cv.waitKey(1) & 0xFF

        # A região de recorte pode ser selecionada novamente se a tecla 'r' for pressionada
        if key == ord("r"):
            img1 = clone.copy()

        # Se a tecla 'c' for pressionada, o programa é inicia o monitoramento da área selecionada
        elif key == ord("c"):

            break

    # Fecha a janela de seleção
    cv.destroyAllWindows()

# Método para iniciar o monitoramento da área
def monitorar_area(camera):
    # O loop é verdadeiro
    emLoop = True
    file = cv.samples.findFile('alert2.wav')
    # Criação das variáveis que recebem os números de pixel da imagem 1 e 2 respectivamente
    x = 0
    y = 0
    #  Enquanto o loop for verdadeiro...
    while (emLoop):
        # Inicia a camera
        ret2, img2 = camera.read()
        # Cria uma variável temporária para guardar a imagem da câmera
        temp2 = img2.copy()
        # Cria uma variável para guardar a imagem recortada para o monitoramento
        roi = temp2[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        # Coordenadas do Início e Fim da área selecionada
        start_point = (refPt[0][0], refPt[0][1])
        end_point = (refPt[1][0], refPt[1][1])
        # Define a cor do retângulo sendo vermelho
        color = (0, 0, 255)
        image = cv.rectangle(img2, start_point, end_point, color, 2)
        # Roi temporário
        temp = roi.copy()
        # Conversão do roi temporário para escala de cinza
        gray = cv.cvtColor(temp, cv.COLOR_BGR2GRAY)
        if (x == 0 and y == 0):
            x = filtros_imagem1(gray) # Valor do perímetro
            y = filtros_imagem2(gray) # Valor da área
        if (ret2 != True):
            print("Algum quadro nao foi recebido.")
            break
        cv.imshow('REC', img2)


        #print(filtros_imagem1(gray)) # Debug para printar o valor da área
        #print(filtros_imagem2(gray)) # Debug para printar valor do perímetro
        print("\n")

        # Condicional para a ativação do alarme
        if ((filtros_imagem1(gray) > x * 2 and filtros_imagem2(gray) > y * 2)
                or (filtros_imagem1(gray) < x / 2 and filtros_imagem2(gray) < y / 2)):
            # Capturar a imagem caso a condicional seja satisfeita
            cv.imwrite("invasor.jpg", roi)
            # Sai do loop
            emLoop = False

        # Chamada do método para imprimir os textos na imagem no momento da invasão
        resgatar_data_hora(roi)

        # Monitorar a área a cada 250 milissegundos
        cv.waitKey(250)

    # Fecha todas as janelas
    cv.destroyAllWindows()
    # Exibe a imagem do invasor
    cv.imshow('Captura', roi)
    cv.waitKey(300)
    # Alarme
    playsound(cv.samples.findFile('alert2.wav'))
    cv.waitKey(0)

# Método para registrar que houve invasão em um determinado momento
def resgatar_data_hora(roi):
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y - %H:%M')
    text = "Data e hora da invasao:"
    # Adicionando os textos em suas devidas posições. X Sempre começando em 10 e Y pulando linha de 30 em 30
    # O tamanho da fonte é 0.75 e o texto é exibido na cor verde (para melhor leitura)
    cv.putText(roi, 'ALERTA INVASAO', (10, 30), cv.FONT_HERSHEY_SIMPLEX, (3/4), (0, 255, 0))
    cv.putText(roi, text, (10, 60), cv.FONT_HERSHEY_SIMPLEX, (3/4), (0, 255, 0))
    cv.putText(roi, data_e_hora_em_texto, (10, 90), cv.FONT_HERSHEY_SIMPLEX, (3/4), (0, 255, 0))