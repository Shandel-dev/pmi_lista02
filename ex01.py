while True:
    try:
        tel = int(input("Insira seu telefone\n(Sem espaços ou caracteres especiais): "))
        tel = str(tel)
        tel = tel.strip().replace(" ", "")

        if len(tel) == 11:
            print("({}){}-{}".format(tel[:2], tel[2:7], tel[7:]))
            break
        else:
            print("O telefone deve ter DDD e outros 9 digitos")
    except ValueError:
        print("Entrada inválida!")
