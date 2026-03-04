nome = input("Digite seu nome completo ou alguma frase:")
i = 0

for letra in nome:
    if letra in "aeiouAEIOU":
        i += 1

print(f"O total de vogais encontradas é de: {i}")