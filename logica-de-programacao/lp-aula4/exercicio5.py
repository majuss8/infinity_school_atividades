i = 1
qtdeFortaleza = qtdeCeara = qtdeFerroviario = qtdeIcasa = qtdeOutros = 0
salarioFortal = salarioCeara = salarioFerroviario = salarioIcasa = salarioOutros = 0
moradoresFortal = moradoresCaucaia = outros = 0

while i <= 5:
    time = int(input('Qual seu time do coração? \n1 - Fortaleza \n2 - Ceará \n3 - Ferroviário \n4 - Icasa \n6 - Outros'))
    lugar = int(input('Onde você mora? \n1 - Fortaleza \n2 - Caucaia \n 3 - Outros'))
    salario = float(input('Qual seu salário? \n'))

    if time == 1:
        qtdeFortaleza += 1
        salarioFortal += salario
        if lugar == 1:
            moradoresFortal += 1
        elif lugar == 2:
            moradoresCaucaia += 1
        else:
            outros += 1

    elif time == 2:
        qtdeCeara += 1
        salarioCeara += salario
        if lugar == 1:
            moradoresFortal += 1
        elif lugar == 2:
            moradoresCaucaia += 1
        else:
            outros += 1
        
    elif time == 3:
        qtdeFerroviario += 1
        salarioFerroviario += salario
        if lugar == 1:
            moradoresFortal += 1
        elif lugar == 2:
            moradoresCaucaia += 1
        else:
            outros += 1

    elif time == 4:
        qtdeIcasa += 1
        salarioIcasa += salario
        if lugar == 1:
            moradoresFortal += 1
        elif lugar == 2:
            moradoresCaucaia += 1
        else:
            outros += 1

    else:
        qtdeOutros += 1
        salarioOutros += salario
        if lugar == 1:
            moradoresFortal += 1
        elif lugar == 2:
            moradoresCaucaia += 1
        else:
            outros += 1    

    i += 1

mediaSalarioFortal = salarioFortal / qtdeFortaleza

print(f'Quantidade de pessoas por clube: \nClube Fortaleza: {qtdeFortaleza} \nClube Ceará: {qtdeCeara} \nClube Ferroviário: {qtdeFerroviario} \nClube Icasa: {qtdeIcasa} \nOutros: {qtdeOutros}')
print(f'Média salarial dos torcedores do Fortaleza: {mediaSalarioFortal}')
