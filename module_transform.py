import math
import tkinter as Tk
import numpy as np
import cv2
import PIL.Image as pimg
# módulo referente às transformações
from PIL import ImageTk


class PI:

    def image_to_matrix(self, img_filename):

        image = pimg.open(img_filename).convert("L")

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
        # print(matriz_pixel[0][0])
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

    def translate(self, image1):
        #Lê a imamgem original e passa os pixels dela para a variável
        imgOriginal = cv2.imread(image1)
        #Através da função .shape lê o numero de linhas e colunas da variável e passa para as duas variáveis respectivamente
        totalLinhas, totalColunas = imgOriginal.shape[:2]
        #Passa a variável imgOriginal para a variável res com seu tamanho normal
        res = cv2.resize(imgOriginal, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        #Define a matriz de multiplicação sendo x' e y' que serão multiplicados pela matriz da imagem original
        matriz = np.float32([[1, 0, 100], [0, 1, 100]])
        #Faz a multiplicação da "matriz" de multiplicação com "totallinhas" e "totalcolulas" para definir a nova posição da imagem original
        #e coloca os novos valores em "imgDeslocada" com os pixels de "res" que é a imagem original
        imgDeslocada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))

        #Mostra as duas imagens
        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem Deslocada", imgDeslocada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rotate(self, image, angle, root):


        #abre a imagem
        imgOriginal = cv2.imread(image)

        #maumenta a escala da imagem
        res = cv2.resize(imgOriginal, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

        #atribui o valor total de linhas e colunas de acordo com o formato da imagem. (linhas x columas)
        totalLinhas, totalColunas, x = res.shape

        #gera a matriz de rotação referente à imagem no ângulo determinado pela variável "angle"
        matriz = cv2.getRotationMatrix2D((totalColunas / 2, totalLinhas / 2), angle, 1)

        #multiplica a matriz pela imagem retornando a imagem rotacionada no ângulo "angle"
        imgRotacionada = cv2.warpAffine(res, matriz, (totalColunas, totalLinhas))


        #mostra a original e a imagem rotacionada
        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem rotacionada em um angulo", imgRotacionada)

        # fecha as telas após pressionar uma tecla
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    def scale(self, image1):
        # Lê a imamgem original e passa os pixels dela para a variável
        imgOriginal = cv2.imread(image1)
        #Através da função de interpolação bicubica com x' e y' = 0,5 multiplicando a imagem inicial, o tamanho dela é modificado e setado na variável
        img_modificada = cv2.resize(imgOriginal, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

        # Mostra as duas imagens
        cv2.imshow("Imagem original", imgOriginal)
        cv2.imshow("Imagem modificada", img_modificada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def reflect(self, image, axis, root):

        result = []
        aux = image

        #Caso axis = x realizamos a operação ao redor do eixo x
        if axis == "x":
            #Percorremos cada lista de linhas dentro de imagem de trás pra frente invertendo as listas e portanto a imagem
            for p in range(len(aux)-1, -1, -1):
                result.append(aux[p])

        #Caso axis = y realizamos a operação ao redor do eixo y
        if axis == "y":
            #percorrer a imagem invertendo a ordem das colunas e na imagem
            for p in image:
                p = np.flip(p)
                result.append(p)


        result = np.asarray(result)
        result = pimg.fromarray(result)
        # converte a imagem em uma PhotoImage da biblioteca ImageTK
        result = ImageTk.PhotoImage(result)
        # Adiciona a imagem na grid da interface
        label = Tk.Label(root, image=result)
        label.image = result
        label.grid(row=0, column=3, rowspan=13)



if __name__ == "__main__":
    pi = PI()

    image1 = "imagens/lena.png"
    image2 = "imagens/lenainverted.png"
    #DESCOMENTE UMA DAS 3 FUNÇÕES ABAIXO PARA QUE ELA SEJA EXECUTADA

    pi.translate(image1)
    #pi.scale(image1)
    #pi.rotate(image1, 90, None)
    #pi.reflect(image1)
