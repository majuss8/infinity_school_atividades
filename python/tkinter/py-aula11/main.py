from tkinter import *

janela = Tk()
janela.title("Biblioteca")

# label = Label(
#     janela,
#     text="Quais suas habilidades?"
# )

# check1_var = BooleanVar()
# check1 = Checkbutton(
#     janela,
#     text="Python",
#     variable=check1_var
# )

# check2_var = BooleanVar()
# check2 = Checkbutton(
#     janela,
#     text="Javascript",
#     variable=check2_var
# )

# label.pack()
# check1.pack()
# check2.pack()

label = Label(
    janela,
    text="Gênero: ",
    fg="purple",
    font=("Arial", 20, "bold")
)
genero_var = StringVar() # verifica qual opção foi marcada
feminino = Radiobutton(
    janela,
    text="Feminino",
    variable= genero_var,
    value= "feminino"
)
masculino = Radiobutton(
    janela,
    text="Masculino",
    variable= genero_var,
    value= "masculino"
)
outros = Radiobutton(
    janela,
    text="Outros",
    variable= genero_var,
    value= "outros"
)

label.pack()
feminino.pack()
masculino.pack()
outros.pack()

janela.mainloop()