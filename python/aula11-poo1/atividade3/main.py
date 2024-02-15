class Empresa():
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.lista = []
    
    def adicionar(self, funcionario):
        self.lista.append(funcionario)

    def mostrar(self):
        for i in self.lista:
            print(i.nome)

    def remover(self, funcionario):
        self.lista.remove(funcionario)

class Funcionario():
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
opcao = 1
e = Empresa("000000000000")
while opcao != 0:
    opcao = int(input("Informe uma opção: \n 1 - Adicionar; \n 2 - Remover; \n 3 - Mostrar"))
    if opcao == 1:
        nome = input("Informe o nome: ")
        cargo = input("Informe o cargo: ")
        salario = float(input("Informe o salario: "))
        f1 = Funcionario(nome, cargo, salario)
        e.adicionar(f1)

    elif opcao == 2:
        nome = input("Informe o nome do(a) funcionario(a) a ser removido(a): ")
        for funcionario in e.lista:
            if funcionario.nome == nome:
                e.remover(funcionario)
                print(f'Funcionario(a) {nome} removido(a) com sucesso!')
                break
            else:
                print(f'Funcionário(a) não encontrado(a)')
    elif opcao == 3:
        print("Funcionarios: ")
