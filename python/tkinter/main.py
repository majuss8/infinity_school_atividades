from tkinter import *

def somar():
    soma = int(caixa_num1.get()) + int(caixa_num2.get()) 
    print("Resultado: ", soma)

janela = Tk() # criação da janela
janela.title("Calculadora")
janela.iconbitmap("img/calculadoraIcon.ico")
janela.geometry("600x400+350+150") 
# janela.resizable(False, False) # bloquear o usuário de alterar as dimensoes
janela.minsize(400, 200)
janela.maxsize(800, 600)

num1 = Label(
    janela, 
    text="Informe o primeiro valor: ",
    fg="purple",    
    font=("Arial", 20, "bold")     
    )

num2 = Label(
    janela, 
    text="Informe o segundo valor: ",
    fg="purple",    
    font=("Arial", 20, "bold")     
    )

caixa_num1 = Entry(cursor="heart")
caixa_num2 = Entry(cursor="spider")
btn_calcular = Button(
    janela,
    text="Calcular",
    command=somar
)

num1.pack()
caixa_num1.pack()
num2.pack()
caixa_num2.pack()
btn_calcular.pack()
janela.mainloop() 

