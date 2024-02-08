from tkinter import *

lista_habilidades = []
def opcao():

    html = html_var.get()
    css = css_var.get()
    js = js_var.get()
    python = python_var.get()

    if html == True:
        lista_habilidades.append("HTML")
    if css == True:
        lista_habilidades.append("CSS")
    if js == True:
        lista_habilidades.append("Javascript")
    if python == True:
        lista_habilidades.append("Python")
    
    return lista_habilidades
    

listaAlunos = {}
def cadastrar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    genero = genero_var.get()
    listaAlunos = {
        "Nome": nome,
        "Idade": idade,
        "Genero": genero,
        "Habilidades": opcao()
    }
    print(listaAlunos)

janela = Tk()
janela.geometry("600x400+350+150")
janela.minsize(400,200)
janela.maxsize(800,600)

label_nome = Label(
    janela,
    text="Nome: ",
    fg="black",
    font=("Arial", 15, "bold")
)

entrada_nome = Entry(janela)

label_idade = Label(
    janela,
    text="Idade: ",
    fg="black",
    font=("Arial", 15, "bold")
)

entrada_idade = Entry(janela)

label_genero = Label(
    janela,
    text="Gênero: ",
    fg="black",
    font=("Arial", 15, "bold")
)

genero_var = StringVar() 
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

label_habilidades = Label(
    janela,
    text="Habilidades: ",
    fg="black",
    font=("Arial", 15, "bold")
)
python_var = BooleanVar() 
js_var = BooleanVar() 
html_var = BooleanVar() 
css_var = BooleanVar() 

python = Checkbutton(
    janela,
    text="Python",
    variable= python_var
)
html = Checkbutton(
    janela,
    text="HTML",
    variable= html_var
)
css = Checkbutton(
    janela,
    text="CSS",
    variable= css_var
)
js = Checkbutton(
    janela,
    text="Javascript",
    variable= js_var
)

label_nota1 = Label(
    janela,
    text="Nota 1: ",
    fg="black",
    font=("Arial", 15, "bold")
)

entrada_nota1 = Entry(janela)

label_nota2 = Label(
    janela,
    text="Nota 2: ",
    fg="black",
    font=("Arial", 15, "bold")
)

entrada_nota2 = Entry(janela)

btn_cadastrar = Button(
    janela,
    text="Cadastrar",
    command= cadastrar
)

# aluno = {
#     nome: entrada_nome,
#     idade: entrada_idade,
#     genero: genero_var,
#     habilidade: habilidade_var,
#     nota1: entrada_nota1,
#     nota2: entrada_nota2
# }

label_nome.grid(column=0, row=0, padx=15, pady=5)
entrada_nome.grid(column=0, row=1, padx=15, pady=5)

label_idade.grid(column=0, row=2, padx=15, pady=5)
entrada_idade.grid(column=0, row=3, padx=15, pady=5)

label_genero.grid(column=0, row=4, padx=15, pady=5)
feminino.grid(column=0, row=5, padx=5, pady=5)
masculino.grid(column=1, row=5, padx=5, pady=5)
outros.grid(column=2, row=5, padx=5, pady=5)

label_habilidades.grid(column=0, row=6, padx=15, pady=5)
python.grid(column=0, row=7, padx=5, pady=5)
js.grid(column=1, row=7, padx=5, pady=5)
html.grid(column=2, row=7, padx=5, pady=5)
css.grid(column=3, row=7, padx=5, pady=5)

label_nota1.grid(column=0, row=8, padx=15, pady=5)
entrada_nota1.grid(column=0, row=9, padx=15, pady=5)
label_nota2.grid(column=1, row=8, padx=15, pady=5)
entrada_nota2.grid(column=1, row=9, padx=15, pady=5)

btn_cadastrar.grid(column=0, row=10, columnspan=2, padx=10)
janela.mainloop()