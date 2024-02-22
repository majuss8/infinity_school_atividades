class Veiculo:
    def __init__(self, marca, modelo, cor):
        self.marcaVeiculo = marca
        self.modeloVeiculo = modelo
        self.corVeiculo = cor
        self.veiculoLigado = False
        self.velocidadeAtual = 0
    
    def ligar(self):
        self.veiculoLigado = True

    def desligar(self):
        self.veiculoLigado = False

class Moto(Veiculo):
    def __init__(self, marca, modelo, cor, cilindradas):
        super().__init__(marca, modelo, cor)
        self.cilindradas = cilindradas

    def acelerar(self):
        if self.veiculoLigado == True:
            self.velocidadeAtual += 30
        ...

    def __repr__(self):
        mensagem = ''
        if self.velocidadeAtual == 0:
            mensagem = 'O veículo está desligado'
        else:
            mensagem = f'Acelerando... {self.velocidadeAtual}'

        return f"Marca: {self.marcaVeiculo}, \nModelo: {self.modeloVeiculo}, \nCor: {self.corVeiculo}, \nVeículo Ligado: {self.veiculoLigado}, \nCilindradas: {self.cilindradas}, \nVelocidade Atual: {mensagem}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, numeroDePortas):
        super().__init__(marca, modelo, cor)
        self.numeroDePortas = numeroDePortas
    
    def acelerar(self):
        if self.veiculoLigado == True:
            self.velocidadeAtual += 20
        pass
            

    # Essa função muda o comportamento do objeto quando printado
    def __repr__(self):
        mensagem = ''
        if self.velocidadeAtual == 0:
            mensagem = 'O veículo está desligado'
        else:
            mensagem = f'Acelerando... {self.velocidadeAtual}'

        return f"Marca: {self.marcaVeiculo}, \nModelo: {self.modeloVeiculo}, \nCor: {self.corVeiculo}, \nVeículo Ligado: {self.veiculoLigado}, \nNúmero de portas: {self.numeroDePortas}, \nVelocidade Atual: {mensagem}"

pcx = Moto("Honda", "Scooter", "Azul", 160)
hb20 = Carro("Hyundai", "Sense", "Branco", 4)

pcx.ligar()
pcx.acelerar()
pcx.acelerar()

hb20.acelerar()

veiculosCadastrados = []
veiculosCadastrados.append(pcx)
veiculosCadastrados.append(hb20)

# print("--- DADOS DOS VEÍCULOS ---")
# for veiculo in veiculosCadastrados:
#     print(f"Marca: {veiculo.marcaVeiculo}")
#     print(f"Modelo: {veiculo.modeloVeiculo}")
#     print(f"Cor: {veiculo.corVeiculo}")
#     print(f"Veículo ligado: {veiculo.veiculoLigado}")

#     if (hasattr(veiculo, 'cilindradas')) :
#         print(f"Cilindradas: {veiculo.cilindradas}")
    
#     if (hasattr(veiculo, 'numeroDePortas')):
#         print(f"Número de portas: {veiculo.numeroDePortas}")

#     print("*" * 50)

print("--- DADOS DOS VEÍCULOS ---")
for veiculo in veiculosCadastrados:
    print(veiculo)
    print("*" * 50)