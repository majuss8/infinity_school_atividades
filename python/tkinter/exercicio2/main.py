from tkinter import *
from tkinter import messagebox

def imprimirNome():
    messagebox.showinfo("mensagem", "Olá " + str(caixa_nome.get()))

window = Tk()

window.geometry("600x400+350+150") 
window.minsize(400, 200)
window.maxsize(800, 600)

nome = Label(
    window, 
    text="Insira seu nome: ",
    fg="black",    
    font=("Arial", 20, "bold")     

    )

caixa_nome = Entry(cursor="spider")

btn = Button(
    window,
    bg="green",
    text="Confirmar",
    command=imprimirNome
)

nome.pack(side="left")
caixa_nome.pack(side="left")
btn.pack(side="left")
window.mainloop() 
