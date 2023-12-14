carros = {}

for i in range(2):
    nomeCarro = str(input('Informe o nome do carro: '))
    kmPorLitro = float(input('Informe quantos quilômetros por litro o carro faz: '))

    carros[f'veiculo {i + 1}'] = {'nome': nomeCarro, 'km-por-litro': kmPorLitro}

print(carros)

maior = 0

for veiculo in carros:
    if carros[veiculo]['kmPorLitro'] > maior:
        maior = carros[veiculo]['kmPorLitro']
        modelo = carros[veiculo]['nomeCarro']
    print(f'O modelo mais econômico é o {modelo} - {maior}')

for veiculo in carros:
    litros = carros[veiculo]['kmPorLitro'] * 1000
    custo = litros * 5.25
    print(f'Em uma distância de 1000 km o {carros[veiculo][nomeCarro]} consome {litros} litros de gasolina, custando R${custo}')


