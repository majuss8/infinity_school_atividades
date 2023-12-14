qtdContatos = int(input("Informe a quantidade de contatos de sua lista: "))

listaDeContatos = {}

for contato in range(qtdContatos):
    nome = str(input("Informe o nome do contato: "))
    telefone = int(input("Informe o telefone do contato: "))

    if nome in listaDeContatos:
        print('Já existe um contato com esse nome!')
    else:
        listaDeContatos[nome] = telefone


for i in(listaDeContatos):
    print(i, " - ", listaDeContatos.get(i))

pesquisa = str(input("Informe o nome do contato que procura: "))
if pesquisa in listaDeContatos:
    print(f'{pesquisa} - {listaDeContatos.get(pesquisa)}')
else: 
    print('Contato não encontrado.')
