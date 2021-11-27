import numpy
import numpy as np
import PIL.Image as pimg


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

    def translate(self):
        pass

    def rotate(self):
        pass

    def scale(self):
        pass

    def reflect(self, image1, pixels, row, column):
        b = 0
        a = 0
        result = image1
        for index in range(row):
            for index2 in range(column):
                b = self.getnewposition(index2, b, column)
                result[index][b] = pixels[index][index2]
        return result

    def getnewposition(self, j, b, column):
        b = column - j - 1
        return b

    def get_pixels(self, image1):
        pixels = numpy.asarray(image1)
        return pixels


if __name__ == "__main__":
    pi = PI()

    image1 = "imagens/lena.png"
    image2 = "imagens/lenainverted.png"

    image1 = pi.image_to_matrix(image1)
    pixels = pi.get_pixels(image1)
    row = len(pixels)
    column = len(pixels[0])

    image2 = pi.image_to_matrix(image2)

    image3 = pimg.fromarray(pi.reflect(image1, image1, row, column))
    image3.show()
