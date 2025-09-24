jogo = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

jogador = "X"
jogadas = 0

while True:
    # Exibir tabuleiro
    i = 0
    while i < 3:
        print(jogo[i][0], "|", jogo[i][1], "|", jogo[i][2])
        if i < 2:
            print("---------")
        i += 1

    # Entrada da jogada
    try:
        x = int(input(f"Jogador {jogador}, linha (0-2): "))
        y = int(input(f"Jogador {jogador}, coluna (0-2): "))

        if jogo[x][y] != " ":
            print("Posição ocupada, tente de novo.")
            continue
        jogo[x][y] = jogador
        jogadas += 1
    except (ValueError, IndexError):
        print("Entrada inválida, tente de novo.")
        continue

    # Verificação de vitória
    i = 0
    ganhou = False
    while i < 3:
        if jogo[i][0] == jogador and jogo[i][1] == jogador and jogo[i][2] == jogador:
            ganhou = True
        if jogo[0][i] == jogador and jogo[1][i] == jogador and jogo[2][i] == jogador:
            ganhou = True
        i += 1

    # Diagonais
    if jogo[0][0] == jogador and jogo[1][1] == jogador and jogo[2][2] == jogador:
        ganhou = True
    if jogo[0][2] == jogador and jogo[1][1] == jogador and jogo[2][0] == jogador:
        ganhou = True

    if ganhou:
        i = 0
        while i < 3:
            print(jogo[i][0], "|", jogo[i][1], "|", jogo[i][2])
            if i < 2:
                print("---------")
            i += 1
        print(f"Jogador {jogador} venceu!")
        break

    if jogadas == 9:
        print("Empate!")
        break

    # Alternar jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
