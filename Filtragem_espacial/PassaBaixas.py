import cv2 as cv
from matplotlib import pyplot as plt

# Método criado exclusivamente para realizar a composição das bandas RGB da imagem
def composicaoFiltros(foto1, foto2, foto3):

    temp = cv.addWeighted(foto1[:, :, 2], 0.5, foto2[:, :, 1], 0.5, 0)
    res = cv.addWeighted(foto3[:, :, 0], 0.5, temp, 0.5, 0)

    return res

# Abrindo a imagem diretamente do diretório e criando suas cópias
img = plt.imread(r'C:\Users\User\Desktop\TESTES\Projetos\Filtragem_espacial\mark.jpg')
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()

# Aplicando filtro da média na imagem e criando suas cópias
blur = cv.blur(img,(5,5))
blur1 = blur.copy()
blur2 = blur.copy()
blur3 = blur.copy()

# Aplicando filtro gaussiano na imagem e criando suas cópias
gaussBlur = cv.GaussianBlur(img,(5,5),0)
gaussBlur1 = gaussBlur.copy()
gaussBlur2 = gaussBlur.copy()
gaussBlur3 = gaussBlur.copy()

# Aplicando filtro da mediana na imagem e criando suas cópias
medianBlur = cv.medianBlur(img,5)
medianBlur1 = medianBlur.copy()
medianBlur2 = medianBlur.copy()
medianBlur3 = medianBlur.copy()

# O método subplot está criando uma matriz 4x4, ou seja, com 16 posições
# Em que o primeiro parâmetro está inserindo 4 linhas e o segundo insere 4 colunas
# E o terceiro parâmetro insere a imagem resultante na posição desejada.

#fonteImagem[:,:,2] <- Converte a imagem para aparecer somente na banda azul
#fonteImagem[:,:,1] <- Converte a imagem para aparecer somente na banda verde
#fonteImagem[:,:,0] <- Converte a imagem para aparecer somente na banda vermelha

# Plotando a imagem sem passa baixas: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4,4,(1)),plt.imshow(composicaoFiltros(img1,img2,img3),cmap='gray'),plt.title('Imagem Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(5)),plt.imshow(img1[:,:,2],cmap='gray'),plt.title('Banda Azul Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(9)),plt.imshow(img2[:,:,1],cmap='gray'),plt.title('Banda Verde Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(13)),plt.imshow(img3[:,:,0],cmap='gray'),plt.title('Banda Vermelha Original')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro da média: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4,4,(2)),plt.imshow(composicaoFiltros(blur1,blur2,blur3),cmap='gray'),plt.title('Media Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(6)),plt.imshow(blur1[:,:,2],cmap='gray'),plt.title('Media Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(10)),plt.imshow(blur2[:,:,1],cmap='gray'),plt.title('Media Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(14)),plt.imshow(blur3[:,:,0],cmap='gray'),plt.title('Media Vermelha')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro gaussiano: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4,4,(3)),plt.imshow(composicaoFiltros(gaussBlur1,gaussBlur2,gaussBlur3),cmap='gray'),plt.title('Gauss Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(7)),plt.imshow(gaussBlur1[:,:,2],cmap='gray'),plt.title('Gauss Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(11)),plt.imshow(gaussBlur2[:,:,1],cmap='gray'),plt.title('Gauss Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(15)),plt.imshow(gaussBlur3[:,:,0],cmap='gray'),plt.title('Gauss Vermelho')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro da mediana: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4,4,(4)),plt.imshow(composicaoFiltros(medianBlur1,medianBlur2,medianBlur3),cmap='gray'),plt.title('Mediana Original')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(8)),plt.imshow(medianBlur1[:,:,2],cmap='gray'),plt.title('Mediana Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(12)),plt.imshow(medianBlur2[:,:,1],cmap='gray'),plt.title('Mediana Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4,4,(16)),plt.imshow(medianBlur3[:,:,0],cmap='gray'),plt.title('Mediana Vermelha')
plt.xticks([]), plt.yticks([])

# Mostrar plotagem resultante
plt.show()
cv.waitKey()
cv.destroyAllWindows()
