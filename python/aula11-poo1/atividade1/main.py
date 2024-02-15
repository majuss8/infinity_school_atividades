class Cachorro():
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def latir(self):
        return f'{self.nome}: Au Au!'
    
    def sentar(self):
        return f'{self.nome} está sentado'
    
    def rolar(self):
        return f'{self.nome} rolou'
    
    def darPata(self):
        return f'{self.nome} deu a pata'
    
    def comer(self):
        return f'{self.nome} está comendo'
    
    def correr(self):
        return f'{self.nome} está correndo'
    
    def mostrar(self):
        print(self.nome, self.raca, self.idade)
    
dog1 = Cachorro("Cacau", "Pitbull", 8)
dog2 = Cachorro("Cupcake", "Rottweiler", 5)

dog2.mostrar()
