nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))

media = (nota1 + nota2) / 2

if (media >= 7):
    print("Sua média foi de: ", media, "Parabéns, você foi aprovado!")
else:
    print("Sua média foi de: ", media, "Infelizmente, você foi reprovado!")