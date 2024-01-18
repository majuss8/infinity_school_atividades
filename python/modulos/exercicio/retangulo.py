import moduloFuncoes

# 1
# base = float(input('Informe a base do retângulo: '))
# altura = float(input('Informe a altura do retângulo: '))

# perimetro = moduloFuncoes.perimetro(base, altura)
# area = moduloFuncoes.area(base, altura)
# diagonal = moduloFuncoes.diagonal(base, altura)

# print(f'O perímetro desse retângulo é: {perimetro}')
# print(f'O área desse retângulo é: {area}')
# print(f'O diagonal desse retângulo é: {diagonal}')

# 2
# num = float(input('Informe um número: '))
# resultado = moduloFuncoes.validacao(num)
# print(resultado)

# 3
# raio = float(input('Informe o raio do circulo: '))
# print(moduloFuncoes.areaCirculo(raio))

# 4 
# numeros = [9, 16, 20, 25, 42]
# for n in numeros:
#     print(moduloFuncoes.raiz(n))
    
# 5
# cateto1 = float(input('Informe o valor do primeiro cateto: '))
# cateto2 = float(input('Informe o valor do segundo cateto: '))

# print(f'A hipotenusa vale: {moduloFuncoes.teorema(cateto1, cateto2)}')

# 6
# raioCilindro = float(input('Informe o valor do raio do cilindro: '))
# alturaCilindro = float(input('Informe o valor da altura do cilindro: '))
# print(f'O volume do cilindro é: {moduloFuncoes.volumeCilindro(raioCilindro, alturaCilindro)}')

# 7
numDeCandidatos = int(input('Informe o número de candidatos: '))
candidatos = []
while True:
    nome = input('Informe o nome do candidato: ')
    candidatos.pop(nome)
