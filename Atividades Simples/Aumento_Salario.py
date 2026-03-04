salario = float(input("Qual o valor do seu salário? "))

if (salario > 0):
    if (salario > 1500):
        aumento = salario * 0.05
        novo_salario = salario + aumento
        print(f"Salário atual: {salario:.2f}")
        print("Percentual aumentato: 5%")
        print(f"Valor do aumento: {aumento:.2f}")
        print(f"Novo salário: {novo_salario:.2f}")
    elif (700 < salario < 1500):
        aumento = salario * 0.1
        novo_salario = salario + aumento
        print(f"Salário atual: {salario:.2f}")
        print("Percentual aumentato: 10%")
        print(f"Valor do aumento: {aumento:.2f}")
        print(f"Novo salário: {novo_salario:.2f}")
    elif (280 < salario < 700):
        aumento = salario * 0.15
        novo_salario = salario + aumento
        print(f"Salário atual: {salario:.2f}")
        print("Percentual aumentato: 15%")
        print(f"Valor do aumento: {aumento:.2f}")
        print(f"Novo salário: {novo_salario:.2f}")
    else:
        aumento = salario * 0.2
        novo_salario = salario + aumento
        print(f"Salário atual: {salario:.2f}")
        print("Percentual aumentato: 20%")
        print(f"Valor do aumento: {aumento:.2f}")
        print(f"Novo salário: {novo_salario:.2f}")
else:
    print("Insira um número válido!")

'''
ate 280+ 20% 
de 280 e 700 + 15% 
700 e 1.500 + 10% 
mais de 1500 + 5%

na tela: 
salario antes, 
percentual aumentado, 
valor do aumento, 
novo salario
'''