import cv2 as cv
from matplotlib import pyplot as plt

# Ler imagem do diretorio
img = cv.imread('mark.jpg',0)
# Aplicando filtro da mediana na imagem
img = cv.medianBlur(img,5)
# Aplicando os limiares e 30, 150 e 200 nas variáveis 'th1','th2' e 'th3' respectivamente
ret,th1 = cv.threshold(img,30,255,cv.THRESH_BINARY)
ret,th2 = cv.threshold(img,150,255,cv.THRESH_BINARY)
ret,th3 = cv.threshold(img,200,255,cv.THRESH_BINARY)
# Limiar adaptativo da media
th4 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
# Limiar adaptativo gaussiano
th5 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

# Array que armazena as legendas
titles = ['Original','Limiar de 30','Limiar de 150','Limiar de 200',
          'Limiar adaptativo da média','Limiar adaptativo gaussiano']
# Array que armazena as imagens
images = [img,th1,th2,th3,th4,th5]

# Loop para fazer a plotagem das imagens na tela. Serão processados até 6 elementos
for i in range (6):
    # Matriz com 2 linhas e 3 colunas é criada e nela será mostrada as imagens e os seus respectivos titulos
    plt.subplot(2,3,(i+1)),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Mostrar plotagem resultante
plt.show()
cv.waitKey()
cv.destroyAllWindows()
