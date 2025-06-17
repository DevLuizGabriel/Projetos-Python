import time

estoque = {}

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto:"))
    quantidade = int(input("Digite a quantidade em estoque: "))

    estoque[nome] = {
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_produto():
    nome = input("Digite o nome do produto que deseja atualizar:")
    
    if nome in estoque:
        try:
            preco = float(input("Digite o novo preço do produto:"))
            quantidade = int(input("Digite a nova quantidade em estoque:"))

            estoque[nome]['preco'] = preco
            estoque[nome]['quantidade'] = quantidade

            print(f"Produto '{nome}' atualizado com sucesso!")
        except ValueError:
            print("Erro; preço ou quantidade inválidos. Tente novamente.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def excluir_produto():
    nome = input("Digite o nome do produto que deseja excluir: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' excluído com sucesso!")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def visualizar_estoque():
    if len(estoque) == 0:
        print("O estoque está vazio.")
    else:
        print("Estoque atual:")
        for nome, info in estoque.items():
            print(f"- {nome}: Preço R$ {info['preco']:.2f}, Quantidade {info['quantidade']}")



while True: 
    print("Bem-vindo ao controle de estoque!")

    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("6 - Sair")

    opcao = input("escolha uma opção:")

    print ("Você escolheu a opção", opcao)

    if opcao == "1":
        adicionar_produto()
        time.sleep(2)
    elif opcao == "2":
        atualizar_produto()
        time.sleep(2)
    elif opcao == "3":
        excluir_produto() 
        time.sleep(2)
    elif opcao == "4":
        visualizar_estoque()
        time.sleep(2)
    elif opcao == "6":
        print("Você escolheu: Sair do sistema")
        time.sleep(2)
        break
    else:
        print("Opção inválida")
        time.sleep(2)