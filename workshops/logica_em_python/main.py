users = [] # lista vazia

def addUser(user, password): # função para adicionar um novo usuário
    usuario = { # dicionário / é tipo um objeto
        'usuario': user, 
        'senha': password
    }

    if len(user) > 0: # verificação do usuário (tamanho)
        print('Usuário cadastrado com sucesso!')
        users.append(usuario) # adicionar usuario na lista users
        return True
    else:
        print('[ERRO] Digite um usuário correto')
    
def login(user, password): # função para logar um usuário ja existente
    for usuario in users: # for que corre pela lista users
        if usuario['usuario'] == user and usuario['senha'] == password: # verificar se os dados (usuario e senha) equivalem a algum usuario ja presente na lista users
            print('Usuário logado com sucesso!')
        else:
            print('[ERRO] Usuário não encontrado')

while True: # enquanto verdadeiro
    op = input("""[1] - Cadastrar\n[2] - Entrar\n[3] - Sair\nDigite o valor da ação deseja fazer: """) # opções

    if op == '1':    
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        addUser(usuario, senha) # chamada da função
    elif op == '2':
        usuario = input('Usuário: ')
        senha = input('Senha: ')       
        login(usuario, senha)
    elif op == '3':
        print('Fim do programa')
        break
    else:
        print('[ERRO] opção inválida')
