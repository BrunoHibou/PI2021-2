import PIL.Image, PIL.ImageTk
from tkinter import filedialog
from tkinter import *
from os import path
def abrirArquivo():
    # Arquivo a ser encontrado as imagens
    folder = './imagens'
    # Tipo de arquivos que podem ser abertos
    types = [('image files', '*.png *.jpeg *.jpg *.gif *.jpe *.bmp')]
    
    # É criado uma janela de dialogo para encontrar a imagem dos tipos acima
    filename = filedialog.askopenfilename(
        title='Escolha uma imagem',
        initialdir=folder,
        filetypes=types
    )
    imageWindow(filename)
    # Retorna o nome do arquivo encontrada para que seja manipulado como imagem
    # return filename

class imageWindow:
    # A janela possui uma imagem para ser mostrada
    src : Image

    @staticmethod
    def criarJanela(img):
        # Cria janela principal
        root = Toplevel()
        root.title('Imagem')

        # Cria label com Imagem
        image_label = Label(root, image=img)
        image_label.image = img
        image_label.pack()

        root.mainloop()
    
    def __init__(self, filename):
        # Abre a propria imagem por meio do filename
        self.src = PIL.Image.open(filename)
        # Transforma a Image em ImageTK para er ua
        image = PIL.ImageTk.PhotoImage(self.src)

        self.criarJanela(image)

# imageWindow()