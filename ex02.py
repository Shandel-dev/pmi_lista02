notas = []
soma = 0
print("Cálculo da média das notas de um aluno")
i = 1
while i <= 4:
    while True:
        try:
            num = float(input(f"Digite a {i}° nota: "))
            if num >= 0 and num <= 10:
                notas.append(num)
                soma += num
                i += 1
                break
            else:
                print("A nota deve ser entre 0 e 10")
        except ValueError:
            print("Digite uma nota válida!")

media = soma / len(notas)
print(f"Média final: {media}")
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


