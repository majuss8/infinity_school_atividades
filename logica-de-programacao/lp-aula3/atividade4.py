# numAlunos = int(input('Quantidade de alunos na turma: '))

# i = 1
# somaDasNotas = 0
# alunosAprovados = 0
# while i <= numAlunos:
#     notaAluno = float(input(f'Nota do aluno {i}: '))
#     somaDasNotas += notaAluno
#     if notaAluno >= 7:
#         alunosAprovados += 1
#     i += 1

# media = somaDasNotas / numAlunos
# percentual = (100 * alunosAprovados) / numAlunos

# print(f'Média da turma: {media}')
# print(f'Percentual de aprovados: {percentual}')

numDeTurmas = int(input('Quantidade de turmas: '))
numeroTurma = 0
while numDeTurmas != 0 and numeroTurma < numDeTurmas:
    numeroTurma += 1
    numAlunos = int(input(f'Quantidade de alunos na turma {numeroTurma}: '))
    i = 1
    somaDasNotas = 0
    alunosAprovados = 0
    while i <= numAlunos:
        notaAluno = float(input(f'Nota do aluno {i}: '))
        somaDasNotas += notaAluno
        if notaAluno >= 7:
            alunosAprovados += 1
        i += 1

    media = somaDasNotas / numAlunos
    percentual = (100 * alunosAprovados) / numAlunos

    print(f'Turma {numeroTurma}:')
    print(f'Total de alunos: {numAlunos}')
    print(f'Média da turma {numeroTurma}: {media}')
    print(f'Percentual de aprovados: {percentual}%')
else:
    print('fim do programa, reinicie')


