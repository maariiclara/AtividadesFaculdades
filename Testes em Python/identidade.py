a = [10, 20, 30]
b = [10, 20, 30]
c = a

if (a is b):
    print("A é o mesmo objeto que B")
else:
    print("A náo é o é objeto que B")


if (a is c):
    print("A é o mesmo objeto que C") 
else:
    print("A náo é o é objeto que C")

'''
(is, is not)
Exercício: Crie duas listas com os mesmos elementos, por exemplo: a = [1,
2] e b = [1, 2]. Crie uma terceira variável c = a. Use o operador de identidade
para verificar se a é o mesmo objeto que b e se a é o mesmo objeto que c.
'''