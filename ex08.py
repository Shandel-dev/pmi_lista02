pessoas = []

while True:
    print("\n1 - Cadastrar pessoa")
    print("2 - Listar todas")
    print("3 - Buscar por nome")
    print("4 - Sair")

    opcao = input("Escolha: ")

    #CADASTRAR PESSOA
    if opcao == "1":
        nome = input("Nome: ").strip()
        if nome == "":
            print("Nome inválido.")
            continue

        try:
            idade = int(input("Idade: "))
            if idade < 0:
                print("Idade inválida.")
                continue
        except ValueError:
            print("Idade deve ser número.")
            continue
        pessoas.append((nome, idade))
        print("Pessoa cadastrada.")

    #LISTAR TODAS
    elif opcao == "2":
        i = 0
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        while i < len(pessoas):
            print(f"{i+1}. Nome: {pessoas[i][0]} | Idade: {pessoas[i][1]}")
            i += 1

    #BUSCAR POR NOME
    elif opcao == "3":
        busca = input("Nome a buscar: ").strip().lower()
        i = 0
        achou = False
        while i < len(pessoas):
            if pessoas[i][0].lower() == busca:
                print(f"Encontrado: Nome: {pessoas[i][0]} | Idade: {pessoas[i][1]}")
                achou = True
            i += 1
        if not achou:
            print("Nenhum registro encontrado.")

    #SAIR
    elif opcao == "4":
        print("Encerrando.")
        break

    else:
        print("Opção inválida.")
