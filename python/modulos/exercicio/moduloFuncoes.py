import math

def perimetro(b, h):
    return 2 * (b + h)

def area(b, h):
    return b * h

def diagonal(b, h):
    return math.sqrt(b**2 + h**2)

def validacao(num):
    raiz = math.sqrt(num)
    if raiz == int(math.sqrt(num)):
        return f'A raiz desse número ( {raiz} ) é exata'
    else:
        return f'A raiz desse número ( {raiz} ) não é exata'
    
def areaCirculo(raio):
    return round(math.pi * (raio ** 2), 2)

def raiz(num):
    return round(math.sqrt(num), 2)

def teorema(c1, c2):
    return round(math.hypot(c1, c2), 2)

def volumeCilindro(r, h):
    return round(math.pi * r ** 2 * h, 2)

