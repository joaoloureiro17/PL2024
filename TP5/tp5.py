import re


def carregar_produtos(nome_arquivo):
    produtos = {}
    with open(nome_arquivo, 'r') as file:
        for line in file:
            match = re.match(r'(\d+)\.\s*(.*?)\s*(\d+)c', line)
            if match:
                id_produto, nome, preco = match.groups()
                produtos[int(id_produto)] = (nome.strip(), int(preco))
    return produtos


def imprimir_menu(produtos):
    print("Produtos disponíveis:")
    for id_produto, (nome, preco) in produtos.items():
        print(f"{id_produto}. {nome} - {preco}c")


def listar_produtos(produtos):
    print("Produtos disponíveis:")
    for id_produto, (nome, preco) in produtos.items():
        print(f"{id_produto}. {nome} - {preco}c")


def selecionar_produto(id_produto, saldo, produtos):
    if id_produto not in produtos:
        print("Produto inválido.")
        return saldo
    nome, preco = produtos[id_produto]
    if saldo < preco:
        print("Saldo insuficiente.")
    else:
        saldo -= preco
        print(f"Produto '{nome}' selecionado. Saldo restante: {saldo}c")
    return saldo


def verificar_moeda(moeda):
    return re.match(r'^[125]|10|20|50+[cC]$', moeda) or re.match(r'^[12]+[eE]$', moeda)


def vending_machine(nome_arquivo):
    produtos = carregar_produtos(nome_arquivo)
    saldo = 0

    while True:
        comando = input(">> ").upper()
        
        if comando.startswith("MOEDA"):
            moedas = re.findall(r'\b\d+[eEcC]?\b', comando)
            for moeda in moedas:
                if verificar_moeda(moeda):
                    if moeda.endswith('E'):
                        saldo += int(moeda.strip('E')) * 100
                    elif moeda.endswith('C'):
                        saldo += int(moeda.strip('C'))
                else:
                    print("Moeda inválida.")
            print(f"< SALDO = {saldo}c")
        elif comando.startswith("SELECIONAR"):
            id_produto = int(comando.split()[1])
            saldo = selecionar_produto(id_produto, saldo, produtos)
        elif comando == "LISTAR":
            listar_produtos(produtos)
        elif comando == "SAIR":
            print(f"< Troco: {saldo}c")
            break
        else:
            print("Comando inválido.")


if __name__ == "__main__":
    arquivo_produtos = "produtos.txt"  
    vending_machine(arquivo_produtos)
