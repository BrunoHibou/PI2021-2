import numpy
import numpy as np
import cv2
import PIL.Image as pimg
import matplotlib.pyplot as plt


# módulo referente às transformações
class PI:

    def image_to_matrix(self, img):

        image = pimg.open(img).convert("L")

        matriz_pixel = list()
        linha_pixel = list()

        ## PERCORRENDO O ARRAY DA IMAGEM
        # Percorre a altura da imagem 
        for x in range(image.height):
            # Zera o array de linha de pixels
            linha_pixel = list()
            # Percorre a linha da imagem
            for y in range(image.width):
                pixel = image.getpixel((y, x))  # recebe o pixel na coordenada
                linha_pixel.append(pixel)  # adiciona o pixel ao array linha
            # adiciona a linha de pixels ao array
            matriz_pixel.append(linha_pixel)

            ## IMPRIMINDO ARRAY COM VALORES DE PIXEL
        file = open('log.txt', 'w')
        for i in range(len(matriz_pixel[0])):
            file.write(f'{matriz_pixel[i]}\n')
        file.close()

        ## RETORNANDO O ARRAY COM VALORES DE PIXELS
        print(matriz_pixel[0][0])
        return np.asarray(matriz_pixel)

    # função que realiza a adição entre uma imagem A e uma imagem B
    def addition(self, image1, image2):
        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                result[index][index2] = image1[index][index2] + image2[index][index2]

        return result

    # função que realiza a subtração entre uma imagem A e uma imagem B
    def subtraction(self, image1, image2):
        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                result[index][index2] = image1[index][index2] - image2[index][index2]

        return result

    # função que realiza a multiplicação entre uma imagem A e uma imagem B
    def multiplication(self, image1, image2):
        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                a = image1[index][index2] / 255
                b = image2[index][index2] / 255
                total = a * b
                result[index][index2] = total * 255

        return result

    # função que realiza a divisão entre uma imagem A e uma imagem B
    def division(self, image1, image2):
        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                a = image1[index][index2] * 255
                b = image2[index][index2] * 255
                total = a / b
                result[index][index2] = total * 255

        return result

    def translate(self, image1):
        imgOriginal = cv2.imread(image1)
        totalLinhas, totalColunas = imgOriginal.shape[:2]
        res = cv2.resize(imgOriginal, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        matriz = np.float32([[1, 0, 100], [0, 1, 100]])

        imgDeslocada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))

        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem Deslocada", imgDeslocada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    def rotate(self, image1):
        imgOriginal = cv2.imread(image1)
        res = cv2.resize(imgOriginal, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        totalLinhas, totalColunas, x = res.shape

        matriz = cv2.getRotationMatrix2D((totalColunas / 2, totalLinhas / 2), 90, 1)

        imgRotacionada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))

        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem rotacionada 90", imgRotacionada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def scale(self, image1):
        imgOriginal = cv2.imread(image1)

        imgModificada = cv2.resize(imgOriginal, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem modificada", imgModificada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def reflect(self, image1):
        imgOriginal = cv2.imread(image1)
        res = cv2.resize(imgOriginal, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        totalLinhas, totalColunas, x = res.shape

        imageReflect = cv2.flip(imgOriginal, 1)



        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem rotacionada 90", imageReflect)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    pi = PI()

    image1 = "imagens/lena.png"
    image2 = "imagens/lenainverted.png"
    #DESCOMENTE UMA DAS 3 FUNÇÕES ABAIXO PARA QUE ELA SEJA EXECUTADA

    #pi.translate(image1)
    #pi.scale(image1)
    #pi.rotate(image1)
    pi.reflect(image1)


