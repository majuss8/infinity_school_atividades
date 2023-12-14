grupo = {}

for i in range(3):
    nome = str(input("Informe o nome: "))
    telefone = int(input("Informe o telefone: "))
    idade = int(input("Informe a idade: "))

    grupo.update({nome: {"telefone": telefone, "idade": idade}})

for i in(grupo):
    print(i, " - ", grupo.get(i))

pesquisa = str(input("Informe o nome da pessoa que procura: "))
print(f'{pesquisa} - {grupo.get(pesquisa)}')


