import tkinter as Tk

import PIL.Image as pimg
import numpy as np
# módulo referente às transformações
from PIL import ImageTk


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
    def addition(self, image1, image2, root):

        result = image1
        #percorre cada celula das matrizes dasimagens e, para cada par de pixels, realiza a soma entre eles.
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):

                result[index][index2] = image1[index][index2] + image2[index][index2]

        #converte a matriz resultante resultado em uma imagem
        result = pimg.fromarray(result)

        #converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = ImageTk.PhotoImage(result)

        #Adiciona a imagem na grid da interface
        label = Tk.Label(root, image=result)
        label.image = result
        label.grid(row=0, column=3, rowspan=13)

    # função que realiza a subtração entre uma imagem A e uma imagem B
    def subtraction(self, image1, image2, root):
        result = image1
        # percorre cada celula das matrizes dasimagens e, para cada par de pixels, realiza a subtração entre eles.
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                result[index][index2] = image1[index][index2] - image2[index][index2]

        # converte a matriz resultante resultado em uma imagem
        result = pimg.fromarray(result)

        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = ImageTk.PhotoImage(result)

        # Adiciona a imagem na grid da interface
        label = Tk.Label(root, image=result)
        label.image = result
        label.grid(row=0, column=3, rowspan=13)

    # função que realiza a multiplicação entre uma imagem A e uma imagem B
    def multiplication(self, image1, image2, root):
        result = image1
        # percorre cada celula das matrizes dasimagens e, para cada par de pixels, realiza a subtração entre eles.
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                #Aqui os valores são normalizados de forma a, no final, encontrar um valor entre 1 e 255. Caso não seja feita a divisão
                # a grande maioria das transformações retornariam uma imagem completamente branca.
                a = image1[index][index2] / 255
                b = image2[index][index2] / 255
                total = a * b
                result[index][index2] = total * 255
        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = pimg.fromarray(result)
        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = ImageTk.PhotoImage(result)
        # Adiciona a imagem na grid da interface
        label = Tk.Label(root, image=result)
        label.image = result
        label.grid(row=0, column=3, rowspan=13)

    # função que realiza a divisão entre uma imagem A e uma imagem B
    def division(self, image1, image2, root):

        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                # Aqui os valores são normalizados de forma a, no final, encontrar um valor entre 1 e 255. Caso não seja feita a divisão
                # a grande maioria das transformações retornariam uma imagem errônea
                a = image1[index][index2] * 255
                b = image2[index][index2] * 255
                total = a / b
                result[index][index2] = total * 255
        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = pimg.fromarray(result)
        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = ImageTk.PhotoImage(result)
        # Adiciona a imagem na grid da interface
        label = Tk.Label(root, image=result)
        label.image = result
        label.grid(row=0, column=3, rowspan=13)

    def translate(self):
        pass

    def rotate(self):
        pass

    def scale(self):
        pass

    def reflect(self):
        pass


if __name__ == "__main__":
    pi = PI()

    image1 = "imagens/lena.png"
    image2 = "imagens/lenainverted.png"

    image1 = pi.image_to_matrix(image1)

    image2 = pi.image_to_matrix(image2)

    image3 = pimg.fromarray(pi.addition(image1, image2))
    image3.show()