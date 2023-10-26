nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print(f'Média: {media:.1f}\nAprovado')
elif media < 5 and media < 7:
    print(f'Média: {media:.1f}\nRecuperação')
else:
    print(f'Média: {media:.1f}\nReprovado')
