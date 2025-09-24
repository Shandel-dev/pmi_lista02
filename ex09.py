while True:
    expressao = input("Calculadora: ").split()
    resul = 0
    try:
        if "+" in expressao:
            numbers = expressao.split("+")
            resul = int(numbers[0]) + int(numbers[1])
        elif "-" in expressao:
            numbers = expressao.split("-")
            resul = int(numbers[0]) - int(numbers[1])
        elif "*" in expressao:
            numbers = expressao.split("*")
            resul = int(numbers[0]) * int(numbers[1])
        elif "/" in expressao:
            numbers = expressao.split("/")
            resul = int(numbers[0]) / int(numbers[1])
        else:
            print("Operador não reconhecido")
            continue
    except ValueError:
        print("Digite números válidos")
        continue
    except ZeroDivisionError:
        print("Divisão por zero não permitida")
        continue

    print("Resultado:", resul)
    break


