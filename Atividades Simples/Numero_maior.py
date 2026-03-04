x = 0
maior = x

for i in range(5):
    x = int(input("Digite um valor para x: "))
 
    if (x > maior):
        maior = x

print("")
print("Esse é o número maior: ", maior)