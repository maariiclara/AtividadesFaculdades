compra = float(input("Digite qual foi o valor da compra: "))

if (compra > 500):
    desconto = compra * 0.3
    compra_desconto = compra * 0.7
    print(f"Seu desconto é de: {desconto:.2f}")
    print(f"O total da sua compra com desconto de 30% é de: {compra_desconto:.2f}")
elif (compra > 200):
    desconto = compra * 0.2
    compra_desconto = compra * 0.8
    print(f"Seu desconto é de: {desconto:.2f}")
    print(f"O total da sua compra com desconto de 20% é de: {compra_desconto:.2f}")
elif (compra > 100):
    desconto = compra * 0.1
    compra_desconto = compra * 0.9
    print(f"Seu desconto é de: {desconto:.2f}")
    print(f"O total da sua compra com desconto de 10% é de: {compra_desconto:.2f}")
else:
    print(f"Infelizmente, você não vai ter desconto! O total da sua compra é de: {compra:.2f}")


''' 
compra = float(input("Digite qual foi o valor da compra: "))

if (compra > 500):
    desconto = compra * 0.7
    print(f"O total da sua compra com desconto de 30% é de: {desconto:.2f}") 
elif (compra > 200):
    desconto = compra * 0.8
    print(f"O total da sua compra com desconto de 20% é de: {desconto:.2f}")
elif (compra > 100):
    desconto = compra * 0.9
    print(f"O total da sua compra com desconto de 10% é de: {desconto:.2f}")
else:
    print(f"Infelizmente, você não vai ter desconto! O total da sua compra é de: {compra:.2f}")

'''