inicio = int(input("Digite o primeiro número inteiro (inicio): "))
fim = int(input("Digite o segundo número inteiro (fim): "))

if inicio <= fim:
    passo = 6 # acrescenta esse valor, ex: inicio = 10 e fim = 40, vai aparecer assim: 10 -- 16 -- 22 -- 28 -- 34 -- 40 --
else:
    passo = -6 # diminui valor, ex: ex: inicio = 40 e fim = 10, vai aparecer assim: 40 -- 34 -- 28 -- 22 -- 16 -- 10 --

print(f"Números no intervalo entre {inicio} e {fim}: ")

for i in range(inicio, fim + passo, passo):
    print(i, end=" -- ")

# print(i, end=" -- ") -- espaco