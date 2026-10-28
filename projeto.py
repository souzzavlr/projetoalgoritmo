nomes_pacientes = []
cpf_pacientes = []
telefones_pacientes = []

while opcao != 0
print('/n--- CLÍNICA ODONTOLÓGICA ---')
print('1 - Cadastrar Paciente')
print('2 - Listar Paciente')
print('0 - Sair')

opcao = input('escolha uma opção:')

if opcao == '1':
    nome = input('Digite o nome do paciente: ')
    cpf = input('Digite o CPF:')
    telefone = input('Digite o telefone:')

    if cpf in cpf_pacientes:
        print('Este CPF já está cadastrado.')

    else:
        