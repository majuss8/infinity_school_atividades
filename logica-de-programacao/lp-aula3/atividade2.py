nome = input('Nome: ')
senha = input('Senha: ')

while nome == senha:
    print('[ERRO] Insira os dados novamente')
    nome = input('Nome: ')
    senha = input('Senha: ')
else: 
    print('Acesso liberado')

