P1 = ()
P2 = ()

qtd = int(input('Quantos alunos tem na turma? '))

P1 = list(P1)
P2 = list(P2)

for i in range(qtd):
    nota1 = float(input('Informe as notas da turma na prova 1: '))
    P1.append(nota1)
    nota2 = float(input('Informe as notas da turma na prova 2: '))
    P2.append(nota2)

mediaP1 = sum(P1) / len(P1)
mediaP2 = sum(P2) / len(P2)

P1 = tuple(P1)
P2 = tuple(P2)

print(f'A média da turma na prova 1 foi: {mediaP1}\nA média da turma na prova 2 foi: {mediaP2}')

if mediaP1 > mediaP2:
    print(f'A melhor média foi na prova 1')
elif mediaP2 > mediaP1:
    print(f'A melhor média foi na prova 2')
else:
    print(f'As médias provas foram iguais')

