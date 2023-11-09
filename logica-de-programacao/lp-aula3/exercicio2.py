# Em um campeonato nacional de arco-e-flecha, tem-se
# equipes de três jogadores para cada estado. Sabendo-se
# que os arqueiros de uma equipe não obtiveram o mesmo
# número de pontos, criar um programa que informe se
# uma equipe foi classificada, de acordo com a seguinte
# especificação:

# • Ler os pontos obtidos por cada jogador da equipe;

# • Mostrar esses valores em ordem decrescente;

# • Se a soma dos pontos for maior do que 100, imprimir a
# média aritmética entre eles, caso contrário, imprimir a
# mensagem "Equipe desclassificada".

jogador1 = int(input('Número de pontos do jogador 1: '))
jogador2 = int(input('Número de pontos do jogador 2: '))
jogador3 = int(input('Número de pontos do jogador 3: '))

soma = jogador1 + jogador2 + jogador3

# if jogador1 > jogador2 and jogador1 > jogador3 and jogador2 > jogador3:
#     print(f'Pontuação do jogador 1: {jogador1} - Pontução do jogador 2: {jogador2} - Pontuação do jogador 3: {jogador3}')

# elif jogador1 > jogador2 and jogador1 > jogador3 and jogador3 > jogador2:
#     print(f'Pontuação do jogador 1: {jogador1} - Pontução do jogador 3: {jogador3} - Pontução do jogador 2: {jogador2}')

# elif jogador2 > jogador1 and jogador2 > jogador3 and jogador1 > jogador3:
#     print(f'Pontuação do jogador 2: {jogador2} - Pontução do jogador 1: {jogador1} - Pontução do jogador 3: {jogador3}')

# elif jogador2 > jogador1 and jogador2 > jogador3 and jogador3 > jogador1:
#     print(f'Pontuação do jogador 2: {jogador2} - Pontução do jogador 3: {jogador3} - Pontução do jogador 1: {jogador1}')

# elif jogador3 > jogador1 and jogador3 > jogador2 and jogador1 > jogador2:
#     print(f'Pontuação do jogador 3: {jogador3} - Pontução do jogador 1: {jogador1} - Pontução do jogador 2: {jogador2}')

# else:
#     print(f'Pontuação do jogador 3: {jogador3} - Pontução do jogador 2: {jogador2} - Pontução do jogador 1: {jogador1}')

if jogador1 > jogador2 and jogador1 > jogador3:
    if jogador2 > jogador3:

        print(f'Pontuação do jogador 1: {jogador1} - Pontução do jogador 2: {jogador2} - Pontuação do jogador 3: {jogador3}')
    else:

        print(f'Pontuação do jogador 1: {jogador1} - Pontução do jogador 3: {jogador3} - Pontução do jogador 2: {jogador2}')

elif jogador2 > jogador1 and jogador2 > jogador3:
    if jogador1 > jogador3:

        print(f'Pontuação do jogador 2: {jogador2} - Pontução do jogador 1: {jogador1} - Pontução do jogador 3: {jogador3}')
    else:

        print(f'Pontuação do jogador 2: {jogador2} - Pontução do jogador 3: {jogador3} - Pontução do jogador 1: {jogador1}')
else:
    if jogador2 > jogador1:

        print(f'Pontuação do jogador 3: {jogador3} - Pontução do jogador 2: {jogador2} - Pontução do jogador 1: {jogador1}')
    else:

        print(f'Pontuação do jogador 3: {jogador3} - Pontução do jogador 1: {jogador1} - Pontução do jogador 2: {jogador2}')
       

if soma > 100:
    media = soma / 3
    print(f'A média de pontos da equipe foi: {media:.2f}')
else: 
    print('Equipe desclassificada')


