e = 2.718 # número de Euler = numero da base de log
resultado = 0 
potencia = 1 # pq todo numero elevado a 0 = 1
vezes = 0.001 # como o 'e' tem 3 casas decimais, tb tera q ser somado com 3 casas

numero = float(input("Digite um número: "))

while (numero <= 0):
  print("-- Número Inválido! --")
  numero = float(input("Digite um número: "))

while (potencia < numero): # vai ter uma repeticao ate chegar ao numero colocado
  resultado = resultado + vezes # resultado é o numero de vezes que foi repetido = contagem
  potencia = e ** resultado # cálculo de vezes que o 'e' se repetiu

print("")
print(f"ln({numero}) ≈ {resultado}")