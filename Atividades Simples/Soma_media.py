soma = 0

# repetir = 5
# x = len(range(repetir))
# for i in range(repetir):
# e a media entao teria que ser dividida pelo x - para nao dar erro

for i in range(5):
    x = int(input(f"Digite o {i+1}° número: "))
    soma += x

media = soma / 5

# print("")
print("\nA soma desses números é de:", soma)
print("A média desses números é de:", media)