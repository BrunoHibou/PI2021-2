from tkinter import *
from module_image import abrirArquivo

class mainWindow():
    def __init__(self):            
        # cria a janela
        window = Tk()
        window.title("Processador de Imagens")

        # cria a barra de ferramentas
        menubar = Menu(window)
        window.config(menu=menubar)

        menu_file = Menu(menubar, tearoff=False)
        menu_file.add_command(label = 'Abrir arquivo', command = lambda: abrirArquivo())
        menubar.add_cascade(label='Arquivo', menu=menu_file)

        # Parte referente aos botòes de Transformações Aritméticas
        ari = Label(window, text="Transformações Aritméticas")
        ari.grid(column=0, row=0, padx=10, pady=10)

        button1 = Button(window, text="Adittion", command=lambda: print("add"))
        button1.grid(column=0, row=1, padx=10, sticky=N + S + W + E)
        button1.anchor(NW)

        button2 = Button(window, text="Subtraction", command=lambda: print("sub"))
        button2.grid(column=0, row=2, padx=10, sticky=N + S + W + E)

        button3 = Button(window, text="Multiplication", command=lambda: print("mult"))
        button3.grid(column=0, row=3, padx=10, sticky=N + S + W + E)

        button4 = Button(window, text="Division", command=lambda: print("div"))
        button4.grid(column=0, row=4, padx=10, sticky=N + S + W + E)

        # Parte referente aos botòes de Transformações Geométricas
        geom = Label(window, text="Transformações Geométricas")
        geom.grid(column=0, row=5, padx=10, pady=10, sticky=N + S + W + E)

        button5 = Button(window, text="Translação", command=lambda: print("add"))
        button5.grid(column=0, row=6, padx=10, sticky=N + S + W + E)
        button5.anchor(NW)

        button6 = Button(window, text="Rotação", command=lambda: print("div"))
        button6.grid(column=0, row=7, padx=10, sticky=N + S + W + E)

        button7 = Button(window, text="Escala", command=lambda: print("sub2"))
        button7.grid(column=0, row=9, padx=10, sticky=N + S + W + E)

        button8 = Button(window, text="Reflexão", command=lambda: print("mult2"))
        button8.grid(column=0, row=10, padx=10, sticky=N + S + W + E)

        window.mainloop()
