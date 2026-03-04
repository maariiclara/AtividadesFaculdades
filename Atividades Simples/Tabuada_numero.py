num = int(input("Digite um número para saber a tabuada dele: "))

for i in range(10):
    x = num * (i + 1)
    print(f"{num} * {i+1} = {x}")