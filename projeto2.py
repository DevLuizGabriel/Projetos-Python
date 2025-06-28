import time 

from datetime import datetime

eventos = []

def cadastrar_evento():
    nome = input("Digite o nome do evento:")
    
    data_str = input("Digite a data do evento (dd/mm/aaaa): ")
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
    except ValueError:
        print("Data inválida! Use o formato dd/mm/aaaa.")
        return  # Sai da função se a data for inválida

    descricao = input("Digite a descrição do evento:")
    
    try:
        participante = int(input("Digite o número máximo de participantes"))
    except ValueError:
        print("Valor inválido! Digite um número inteiro.")
        return  

    evento = {
    "nome": nome,
    "data": data,
    "descricao": descricao,
    "max_participantes": participante,
    "inscritos": []  }

    eventos.append(evento)

    print("\nEvento cadastrado com sucesso!\n")
    print(f"Nome: {evento['nome']}")
    print(f"Data: {evento['data'].strftime('%d/%m/%Y')}")
    print(f"Descrição: {evento['descricao']}")
    print(f"Nº máximo de participantes: {evento['max_participantes']}")

def atualizar_evento():
    if not eventos:
        print("Não há eventos cadastrados para atualizar.")
        return

    print("Eventos cadastrados:")
    for i, evento in enumerate(eventos):
        print(f"{i+1} - {evento['nome']} (Data: {evento['data'].strftime('%d/%m/%Y')}, Vagas: {evento['max_participantes']})")

    try:
        escolha = int(input("Digite o número do evento que deseja atualizar: "))
        if escolha < 1 or escolha > len(eventos):
            print("Número inválido!")
            return
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return

    evento = eventos[escolha - 1]

    print(f"Você escolheu atualizar o evento: {evento['nome']}")

    print("O que deseja atualizar?")
    print("1 - Data")
    print("2 - Número máximo de participantes")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nova_data_str = input("Digite a nova data do evento (dd/mm/aaaa): ")
        try:
            nova_data = datetime.strptime(nova_data_str, "%d/%m/%Y")
            evento['data'] = nova_data
            print("Data atualizada com sucesso!")
        except ValueError:
            print("Data inválida! Operação cancelada.")
    elif opcao == "2":
        try:
            novo_max = int(input("Digite o novo número máximo de participantes: "))
            evento['max_participantes'] = novo_max
            print("Número máximo de participantes atualizado com sucesso!")
        except ValueError:
            print("Número inválido! Operação cancelada.")
    else:
        print("Opção inválida!")

def visualizar_eventos():
    if not eventos:
        print("Não há eventos disponíveis no momento.")
        return
    print("Eventos Disponíveis:")
    for i, evento in enumerate(eventos):
        vagas_restantes = evento['max_participantes'] - len(evento['inscritos'])
        print(f"Evento {i+1}:")
        print(f"Nome: {evento['nome']}")
        print(f"Data: {evento['data'].strftime('%d/%m/%Y')}")
        print(f"Descrição: {evento['descricao']}")
        print(f"Vagas restantes: {vagas_restantes}")
        print("-" * 40)

def inscrever_em_evento():
    if not eventos:
        print("Não há eventos disponíveis para inscrição.")
        return

    print("Eventos disponíveis para inscrição:")
    for i, evento in enumerate(eventos):
        vagas_restantes = evento['max_participantes'] - len(evento['inscritos'])
        print(f"{i+1} - {evento['nome']} | Data: {evento['data'].strftime('%d/%m/%Y')} | Vagas restantes: {vagas_restantes}")

    try:
        escolha = int(input("Digite o número do evento que deseja se inscrever: "))
        if escolha < 1 or escolha > len(eventos):
            print("Número inválido!")
            return
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return

    evento = eventos[escolha - 1]
    vagas_restantes = evento['max_participantes'] - len(evento['inscritos'])

    if vagas_restantes <= 0:
        print("Não há mais vagas disponíveis para este evento.")
        return

    nome_participante = input("Digite seu nome para a inscrição: ")
    
    if nome_participante in evento['inscritos']:
        print("Você já está inscrito nesse evento.")
    else:
        evento['inscritos'].append(nome_participante)
        print(f"{nome_participante}, sua inscrição foi realizada com sucesso!")

def visualizar_inscritos():
    if not eventos:
        print("\nNão há eventos cadastrados.\n")
        return

    print("\nLista de inscrições por evento:\n")
    for i, evento in enumerate(eventos, start=1):
        print(f"Evento {i}: {evento['nome']}")
        if evento['inscritos']:
            for j, nome in enumerate(evento['inscritos'], start=1):
                print(f"  {j}. {nome}")
        else:
            print("  (Nenhum inscrito)")
        print("-" * 40)

def excluir_evento():
    if not eventos:
        print("\nNão há eventos cadastrados para excluir.\n")
        return

    print("\nEventos cadastrados:")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i} - {evento['nome']} (Data: {evento['data'].strftime('%d/%m/%Y')})")

    try:
        escolha = int(input("\nDigite o número do evento que deseja excluir: "))
        if escolha < 1 or escolha > len(eventos):
            print("Número inválido! Operação cancelada.")
            return
    except ValueError:
        print("Entrada inválida! Digite um número.")
        return

    evento = eventos.pop(escolha - 1)
    print(f"O evento '{evento['nome']}' foi excluído com sucesso!")

while True:
    print ("Bem vindo ao sistema de gerenciamento!")

    print("1 - Cadastro de eventos")
    print("2 - Atualização de Eventos")
    print("3 - Visualização de Eventos Disponíveis")
    print("4 - Inscrição em Eventos")
    print("5 - Visualizar Inscrições")
    print("6 - Exclusão de Eventos")
    print("0 - Sair")

    opcao = input("Digite o número da opção desejada")
    print(f"Você escolheu a opção {opcao}")

    if opcao =="1": 
        cadastrar_evento()
    elif opcao =="2":
        atualizar_evento()
    elif opcao == "3":
        visualizar_eventos()
    elif opcao == "4":
        inscrever_em_evento()
    elif opcao == "5":
        visualizar_inscritos()
    elif opcao == "6":
        excluir_evento()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção não implementada ainda.")
   
    time.sleep(2)

    
