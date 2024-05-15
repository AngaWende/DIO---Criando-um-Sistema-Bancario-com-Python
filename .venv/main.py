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


def depositar():
    global saldo, extrato
    try:
        valor = float(input('Digite o valor que será depositado: '))
        saldo += valor
        extrato += f'Depósito: R${valor:.2f}\n'
        print(f'Feito de R${valor:.2f}')
    except:
        print('O valor digitado é inválido. Retornando à tela inicial...')


def sacar():
    global saldo, numero_saques, extrato
    if numero_saques == LIMITE_SAQUES:
        print('O limite diário de saque já foi alcançado.')
    else:
        try:
            valor_saque = float(input('Digite a quantia a ser retirada: '))

        except:
            print('O valor digitado é inválido. Retornando à tela inicial...')
            return

        if valor_saque > saldo:
            print('Saldo insuficiente.')
        elif valor_saque > limite:
            print('O limite de cada saque é de R$500,00.')
        else:
            saldo -= valor_saque
            numero_saques += 1
            print(f'Feito saque de R${valor_saque:.2f}')
            extrato += f'Saque: -R${valor_saque:.2f}\n'


def show_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:
    choice = input(menu)

    match choice:
        case 'd':
            depositar()
        case 's':
            sacar()
        case 'e':
            show_extrato()
        case 'q':
            break
        case _:
            print('Opção inválida.\n')
