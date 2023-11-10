from tkinter import *
# código calculadora: https://www.invertexto.com/514aula10python
janelaPrincipal = Tk()
janelaPrincipal.title('Calculadora')

#Criar funções - ações
def inserir(valor):
    visor.insert(END, valor)

def limpar():
    visor.delete(0,END)


def calcular():
    texto_visor = visor.get() #Pegar os números
    resultado = eval(texto_visor)
    visor.delete(0, END)
    visor.insert(0, str(resultado))


#Entry = Input
visor = Entry(janelaPrincipal, font='Arial 20 bold', bg='#00FFFF', fg='#000000', width=19)
visor.pack()

#Criar painel para inserir os botões
panel = Frame(janelaPrincipal)

#criar os botões
botao_1 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='1', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command= lambda: inserir('1')
                 )

botao_2 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='2', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command= lambda: inserir('2')
                 )


botao_3 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='3', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command= lambda: inserir('3')
                 )

botao_soma = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='+', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('+')
                 )


botao_4 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='4', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('4')
                 )

botao_5 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='5', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('5')
                 )


botao_6 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='6', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('6')
                 )

botao_multi = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='*', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('*')
                 )


botao_7 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='7', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('7')
                 )

botao_8 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='8', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('8')
                 )


botao_9 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='9', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('9')
                 )

botao_divisao = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='/', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('/')
                 )



botao_0 = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='0', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('0')
                 )

botao_calcular = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='=', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: calcular()
                 )


botao_limpar = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='C', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: limpar()
                 )

botao_subtracao = Button(panel, bg="#D5D6D6",
                 bd=1,
                 text='-', #APARECER PARA O USUARIO
                 font='Arial 16 bold',
                 fg='#000000',
                 width=5, height=3,
                 command=lambda: inserir('-')
                 )


#ativar o panel
panel.pack()


#primeira linha
botao_7.grid(row=0, column=0)
botao_8.grid(row=0, column=1)
botao_9.grid(row=0, column=2)
botao_divisao.grid(row=0, column=3)

#segunda linha
botao_4.grid(row=1, column=0)
botao_5.grid(row=1, column=1)
botao_6.grid(row=1, column=2)
botao_multi.grid(row=1, column=3)

#terceira linha
botao_1.grid(row=2, column=0)
botao_2.grid(row=2, column=1)
botao_3.grid(row=2, column=2)
botao_soma.grid(row=2, column=3)


#quarta linha
botao_0.grid(row=3, column=0)
botao_calcular.grid(row=3, column=1)
botao_limpar.grid(row=3, column=2)
botao_subtracao.grid(row=3, column=3)

mainloop()
