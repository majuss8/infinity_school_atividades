import uuid
from dataclasses import dataclass

# com dataclass
@dataclass
class Aluno:
    nomeAluno: str
    cursoAluno: str
    matricula: uuid = uuid.uuid4()
    qtdFaltas: int = 0
    
    def atribuirFalta(self):
        self.qtdFaltas += 1

# sem dataclass
# class Aluno:
#     def __init__(self, nome, curso) :
#         self.nomeAluno = nome
#         self.cursoAluno = curso
#         self.matricula = uuid.uuid4()
#         self.qtdFaltas = 0
    
#     def atribuirFalta(self):
#         self.qtdFaltas += 1

aluno1 = Aluno("Jonas", "Python")
aluno2 = Aluno("Letícia", "Java")

# print(aluno1.nomeAluno, aluno1.cursoAluno)

# Alterar o valor de um atributo de um objeto
# aluno1.nomeAluno = "Jonas Lopes"
# print(aluno1.nomeAluno)

aluno1.atribuirFalta()
aluno1.atribuirFalta()
aluno2.atribuirFalta()

# print(aluno1.nomeAluno, aluno1.qtdFaltas)
# print(aluno2.nomeAluno, aluno2.qtdFaltas)

alunosMatriculados = []
alunosMatriculados.append(aluno1)
alunosMatriculados.append(aluno2)

print("--- DADOS DOS ALUNOS ---")
for aluno in alunosMatriculados:
    print(f"Matricula: {aluno.matricula}")
    print(f"Nome: {aluno.nomeAluno}")
    print(f"Curso: {aluno.cursoAluno}")
    print(f"Quantidade de faltas: {aluno.qtdFaltas}")
    print("*" * 50)