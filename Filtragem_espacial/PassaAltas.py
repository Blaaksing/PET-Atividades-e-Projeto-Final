import cv2 as cv
from matplotlib import pyplot as plt

# Método criado exclusivamente para realizar a composição das bandas RGB da imagem
def composicaoFiltros(foto1, foto2, foto3):
    temp = cv.addWeighted(foto1[:, :, 2], 0.5, foto2[:, :, 1], 0.5, 0)
    res = cv.addWeighted(foto3[:, :, 0], 0.5, temp, 0.5, 0)

    return res


# Abrindo a imagem do diretório e criando suas cópias
img = plt.imread("mark.jpg")
img1 = img.copy()
img2 = img.copy()
img3 = img.copy()

# Aplicando filtro de Laplace na imagem e criando suas cópias
laplace = cv.Laplacian(img, cv.CV_8U)
laplace1 = laplace.copy()
laplace2 = laplace.copy()
laplace3 = laplace.copy()

# Aplicando filtro da Sobel em X na imagem e criando suas cópias
sobelX = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=5)
sobelX1 = sobelX.copy()
sobelX2 = sobelX.copy()
sobelX3 = sobelX.copy()

# Aplicando filtro da Sobel em Y na imagem e criando suas cópias
sobelY = cv.Sobel(img, cv.CV_8U, 0, 1, ksize=5)
sobelY1 = sobelY.copy()
sobelY2 = sobelY.copy()
sobelY3 = sobelY.copy()

# O método subplot está criando uma matriz 4x4, ou seja, com 16 posições
# Em que o primeiro parâmetro está inserindo 4 linhas e o segundo insere 4 colunas
# E o terceiro parâmetro insere a imagem resultante na posição desejada.

# fonteImagem[:,:,2] <- Converte a imagem para aparecer somente na banda azul
# fonteImagem[:,:,1] <- Converte a imagem para aparecer somente na banda verde
# fonteImagem[:,:,0] <- Converte a imagem para aparecer somente na banda vermelha

# Plotando a imagem sem passa altas: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4, 4, (1)), plt.imshow(composicaoFiltros(img1, img2, img3), cmap='gray'), plt.title('Imagem Totalmente Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (5)), plt.imshow(img1[:, :, 2], cmap='gray'), plt.title('Banda Azul Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (9)), plt.imshow(img2[:, :, 1], cmap='gray'), plt.title('Banda Verde Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (13)), plt.imshow(img3[:, :, 0], cmap='gray'), plt.title('Banda Vermelha Composta')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro de Laplace: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4, 4, (2)), plt.imshow(composicaoFiltros(laplace1, laplace2, laplace3), cmap='gray'), plt.title('Laplace Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (6)), plt.imshow(laplace1[:, :, 2], cmap='gray'), plt.title('Laplace Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (10)), plt.imshow(laplace2[:, :, 1], cmap='gray'), plt.title('Laplace Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (14)), plt.imshow(laplace3[:, :, 0], cmap='gray'), plt.title('Laplace Vermelha')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro de Sobel em X: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4, 4, (3)), plt.imshow(composicaoFiltros(sobelX1, sobelX2, sobelX3), cmap='gray'), plt.title('Sobel X Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (7)), plt.imshow(sobelX1[:, :, 2], cmap='gray'), plt.title('Sobel X Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (11)), plt.imshow(sobelX2[:, :, 1], cmap='gray'), plt.title('Sobel X Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (15)), plt.imshow(sobelX3[:, :, 0], cmap='gray'), plt.title('Sobel X Vermelho')
plt.xticks([]), plt.yticks([])

# Plotando a imagem com filtro de Sobel em Y: em 3 bandas RGB monocromáticas cada e uma imagem composta por todas elas
plt.subplot(4, 4, (4)), plt.imshow(composicaoFiltros(sobelY1, sobelY2, sobelY3), cmap='gray'), plt.title('Sobel Y Composta')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (8)), plt.imshow(sobelY1[:, :, 2], cmap='gray'), plt.title('Sobel Y Azul')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (12)), plt.imshow(sobelY2[:, :, 1], cmap='gray'), plt.title('Sobel Y Verde')
plt.xticks([]), plt.yticks([])
plt.subplot(4, 4, (16)), plt.imshow(sobelY3[:, :, 0], cmap='gray'), plt.title('Sobel Y Vermelha')
plt.xticks([]), plt.yticks([])

# Mostrar plotagem resultante
plt.show()
cv.waitKey()
cv.destroyAllWindows()
