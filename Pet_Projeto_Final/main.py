# Importando as bibliotecas necessárias
import cv2 as cv
import ProjetoPETMetodos

# A main é utilizada para chamar os métodos da aplicação
#camera = cv.VideoCapture(0)
camera = cv.VideoCapture('http://192.168.1.10:4747/video')  # URL da Camera do telefone
ret1, img1 = camera.read()
ProjetoPETMetodos.selecionar_area_para_monitoramento(img1)
ProjetoPETMetodos.monitorar_area(camera)
ProjetoPETMetodos.resgatar_data_hora(img1)
camera.release()
cv.destroyAllWindows()

