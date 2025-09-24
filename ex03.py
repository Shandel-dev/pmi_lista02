
print("Programa conversor de bases numéricas")
while True:
    try:
        entrada = int(input("Digite um número: "))

        print("Binário:", bin(entrada))
        print("Octal:", oct(entrada))
        print("Hexadecimal:", hex(entrada))
        print("Decimal:", float(entrada))
        break
    except ValueError:
        print("Entrada inválida! Impossível converter")
