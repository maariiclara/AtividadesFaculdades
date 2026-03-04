n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))

adicao = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao_real  = n1 / n2
divisao_inteira = n1 // n2
modulo = n1 % n2
potencia = n1 ** n2

print("")
print(f"A soma entre: {n1} + {n2} = {adicao:.2f}")
print(f"A subtração entre: {n1} - {n2} = {subtracao:.2f}")
print(f"A multiplicação entre: {n1} * {n2} = {multiplicacao:.2f}")
print(f"A divisão real entre: {n1} / {n2} = {divisao_real:.2f}")
print(f"A divisão inteira entre: {n1} // {n2} = {divisao_inteira:.2f}")
print(f"A resto da divisão entre: {n1} % {n2} = {modulo:.2f}")
print(f"A potenciação entre: {n1} ** {n2} = {potencia:.2f}")

'''
dois numeros inteiros 
soma, a diferenca, produto, divisao real, divisao inteira e o resto da divisao

Peça ao usuário dois números inteiros. Calcule e exiba a soma, a
diferença, o produto, a divisão real, a divisão inteira e o resto da divisão
(módulo) entre eles.
'''