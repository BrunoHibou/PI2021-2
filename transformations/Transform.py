import numpy as np
import PIL.Image as pimg


# módulo referente às transformações
class PI:

    def image_to_matrix(self, img):
        image = pimg.open(img).convert("L")
        image_array = np.matrix(image)
        image_array = np.squeeze(image_array)
        return image_array

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
                result[index][index2] = (image1[index][index2]) * (image2[index][index2])

        return result

    # função que realiza a divisão entre uma imagem A e uma imagem B
    def division(self, image1, image2):
        result = image1
        for index in range(len(image1)):
            for index2 in range(len(image1[index])):
                result[index][index2] = image1[index][index2] / image2[index][index2]

        return result


if __name__ == "__main__":
    pi = PI()

    image1 = "../imagens/lena.png"
    image2 = "../imagens/lenainverted.png"

    image1 = pi.image_to_matrix(image1)

    image2 = pi.image_to_matrix(image2)

    image3 = pimg.fromarray(pi.multiplication(image1, image2))
    image3.show()

