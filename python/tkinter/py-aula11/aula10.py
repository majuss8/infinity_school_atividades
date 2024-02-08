from tkinter import ttk
from tkinter import *
# from tkinter.ttk import *

janela = Tk()
janela.title("Biblioteca")

dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

listaSemana = ttk.Combobox(
    janela,
    values= dias
)

listaSemana.pack()
janela.mainloop()