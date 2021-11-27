from tkinter import *
from module_image import abrirArquivo
from PIL import Image, ImageTk
import module_transform as transform


class mainWindow():



    def __init__(self):
        # cria a janela
        window = Tk()
        window.title("Processador de Imagens")
        button_frame = Frame()
        # cria a barra de ferramentas
        menubar = Menu(window)
        window.config(menu=menubar)

        menu_file = Menu(menubar, tearoff=False)
        menu_file.add_command(label='Abrir arquivo', command=lambda: abrirArquivo())
        menubar.add_cascade(label='Arquivo', menu=menu_file)

        # Texto referente ao caminho das imagens
        images = Label(window, text="título das imagens")
        images.grid(column=0, row=0, padx=10, pady=10)

        # Text Fields que tem o caminho das imagens
        path1 = Text(window, height=1, width=5)
        path1.grid(column=0, row=1, padx=10, sticky=N + S + W + E)

        path2 = Text(window, height=1, width=5)
        path2.grid(column=0, row=2, padx=10, sticky=N + S + W + E)

        # Botão de Abrir as duas imagens
        button1 = Button(window, text="Abrir Imagens", command=lambda: self.set_image(root=window, text_field=path1,text_field2= path2))
        button1.grid(column=0, row=3, padx=10, sticky=N + S + W + E)
        button1.anchor(NW)

        # Parte referente aos botòes de Transformações Aritméticas
        ari = Label(window, text="Transformações Aritméticas")
        ari.grid(column=0, row=4, padx=10, pady=10)

        # Adição
        button1 = Button(window, text="Adittion", command=lambda: transform.addition())
        button1.grid(column=0, row=5, padx=10, sticky=N + S + W + E)
        button1.anchor(NW)

        # Sugtração
        button2 = Button(window, text="Subtraction", command=lambda: print("sub"))
        button2.grid(column=0, row=6, padx=10, sticky=N + S + W + E)

        # Multiplicação
        button3 = Button(window, text="Multiplication", command=lambda: print("mult"))
        button3.grid(column=0, row=7, padx=10, sticky=N + S + W + E)

        # Divisão
        button4 = Button(window, text="Division", command=lambda: print("div"))
        button4.grid(column=0, row=8, padx=10, sticky=N + S + W + E)

        # Parte referente aos botòes de Transformações Geométricas
        geom = Label(window, text="Transformações Geométricas")
        geom.grid(column=0, row=9, padx=10, pady=10, sticky=N + S + W + E)

        # Translação
        button5 = Button(window, text="Translação", command=lambda: print("add"))
        button5.grid(column=0, row=10, padx=10, sticky=N + S + W + E)
        button5.anchor(NW)

        # Rotação
        button6 = Button(window, text="Rotação", command=lambda: print("div"))
        button6.grid(column=0, row=11, padx=10, sticky=N + S + W + E)

        # Escala
        button7 = Button(window, text="Escala", command=lambda: print("sub2"))
        button7.grid(column=0, row=12, padx=10, sticky=N + S + W + E)

        # Reflexão
        button8 = Button(window, text="Reflexão", command=lambda: print("mult2"))
        button8.grid(column=0, row=13, padx=10, sticky=N + S + W + E)

        # image Labels
        window.mainloop()

    def set_image(self,root,text_field, text_field2 ):
        image = Image.open("./imagens/"+text_field.get("1.0", "end-1c"))
        photo = ImageTk.PhotoImage(image)

        image = Image.open("./imagens/"+text_field2.get("1.0", "end-1c"))
        photo2 = ImageTk.PhotoImage(image)

        label = Label(root, image=photo)
        label.image = photo
        label.grid(row=0,column=1, rowspan = 14)

        label2 = Label(root, image=photo2)
        label2.image = photo2
        label2.grid(row=0,column=2, rowspan=14)
