from dataclasses import dataclass

@dataclass
class Veiculo:
    marcaVeiculo = str
    modeloVeiculo = str
    corVeiculo = str
    veiculoLigado = bool = False
    
    def ligar(self):
        self.veiculoLigado = True

    def desligar(self):
        self.veiculoLigado = False

class Moto(Veiculo):
    def __init__(self):
        cilindradas = cilindradas

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, numeroDePortas):
        super().__init__(marca, modelo, cor)
        self.numeroDePortas = numeroDePortas

pcx = Moto("Honda", "Scooter", "Azul", 160)
hb20 = Carro("Hyundai", "Sense", "Branco", 4)

pcx.ligar()

veiculosCadastrados = []
veiculosCadastrados.append(pcx)
veiculosCadastrados.append(hb20)

print("--- DADOS DOS VEÍCULOS ---")
for veiculo in veiculosCadastrados:
    print(f"Marca: {veiculo.marcaVeiculo}")
    print(f"Modelo: {veiculo.modeloVeiculo}")
    print(f"Cor: {veiculo.corVeiculo}")
    print(f"Veículo ligado: {veiculo.veiculoLigado}")

    if (hasattr(veiculo, 'cilindradas')) :
        print(f"Cilindradas: {veiculo.cilindradas}")
    
    if (hasattr(veiculo, 'numeroDePortas')):
        print(f"Número de portas: {veiculo.numeroDePortas}")

    print("*" * 50)

    