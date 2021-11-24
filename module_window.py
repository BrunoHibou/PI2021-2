from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter as gui

class Janela_imagem:
    MAX_SIZE = 480
    src : Image
    # Função para Abrir a imagem numa Janela  
    @staticmethod
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
        # Retorna o nome do arquivo encontrada para que seja manipulado como imagem
        return filename

    # Função para Redimensionar uma a imagem
    def dimensionarImagem(self, max_size):
        width = self.src.width
        height = self.src.height

        # Redimesiona a imagem caso seja maior
        if(width > max_size or height > max_size):            
            
            # A escala é dada como o quantidade 
            # de vezes que a altura e a largura 
            # for maior do que o tamanho maximo
            height_scale = (height // max_size)
            width_scale = (width // max_size)  
            # Pega a escala menor 
            scale = min(height_scale, width_scale)
            
            # É preciso usar o mesmo valor na divisão
            # para garantir que a imagem não vai ser 
            # destorcida durante o redimensionamento  
            
            # E divide as medidas pela escala dada
            new_width = width//scale
            new_height = height//scale

            # Depois basta colocar o novo tamanho nos da imagem e   
            # atribuir a  ela mesma a nova imagem redimesionada 
            nova_imagem = self.src.resize(size=[new_width, new_height])

            return nova_imagem

    def __init__(self):
        # O nome da imagem encontrado
        filename = self.abrirArquivo()
        # A imagem pode ser aberta pelo seu nome
        self.src = Image.open(filename)
        # A dimensÕes da imagem encontrada
        dimensions = f'{self.src.width}x{self.src.height}'

        ### TRATANDO A IMAGEM
        # Redimesionando a imagem selecionada
        img_reduzida = self.dimensionarImagem(self.MAX_SIZE)
 
        # A imagem pode ser transforma em Tk Image
        img_alterada = ImageTk.PhotoImage(img_reduzida)
        
        ### CRIANDO A JANELA PARA IMAGEM
        # Janela para imagem
        root = gui.Toplevel()
        root.title('Imagem selecionada')

        # Label da imagem 
        image_label = gui.Label(root, image=img_alterada)
        image_label.image = img_alterada
        
        # Label da legenda 
        legenda_label = gui.Label(root, text=filename)
        size_label = gui.Label(root, text=dimensions)
        
        # Empacotando e rodando as coisas
        size_label.pack()
        image_label.pack()
        legenda_label.pack()
        root.mainloop()