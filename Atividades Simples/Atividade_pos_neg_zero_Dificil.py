'''
n = float(input('Digite um número: '))

zero = n == 0
pos = n >= 1
neg = n < 0

print('O número digitado é igual a zero: ', zero)
print('O número digitado é positivo: ', pos)
print('O número digitado é negativo: ', neg)
'''

n = float(input('Digite um número: '))

result = (n == 0 and "zero") or (n >= 1 and "positivo") or "negativo"

print('O número digitado é: ', result)



'''
n = float(input('Digite um número: '))

result = ("positivo" * (n > =1)) or ("negativo" * (n > =1)) or ("zero" * (n > =1))

print('O número digitado é: ', result)

'''