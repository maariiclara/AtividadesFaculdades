'''
a = [1, 2, 3]
b = [1, 2, 3]
c = a

colocar - id(a)

vai mostra o id e mesmo sendo listas iguais mas em variaveis diferentes - elas tem diferentes id (enderecos)
oq muda qaundo vc atribui uma lista a outra lista - ai sao iguais - tem o mesmo id

is = posicao de memoria

a == b = true pq esta comparando valores e nao posicao de  memoria
'''

teste1 = 20
teste2 = teste1

print(f"{teste1 is teste2}")

teste1 += 10

print(f"{teste1 is teste2}")

teste1 -= 10

print(f"{teste1 is teste2}")