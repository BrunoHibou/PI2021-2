import numpy as np
import matplotlib.pyplot as plt
from module_transform import PI

image = "imagens/lena.png"
image2 = "imagens/lenainverted.png"

pi = PI()
data = pi.image_to_matrix(image)

def histograma():
    hist = plt.hist(data, bins='auto')
    plt.ylim([0, 60])
    plt.show()

# def histograma_normalizado():
#     pass
# data_array = list()
# data_line = list()
# image_size = pi.image_to_matrix(image)
# for line in data:
#     for pixel in line:
#         unidade = pixel/image_size
#         data_line.append(unidade)
#     data_array.append(data_line)
# # print(data_array)
# # print(len(data))
# plt.hist(data_array, bins='auto')
# # plt.ylim([0, 60])
# plt.show()