menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar novo cliente
[l] Listar clientes
[cc] Criar nova conta
[lc] Listar contas
[q] Sair

=> """

AG = '0001'
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []
num_conta = 1


def depositar(saldo_dep, extrato_dep, /):
    while True:
        try:
            valor = float(input('Digite o valor que será depositado: '))
            if valor <= 0:
                raise Exception
            saldo_dep += valor
            extrato_dep += f'Depósito: R${valor:.2f}\n'
            print(f'Feito de R${valor:.2f}')
            return saldo_dep, extrato_dep
        except:
            print('O valor digitado é inválido. Digite somente valores numéricos maiores que 0,0\n')


def sacar(*, saldo_sac, numero_saques_sac, extrato_sac):
    if numero_saques_sac == LIMITE_SAQUES:
        print('O limite diário de saque já foi alcançado.')
        return saldo_sac, numero_saques_sac, extrato_sac
    else:
        try:
            valor_saque = float(input('Digite a quantia a ser retirada: '))

        except:
            print('O valor digitado é inválido. Retornando à tela inicial...')
            return saldo_sac, numero_saques_sac, extrato_sac

        if valor_saque > saldo_sac:
            print('Saldo insuficiente.')
            return saldo_sac, numero_saques_sac, extrato_sac
        elif valor_saque > limite:
            print('O limite de cada saque é de R$500,00.')
            return saldo_sac, numero_saques_sac, extrato_sac
        else:
            saldo_sac -= valor_saque
            numero_saques_sac += 1
            print(f'Feito saque de R${valor_saque:.2f}')
            extrato_sac += f'Saque: -R${valor_saque:.2f}\n'
            return saldo_sac, numero_saques_sac, extrato_sac


def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def listar_clientes(clientes):
    if len(clientes) <= 0:
        print('Nenhum cliente cadastrado.')
        return
    for i in clientes:
        print(f'Nome: {i[0]}\n'
              f'Data de Nascimento:{i[1]}\n'
              f'CPF: {i[2]}\n'
              f'Endereço: {i[3]}\n\n\n')


def cadastrar_cliente(clientes):
    print('Digite os dados a seguir:')
    cpf = input('CPF: ')
    for i in clientes:
        if cpf in i:
            print('\n|||||  CPF já cadastrado  |||||'
                  '\n Retornando à tela inicial. ')
            return clientes

    nome = input('Nome: ')
    dt_nasc = input('Data de nascimento: ')
    endereco = input('Endereço: ')

    clientes.append([nome, dt_nasc, cpf, endereco])
    return clientes


def criar_conta(ag, numero_conta, clientes):
    if clientes:
        cpf = input('Digite o CPF: ')
        for i in clientes:
            if cpf in i:
                print('Conta criada com sucesso!')
                return {"agencia": ag, "numero_conta": numero_conta, "cliente": i[0]}
        print('CPF não localizado!')
    else:
        print('Sem clientes cadastrados!')


def listar_contas(contas):
    if len(contas) > 0:
        for i in contas:
            print(f'Ag: {i["agencia"]}\n'
                  f'CC: {i["numero_conta"]}\n'
                  f'Titular: {i["cliente"]}\n\n')

    else:
        print('Sem nenhuma conta aberta!')


while True:
    choice = input(menu)

    match choice:
        case 'd':
            soma_saldo, txt_extrato_dep = depositar(saldo, extrato)
            saldo = soma_saldo
            extrato = txt_extrato_dep
        case 's':
            saldo_retirado, qtde_saque, txt_extrato_sac = sacar(saldo_sac=saldo, numero_saques_sac=numero_saques,
                                                                extrato_sac=extrato)
            saldo = saldo_retirado
            numero_saques = qtde_saque
            extrato = txt_extrato_sac

        case 'e':
            show_extrato(saldo, extrato=extrato)
        case 'c':
            clientes = cadastrar_cliente(clientes)
        case 'l':
            listar_clientes(clientes)
        case 'cc':
            nova_conta = criar_conta(AG, num_conta, clientes)
            if nova_conta:
                contas.append(nova_conta)
                num_conta += 1
        case 'lc':
            listar_contas(contas)
        case 'q':
            break
        case _:
            print('Opção inválida.\n')
