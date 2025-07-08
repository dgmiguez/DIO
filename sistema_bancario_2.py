def menu():
    print('''Menu:
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [0] Sair''')
    return input('Digite uma opção: ')

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Valor de depósito inválido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print('Saldo insuficiente.')
    elif excedeu_limite:
        print('Excedeu o limite de saque.')
    elif excedeu_saques:
        print('Número de saques atingidos.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}'
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Valor informado é inválido.')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: {saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe um usuário com esse CPF.')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ')
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print('Usuário criado com sucesso!')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF  do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print(f'Conta criada com sucesso para {usuario["nome"]}')
        return {'agencia': agencia,
                'número conta': numero_conta,
                'usuario': usuario}
        
    if not usuario:
        print('Usuário não encontrado. Crie um usuário antes de criar uma conta.')
        
def main():
    AGENCIA = '0001'
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()
        
        if opcao == '1':
            valor = float(input('Quanto quer depositar? '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Quanto deseja sacar? '))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,)

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == '0':
            print('Volte sempre!')
            break

        else:
            print('Opção inválida. Tente novamente.')

main()