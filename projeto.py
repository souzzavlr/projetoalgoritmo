#lista
pacientes = []
dentistas = []
consultorios = []
consultas = []

#login admin
admins = [['ajato', '1234'], ['yohane', '4321']]


while True:
    print('========== CLINICA ODONTOLOGICA ==========')
    print('ENTRAR COMO:')
    print('1 - ADMINISTRADOR')
    print('2 - PACIENTE')
    print('0 - SAIR')
    opcao = input('Digite a opção desejada: ')
    if opcao == '0':
        break
    elif opcao == '1':
        logado = False
        while True:
            print('========== LOGIN ADMINISTRADOR ==========')
            print()
            print('Digite 0 para voltar a tela inicial.')
            print()
            login = input ('Digite o login: ')
            if login == '0':
                break
            senha = input ('Digite a senha: ')
            for a in admins:
                if login == a[0] and senha == a[1]:
                    logado = True
                    break

            if logado:
                print('Login realizado com sucesso!')
                print()
                while True:
                    print('========== MENU ADMINISTRADOR ==========')
                    print()
                    print(f'Bem-vindo(a) ao sistema, administrador(a): {login}')
                    break
            else:
                    print('Login ou senha incorretos. Tente novamente.')

                
