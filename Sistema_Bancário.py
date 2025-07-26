import textwrap
import json
import time 



def barra_carregamento(texto="Carregando", tempo_total=1.5):
    """Exibe uma barra de carregamento animada."""
    simbolo = '█'
    total_blocos = 30
    print(f"\n{texto} ", end="")
    for i in range(total_blocos):
        print(simbolo, end='', flush=True)
        time.sleep(tempo_total / total_blocos)
    print(" Concluído!")
    time.sleep(0.5) # Uma pequena pausa após a conclusão

def carregar_dados(nome_arquivo):
    """Carrega dados de um arquivo JSON."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(nome_arquivo, dados):
    """Salva os dados em um arquivo JSON."""
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)




def menu():
    menu_texto = """\n
    ======================= MENU =======================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))

def criar_usuario(usuarios, nome_arquivo):
    cpf = input("Informe o CPF do usuário (apenas números): ")
    usuario_existente = filtrar_usuario(cpf, usuarios)
    
    if usuario_existente:
        print("\n@@@ Usuário já cadastrado com esse CPF. @@@")
        return
    
    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe o endereço (Rua, Número - Bairro - Cidade/Sigla Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    salvar_dados(nome_arquivo, usuarios)
    
    print(f"\n=== Usuário {nome} cadastrado com sucesso! ===")



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print(f"\n=== Depósito de R$ {valor:.2f} realizado com sucesso! ===")
    else:
        print("\n@@@ Erro: Valor de depósito deve ser positivo. @@@")
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Erro: Saldo insuficiente para saque. @@@")
    elif excedeu_limite:
        print("\n@@@ Erro: Valor de saque excede o limite por operação. @@@")
    elif excedeu_saques:
        print("\n@@@ Erro: Limite de saques diários atingido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n=== Saque de R$ {valor:.2f} realizado com sucesso! ===")
    else:
        print("\n@@@ Operação inválida. O valor do saque deve ser positivo. @@@")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n====================== EXTRATO ======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual:\tR$ {saldo:.2f}")
    print("======================================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print(f"\n=== Conta criada com sucesso para {usuario['nome']}! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado. Conta não criada. @@@")
    return None

def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta cadastrada.")
        return
        
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    ARQUIVO_USUARIOS = "usuarios.json"
    
    # Exibindo a barra de carregamento na inicialização
    barra_carregamento("Iniciando sistema...")
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    
    usuarios = carregar_dados(ARQUIVO_USUARIOS)

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios, ARQUIVO_USUARIOS)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            # Exibindo a barra de carregamento ao sair
            barra_carregamento("Encerrando sessão...")
            print("\nObrigado por usar nosso banco!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")



main()