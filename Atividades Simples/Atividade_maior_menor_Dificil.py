n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))


result = (n1 > n2 and "O primeiro número é maior que o segundo") or (n1 < n2 and "O primeiro número é menor que o segundo") or "Os dois números tem o mesmo valor" 

print(result)

'''
n = float(input('Digite um número: '))

resto = n % 2

result = ("par" * (1 - resto)) + ("impar" * (resto))

print('O número digitado é: ', result)

'''