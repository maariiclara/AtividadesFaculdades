n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))

maior = n1 > n2
iguais = n1 == n2
diferente = n1 != n2

print(f"O primeiro é maior que o segundo? {maior}")
print(f"Os dois números sao igauis? {iguais}")
print(f"O primeiro é diferenre que o segundo? {diferente}")

'''
Receba dois valores numéricos e retorne uma série de
booleanos (True ou False) verificando se o primeiro é maior que o segundo,
se são iguais e se o primeiro é diferente do segundo.
'''