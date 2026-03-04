# mostre os numeros de 1.000 e 2.000  
# divididos por 11 tenham resto = 2
cont = 0

for i in range(1000, 2000): 
    if (i % 11 == 2):
        print(i, end=" - ")
        cont += 1

print("")
print("")
print(f"No total tem: {cont} números que tem o resto 2 quando divididos por 11")
print("")