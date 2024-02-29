class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

class Livro:
    def __init__(self, titulo, autor, biblioteca):
        self.titulo = titulo
        self.autor = autor
        self.biblioteca = biblioteca
    
    def __repr__(self):
        return f'Título: {self.titulo} - Autor: {self.autor}'

biblioteca = Biblioteca('Biblio Infinity')
livro1 = Livro('Harry Potter', 'JK Rolling', biblioteca)
livro2 = Livro('Código Limpo', 'James', biblioteca)
biblioteca.livros.append(livro1)
biblioteca.livros.append(livro2)

# print(biblioteca.livros)

class Conta:
    def __init__(self, numero, cliente, saldo):
        self.__numero = numero
        self.__cliente = cliente
        self.__saldo = saldo

    @property
    def getNumero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        self.__numero = valor
    
    @property
    def getCliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def setSaldo(self, valor):
        self.__saldo = valor

    def saque(self, valor):
        if self.__saldo <= valor:
            self.__saldo = self.__saldo - valor
            print('saldo realizado')
        else:
            print('saldo insuficiente')

    def deposito(self, valor):
        self.__saldo += valor
        print('depósito realizdo')

    def __repr__(self):
        return f'N. Conta: {self.numero} - Nome: {self.cliente} - Saldo: {self.saldo}'
    
# cc = Conta('111', 'Jonas', 1000)
# cc.nome = 1111
# cc.saldo = 10000000
# print(cc.getSaldo())

class Produto:
    def __init__(self, codigo, nome, preco, categoria, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.estoque = estoque

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, value):
        self.codigo = value

    def get_nome(self):
        return self.nome

    def set_nome(self, value):
        self.nome = value

    def get_preco(self):
        return self.preco

    def set_preco(self, value):
        self.preco = value

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, value):
        self.categoria = value

    def get_estoque(self):
        return self.estoque

    def set_estoque(self, value):
        self.estoque = value

