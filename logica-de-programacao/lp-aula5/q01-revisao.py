somaDeConsumoResidencial = somaDeConsumoComercial = somaDeConsumoIndustrial = 0
qtdResidencial = qtdComercial = 0

numero = int(input('Informe o número do cliente: '))

while numero != 0:
    kwh = int(input('Informe a quantidade de Kwh: '))
    tipo = int(input('Informe tipo de consumidor: \n1 - Residencial \n2 - Comercial \n3 - Industrial \n'))

    if tipo == 1:
        conta = kwh * 0.3
        print(f'Custo total: R$ {conta}')
        somaDeConsumoResidencial += conta
        qtdResidencial += 1
    elif tipo == 2:
        conta = kwh * 0.5
        print(f'Custo total: R$ {conta}')
        somaDeConsumoComercial += conta
        qtdComercial += 1
    else: 
        conta = kwh * 0.7
        print(f'Custo total: R$ {conta}')
        somaDeConsumoIndustrial += conta


    numero = int(input('Informe o número do cliente ou 0 para sair: '))

mediaResidencial = somaDeConsumoResidencial / qtdResidencial
mediaComercial = somaDeConsumoComercial / qtdComercial

print(f'Consumo total do tipo Residencial: {somaDeConsumoResidencial}')
print(f'Consumo total do tipo Comercial: {somaDeConsumoComercial}')
print(f'Consumo total do tipo Industrial: {somaDeConsumoIndustrial}')
print(f'Média do consumo do tipo Residencial: {mediaResidencial}')
print(f'Média do consumo do tipo Comercial: {mediaComercial}')


