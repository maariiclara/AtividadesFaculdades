num = int(input("Digite um número para saber a tabuada dele: "))

for i in range(10):
    x = num * (i + 1)
    print(f"{num} * {i+1} = {x}")

'''
Peça um número inteiro ao usuário e exiba a tabuada de
multiplicação desse número de 1 a 10 utilizando o laço for e a
função range().
'''