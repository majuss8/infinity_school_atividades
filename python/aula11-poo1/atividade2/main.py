class Pessoa():
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

    def mostrar(self):
        print(self.nome, self.idade, self.peso, self.genero)

user1 = Pessoa("Maju", 18, 65, "Feminino")

user1.mostrar()