nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
telefone = int(input("Informe seu telefone: "))
endereco = str(input("Informe seu endereco: "))

usuario = {
    "nome": nome,
    "idade": idade,
    "telefone": telefone,
    "endereco": endereco
}

print(usuario)
print(usuario.items())
