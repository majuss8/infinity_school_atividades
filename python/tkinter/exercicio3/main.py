from tkinter import *

janela = Tk()
janela.geometry("500x500+350+150")

btn1 = Button(
    janela,
    text="1"
)

btn2 = Button(
    janela,
    text="2"
)

btn3 = Button(
    janela,
    text="3"
)

btn4 = Button(
    janela,
    text="4"
)

btn5 = Button(
    janela,
    text="5"
)

btn6 = Button(
    janela,
    text="6"
)

btn1.grid(column=0,row=0,columnspan=3)

btn2.grid(column=0,row=2,columnspan=2)

btn3.grid(column=1,row=2,columnspan=3)

btn4.grid(column=0,row=3)

btn5.grid(column=1,row=3)

btn6.grid(column=2,row=3)

janela.mainloop()