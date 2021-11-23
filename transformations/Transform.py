import numpy.matrixlib as np
import PIL.Image as pimg


# módulo referente às transformações
class PI:

    def image_to_matrix(img):
        image = pimg.open(img).convert("L")
        image_array = np.matrix(image)
        return image_array

    # função que realiza a adição entre uma imagem A e uma imagem B
    def addition(self, image1, image2):
        result = image1
        result.fill(0)
        for index, value in enumerate(image1):
            for index2, value2 in enumerate(image1[index]):
                result[index][index2] = image1[index][index2] + image2[index][index2]

        return result

    # função que realiza a subtração entre uma imagem A e uma imagem B
    def subtraction(self, image1, image2):
        result = image1
        result.fill(0)
        for index, value in enumerate(image1):
            for index2, value2 in enumerate(image1[index]):
                result[index][index2] = image1[index][index2] - image2[index][index2]

        return result

    # função que realiza a multiplicação entre uma imagem A e uma imagem B
    def multiplication(self, image1, image2):
        result = image1
        result.fill(0)
        for index, value in enumerate(image1):
            for index2, value2 in enumerate(image1[index]):
                result[index][index2] = image1[index][index2] - image2[index][index2]

        return result

    # função que realiza a divisão entre uma imagem A e uma imagem B
    def division(self, image1, image2):
        result = image1
        result.fill(0)
        for index, value in enumerate(image1):
            for index2, value2 in enumerate(image1[index]):
                result[index][index2] = image1[index][index2] - image2[index][index2]

        return result
