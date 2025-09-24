estoque = []
while True:
    try:
        print("=" * 10, "Menu", "=" * 10)
        print("1 - Criar\n2 - Ler\n3 - Atualizar\n4 - Apagar\n5 - Listar")
        print("=" * 26)
        option = int(input(""))

        if option == 1:     #CRIAR
            while True:
                try:
                    print("CADASTRO DE PRODUTO")
                    nome = input("Nome: ")
                    qtd = int(input("Quantidade: "))
                    preco = float(input("Preço: R$"))
                    estoque.append((nome, qtd, preco))
                    break
                except ValueError:
                    print("Entrada inválida! Preencha corretamente os dados do produto!")
        elif option == 2:   #LER
            while True:
                try:
                    print("LER PRODUTOS CADASTRADOS")
                    print("! - Busca de produtos baseados no índice da lista")

                    id = int(input("ID do produto que deseja visualizar: "))
                    produto = estoque[id]
                    print(f"ID: {id}")
                    print(f"Nome:{produto[0]}")
                    print(f"Quantidade:{produto[1]}")
                    print(f"Preço: R${produto[2]}")
                    break
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                except IndexError:
                    print("Produto não encontrado!")
                    break
        elif option == 3:   #ATUALIZAR
            while True:
                try:
                    print("ATUALIZAR PRODUTOS EXISTENTES")
                    print("! - Busca de produtos baseados no índice da lista")
                    id = int(input("ID do produto que deseja Atualizar: "))
                    nome = input("Nome: ")
                    qtd = int(input("Quantidade: "))
                    preco = float(input("Preço: R$"))
                    estoque[id] = (nome, qtd, preco)
                    break;
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                except IndexError:
                    print("Produto não encontrado!")
                    break
        elif option == 4:   #APAGAR
            while True:
                try:
                    print("APAGAR UM PRODUTO")
                    print("! - Busca de produtos baseados no índice da lista")

                    id = int(input("ID do produto que deseja Apagar: "))
                    estoque.pop(id)
                    break
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                except IndexError:
                    print("Produto não encontrado")
                    break
        elif option == 5:   #LISTAR para ver
            print("Listando estoque")
            print(estoque)
        else:
            print("Opção inválida!")
    except ValueError:
        print("Entrada inválida!")

