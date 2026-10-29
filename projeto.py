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
            else:
                print('Login ou senha incorretos. Tente novamente.')
                break
            while True:
                    print('========== MENU ADMINISTRADOR ==========')
                    print()
                    print(f'Bem-vindo(a) ao sistema, administrador(a): {login}')
                    print('Escolha uma opção:')
                    print()
                    print('1 - Ver cadastros de pacientes')
                    print('2 - Administrar dentistas')
                    print('0 - Sair')
                    print()
                    opcao_admin = input('Digite a opção desejada: ')
                    if opcao_admin == '0':
                        print('Saindo do Menu Administrador...')
                        break
                    elif opcao_admin == '1':
                        print('PACIENTES CADASTRADOS:')
                        print (pacientes)

                    #DENTISTAS
                    elif opcao_admin == '2':
                        print('GESTÃO DE DENTISTAS')
                        print('1 - Cadastrar dentista')
                        print('2 - Listar dentistas')
                        print('3 - Buscar dentista()')
                        print('4 - Atualizar dentista()')
                        print('5 - Excluir dentista()')
                        print('0 - Voltar ao menu anterior')
                        print()
                        opcao3 = input('Escolha uma opção: ')
                        if opcao3 == '0':
                            print('Voltando ao menu anterior...')
                            break
                        elif opcao3 == '1':
                            while True:
                                dent_id = input('Digite o ID do dentista: ').strip()
                                if dent_id .isdigit() == False:
                                    print('Digite um ID válido (apenas números).')
                                    continue
                                dent_nome = input('Digite o nome do dentista: ').lower().strip()
                                dent_cro = input('Digite o CRO do dentista: ').lower().strip()
                                dent_especialidade = input('Digite a especialidade do dentista: ').lower().strip()
                                dentistas.append(dent_id)
                                print(f'Dentista {dent_nome} cadastrado com sucesso!')
                                break
                        elif opcao3 == '2':
                            for dentista in dentistas:
                                print('INFORMAÇÕES DO DENTISTA: ')
                                print()
                                print('ID Dentista:', dentista[0])
                                print('Nome do dentista:', dentista[1])
                                print('CRO do dentista:', dentista[2])
                                print('Especialidade do dentista:', dentista[3])

                        elif opcao3 == '3':
                            dent_id = input('Digite o ID do dentista que deseja buscar: ')
                            



                



                        

                    
            

                
