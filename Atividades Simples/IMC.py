altura = float(input("Digite a sua altura (metros): "))
peso = float(input("Digite o seu peso: "))

imc = peso / (altura * altura)

if (imc < 18.5):
    print("")
    print(f"Seu IMC é de: {imc:.2f}")
    print("Você está abaixo do peso normal")
    print("")
elif (imc > 18.5) and (imc < 24.9):
    print("")
    print(f"Seu IMC é de: {imc:.2f}")
    print("Você está com um peso normal")
    print("")
elif (imc > 25.0) and (imc < 29.9):
    print("")
    print(f"Seu IMC é de: {imc:.2f}")
    print("Você está com sobrepeso")
    print("")
elif (imc > 30) and (imc < 34.9):
    print("")
    print(f"Seu IMC é de: {imc:.2f}")
    print("Você está com obesidade grau I")
    print("")
else:
    print("")
    print(f"Seu IMC é de: {imc:.2f}")
    print("Você está com obesidade grau II")
    print("")

# ** _ = elevado e coloca o numero a ser elevado depois

"""
print("")
print(f"Seu IMC é de: {imc:.2f}")
print("")
"""