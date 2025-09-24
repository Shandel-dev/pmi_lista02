# conjuntos de caracteres
maius = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minus = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
simb = "!@#$%&*?"

senha = ""
i = 0

# adicionar pelo menos 1 de cada tipo
while i < 1:
    senha += maius[i]      # 'A'
    senha += minus[i]      # 'a'
    senha += nums[i]       # '0'
    senha += simb[i]       # '!'
    i += 1

# completar até 8 caracteres repetindo minúsculas
i = len(senha)
while i < 8:
    senha += minus[i % len(minus)]
    i += 1

print("Senha gerada:", senha)
