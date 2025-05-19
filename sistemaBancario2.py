class ContaBancaria():
    def __init__(self, saldo = 0 , limite = 500, saque = 0, deposito = 0, saqueLimite = 10):
    
        self._saldo = saldo
        self._limite = limite
        self._saque = saque
        self._deposito = deposito
        self._saqueLimite = saqueLimite
        self._extrato = []

    def deposito(self):
        while True:
            deposito = float(input('Quanto deseja depositar? '))

            if deposito <= 0:
                print(f'Deposito não realizado!')

            else:
                self._saldo += deposito
                self._extrato.append(f'Deposito: +{deposito}')
                print(f'Deposito realizado com sucesso!')
                break
        
    def saque(self):
        while True:
            saque = float(input('Quanto deseja sacar? '))

            if saque <= 0:
                print(f'Saque não realizado!')

            elif saque > self._limite:
                print(f'Saque acima do limite!')
                                
            elif saque > self._saldo:
                print(f'Saldo insuficiente!')

            else:
                self._saldo -= saque
                self._extrato.append(f'Saque: -{saque}')
                print(f'Saque realizado com sucesso!')
                break

    def extrato(self):
        print('----------EXTRATO----------')
        if not self._extrato:
            print('Não foram realizadas movimentaçõess.')
        else:
            for trasacao in self._extrato:
                print(trasacao)

                     
conta = ContaBancaria()

menu = input('Digite uma opção: [d] = Deposito, [s] = Saque, [e] = Extrato, [q] = Sair: ')
while True:
    if 'd' in menu:
        conta.deposito()
        menu = input('Digite uma opção: [d] = Deposito, [s] = Saque, [e] = Extrato, [q] = Sair: ')
    elif 's' in menu:
        conta.saque()
        menu = input('Digite uma opção: [d] = Deposito, [s] = Saque, [e] = Extrato, [q] = Sair: ')
    elif 'e' in menu:
        conta.extrato()
        print(f'Saldo: {conta._saldo}')
        menu = input('Digite uma opção: [d] = Deposito, [s] = Saque, [e] = Extrato, [q] = Sair: ')
    else:
        print('Volte sempre!')
        break

