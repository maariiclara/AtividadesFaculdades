continuar = 1
cont = 0
soma = 0
desconto = 0.05

while continuar != 0:
    preco = float(input("Digite o preço do produto: "))
    
    while preco < 0:
        print("Digite um preço válido!")
        preco = float(input("Digite o preço do produto: "))

    soma += preco
    cont += 1
    media = soma / cont

    continuar = int(input("Deseja continuar? (1 - Sim / 0 - Não): "))

pagamento = int(input("Qual forma de pagamento? (1 - Dinheiro / 2 - Cartão): "))

if pagamento == 1:
    soma = soma - (soma * desconto)

print("")
print(f"Total da compra: {soma:.2f}")
print(f"Quantidade de Itens: {cont}")
print(f"Média de Preço por Produto: {media:.2f}")

# Poderia usar o While True e depois usar um if preco == 0: break