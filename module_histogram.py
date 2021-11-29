import numpy as np
import matplotlib.pyplot as plt
from module_transform import PI
from PIL import Image

image = "imagens/lena.png"
image2 = "imagens/lenainverted.png"

pi = PI()
data = pi.image_to_matrix(image)

nk = [0]*256
pr = [0.0]*256
freq = [0.0]*256
equa = [0.0]*256
rk = [0.0]
k = 0


def histograma():
    hist = plt.hist(data, bins='auto')
    plt.ylim([0, 60])
    plt.show()


def cinza(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x, y))
            lum = (pxl + pxl + pxl) // 3
            img.putpixel((x, y), (lum, lum, lum))
    return img


def equaliza(negativa):
    # coloca nas variáveis tamanho e altura respectivamente da imagem passada no parâmetro
    w, h = negativa.size
    # passa toda a matriz com seus valores RGB criando a imagem na variável "img"
    img = Image.new("RGB", (w, h))

    # percorre a matriz em x para tamanho
    for x in range(w):
        # percorre a matriz em y para altura
        for y in range(h):
            # Seta os pixels da imagem passada na posição x e y para a variável "pxl"
            pxl = negativa.getpixel((x, y))
            # faz o calculo da luminosidade da imagem
            lum = (255 - 1 - pxl[0])
            # coloca o valor da luminosidade calculada nos pixels da nova imagem
            img.putpixel((x, y), (lum, lum, lum))
    return img


def graficos(histograma):
    # coloca nas variáveis tamanho e altura respectivamente da imagem passada no parâmetro
    w, h = histograma.size

    # passa toda a matriz com seus valores RGB criando a imagem na variável "img"
    img = Image.new("RGB", (w, h))
    i = 0
    j = 0
    # percorre a matriz em x para tamanho
    for x in range(w):
        # percorre a matriz em y para altura
        for y in range(h):
            # Seta os pixels da imagem passada na posição x e y para a variável "pxl"
            pxl = histograma.getpixel((x, y))
            # Faz a média dos valores RGB do pixel e o coloca na variável "lum"
            lum = (pxl + pxl + pxl) // 3
            print(lum)


def equalizar(normalizar):
    # coloca nas variáveis tamanho e altura respectivamente da imagem passada no parâmetro
    w, h = normalizar.size

    # passa toda a matriz com seus valores RGB criando a imagem na variável "img"
    img = Image.new("RGB", (w, h))
    i = 0
    j = 0
    # percorre a matriz em x para tamanho
    for x in range(w):
        # percorre a matriz em y para altura
        for y in range(h):
            # Seta os pixels da imagem passada na posição x e y para a variável "pxl"
            pxl = normalizar.getpixel((x, y))
            # calcula o valor de nk
            nk[pxl[0]] = nk[pxl[0]] + 1

            # calcula o valor de pr
            pr[pxl[0]] = nk[pxl[0]] / (w * h)

    # esta função define a frenquência da soma normalizada
    for j in range(len(pr)):
        if (j == 0):
            freq[j] = pr[j]
        freq[j] = pr[j] + freq[j - 1]

    # esta função calcula e define o Look-Up Table
    for j in range(len(pr)):
        if (j == 0):
            equa[j] = 255 * pr[j]
        equa[j] = 255 * pr[j] + equa[j - 1]

    # Passa os novos valores para os pixels da nova imagem e então retorna a imagem
    for x in range(w):
        for y in range(h):
            pxl = normalizar.getpixel((x, y))
            rk[0] = round(equa[pxl[0]])
            lum = (rk[0])
            img.putpixel((x, y), (lum, lum, lum))
    return img


sol = Image.open("sol.jpg")
pb_sol = cinza(sol)
pb_sol.save("sol_cinza.jpg")
solcinza = Image.open("sol_cinza.jpg")
ng_sol = equaliza(solcinza)
ng_sol.save("sol_negativado.jpg")

# print(data_array)
# # print(len(data))
# plt.hist(data_array, bins='auto')
# # plt.ylim([0, 60])
# plt.show()