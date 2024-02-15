class Carro():
    # atributos / caracteristicas
    # cor, modelo, ano, marca
    def __init__(self, cor, modelo, ano, marca): # construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    # metodos
    def ligar(self):
        return f'O {self.modelo} está ligado!'
        
############ FORA DA CLASSE ############

carro1 = Carro("azul", "Sandero", 2021, "Renault")
carro2 = Carro("prata", "Argo", 2020, "Fiat")
print(carro1.marca)
print(carro2.ligar())

lista = {
    "carros": [
        carro1, 
        carro2
    ]
}
print(lista["carros"][1].ano)


