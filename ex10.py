while True:
    try:
        cpf = input("CPF (somente números): ").strip()
        if len(cpf) != 11 or not cpf.isdigit():
            print("CPF deve ter 11 números")
            continue

        verificadores = [0, 0]

        # primeiro dígito
        soma = 0
        multi = 10
        i = 0
        while i < 9:
            soma += multi * int(cpf[i])
            multi -= 1
            i += 1

        if soma % 11 < 2:
            verificadores[0] = 0
        else:
            verificadores[0] = 11 - (soma % 11)

        # segundo dígito
        soma = 0
        multi = 11
        i = 0
        while i < 10:
            soma += multi * int(cpf[i])
            multi -= 1
            i += 1

        if soma % 11 < 2:
            verificadores[1] = 0
        else:
            verificadores[1] = 11 - (soma % 11)

        # verificar dígitos
        if verificadores[0] == int(cpf[9]) and verificadores[1] == int(cpf[10]):
            print(f"CPF válido: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
        else:
            print("CPF inválido!")
        break
    except ValueError:
        print("Entrada inválida!")
