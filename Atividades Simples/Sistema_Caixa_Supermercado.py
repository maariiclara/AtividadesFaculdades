continuar = 1
desconto = 5
valor_total = 0
preco = 0
media = 0

quantidade = 0
while continuar != 0 :
    preço = float (input( "qual o preço do produto: "))
    while preço < 0 :
        print("valor invalido")
        preço = float (input( "qual o preço do produto: "))

    valor_total += preço
    quantidade += 1
    continuar = float (input("deseja continuar: "))
    media = valor_total / quantidade

    pagamento = int(input("Qual forma de pagamento? (1 - Dinheiro / 2 - Cartão): "))


if pagamento == 1:

    valor_total = valor_total - (valor_total * desconto / 100)

    print (f"valor total: {valor_total}")
    print(f"quantidade de produtos: {quantidade}")
    print(f"media de preço por produtos: {media}")

else:
    print (f"Valor total: {valor_total}")
    print (f"Quantidade de produtos: {quantidade}")
    print (f"media de preço por produtos: {media} ")


'''   
Contexto: Você deve criar um programa que simule o fechamento do caixa de
uma loja. O programa deve ler os preços dos produtos de um cliente, mas não
sabe quantos produtos ele comprou.

Requisitos do Algoritmo:
1. Entrada Infinita: O programa deve perguntar o preço do produto
repetidamente.

2. Condição de Parada: O usuário deve digitar 0 (zero) quando quiser
encerrar a compra.

3. Validação de Dados: O programa não pode aceitar preços negativos.
Se o aluno digitar um valor negativo, o programa deve exibir &quot;Valor
Inválido&quot; e pedir o preço novamente (Dica: use um while dentro de
outro).

4. Processamento:
- Somar o valor total da compra.
- Contar quantos produtos foram comprados.

5. Finalização: Ao digitar 0, o programa deve exibir:
- O total da conta.
- A quantidade de itens.
- A média de preço por produto.

- Bônus: Pergunte qual a forma de pagamento (1 - Dinheiro / 2 - Cartão).
Se for Dinheiro, aplique 5% de desconto no total.
'''