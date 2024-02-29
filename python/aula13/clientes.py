class Cliente: 
    def __init__(self, id: int, nome: str, cpf: str):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.endereco = []

    def cadastrarEndereco(self, end):
        self.endereco.append(end)

    def __repr__(self):
        return f'ID: {self.id} - Nome: {self.nome} - CPF: {self.cpf} - Endereço: {self.endereco}'
    
class Endereco:
    def __init__(self, endereco: dict):
        self.rua = endereco['rua']
        self.bairro = endereco['bairro']
        self.cep = endereco['cep']
        self.cidade = endereco['cidade']
        self.estado = endereco['estado']
        self.numero = endereco['numero']

    def __repr__(self):
        return


cliente = Cliente(1, "Jonas", "111.111.111-11")
cliente.cadastrarEndereco("Rua a", "Fortal", "CE", "1111", "Aldeota", "60000000")
