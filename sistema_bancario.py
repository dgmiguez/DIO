saldo = 0
saque = 0
saquecont = 0
saquerest = 3
print('[d] = Deposito\n[s] = saque\n[e] = extrato\n[q] = sair')
menu = input('Digite uma opção: ')
while True:
    if 'd' in menu:
        deposito = float(input('Quanto quer depositar? '))
        saldo += deposito
        print(f'Saldo: {saldo}')
        menu = input('Digite uma opção: ')
    elif 's' in menu:
        saquecont += 1
        if saquecont <= 3:
            saque = int(input('Quanto deseja sacar? '))
            if saque >= 500.01:
                print('Excede o limite de saque por transação.')
                saquecont -= 1
                menu = input('Digite uma opção: ')
            elif saque <= saldo:
                saldo -= saque
                saquerest -= 1
                print(f'Saldo: {saldo}')
                menu = input('Digite uma opção: ')
            else:
                saquecont -= 1
                print(f'Saldo insuficiente')
                menu = input('Digite uma opção: ')
        else:
            saquecont -= 1
            print('Linmite de saque atingido. Volte amanhã.')
            menu = input('Digite uma opção: ')
    elif 'e' in menu:
        print(f'Saldo: {saldo}\nSaques restantes: {saquerest}\nSaques realizados: {saquecont}')
        menu = input('Digite uma opção: ')   
    else:
        print('Volte sempre')
        break