menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Valor de deposito: '))
        if 0 <= deposito:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
        else:
            print('Valor inesperado')

    elif opcao == 's':
        valorASacar = float(input('Valor a sacar R$ '))
        if saldo > valorASacar and numero_saques < LIMITE_SAQUES and valorASacar < 500:
            numero_saques += 1
            saldo -= valorASacar
            extrato += f"Saque: R$ {valorASacar:.2f}\n"
        else:
            print('Erro no saque! Tente novamente.')

    elif opcao == 'e':
        print('============== Extrato ==============')
        print(extrato if not extrato else extrato)
        print('\nR$ {:.2f}'.format(saldo))
        print('=====================================')

    elif opcao == 'q':
        break
    else:
        print('Opção invalida')
