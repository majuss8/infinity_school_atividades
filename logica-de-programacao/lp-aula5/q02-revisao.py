somaTotalPeso = somaTotalIdade = qtdTotalJogadores = 0

for i in range(3):
    somaPeso = somaIdade = qtdJogadores = 0

    pesoJogadores = []
    idadeJogadores = []
    
    maiorPeso = menorIdade = 0

    for i in range(3):
        peso = float(input('Informe o peso do jogador: '))
        idade = int(input('Informe a idade do jogador: '))
        
        somaPeso += peso
        somaIdade += idade
        qtdJogadores += 1

        pesoJogadores.append(peso)
        idadeJogadores.append(idade)

        for peso in pesoJogadores:
            if maiorPeso == 0 or peso > maiorPeso:
                maiorPeso = peso
    
        for idade in idadeJogadores:
            if menorIdade == 0 or idade < menorIdade:
                menorIdade = idade

    mediaPeso = somaPeso / qtdJogadores
    mediaIdade = somaIdade / qtdJogadores

    print(f'A média do peso dos jogadores desse time é {mediaPeso}')
    print(f'A média da idade dos jogadores desse time é {mediaIdade}')
    print(f'O atleta mais pesado desse time tem {maiorPeso} Kg')
    print(f'O atleta mais novo desse time tem {menorIdade} anos')

    somaTotalPeso += somaPeso
    somaTotalIdade += somaIdade
    qtdTotalJogadores += qtdJogadores

pesoMedioTotal = somaTotalPeso / qtdTotalJogadores
idadeMediaTotal = somaTotalIdade / qtdTotalJogadores

print(f'A média total do peso dos participantes do campeonato é de {pesoMedioTotal}')
print(f'A média total da idade dos participantes do campeonato é de {idadeMediaTotal}')

