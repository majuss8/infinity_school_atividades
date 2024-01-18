import meuModulo as m
import math as mat
import random 
import time
import tkinter

nome = input('Informe o nome: ')

m.boasVindas(nome)

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Informe o segundo número: '))

resultado = m.multiplicar(numero1, numero2)

print(resultado)