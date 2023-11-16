import random
cadastros = [] # lista vazia

while True: 
    cliente = {    
        'nome' : input("Qual o nome do cliente?\n"),
        'telefone' : input("Qual seu telefone?\n"),
        'endereco' : input("Qual seu endereço?\n")
    }
    cadastros.append(cliente)

    if cliente['nome'] == 'fim' and cliente['telefone'] == '' and cliente['endereco'] == '':
        cadastros.pop()
        sorteio = random.choice(cadastros)
        print(f'Sorteado do dia: {sorteio}')
        print('Fim do programa')
        break  