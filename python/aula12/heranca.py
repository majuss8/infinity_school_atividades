class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        
class Professor(Funcionario):
    # matricula, nome, salario, turmas
    def __init__(self, matricula, nome, salario, turmas):
        super().__init__(matricula, nome, salario)
        self.turmas = turmas


class Coordenador(Funcionario):
    pass

class Estagiario(Funcionario):
    pass

p = Professor(1, "João", 3500, ['PYTHON', 'JAVASCRIPT'])
print(p.nome)

        
