nome = input("Digite seu nome: ")
print("Olá", nome, "! Responda as perguntas abaixo com 'sim' ou 'não' ")

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

contador_sim = 0
contador_nao = 0

for pergunta in perguntas:
        
        resposta = input(pergunta + " ")

        if resposta == "sim" or resposta == "Sim" or resposta == "SIM":
            contador_sim += 1
           
        elif resposta == "não" or resposta == "nao" or resposta == "Não" or resposta == "Nao" or resposta == "NÃO" or resposta == "NAO":
            contador_nao += 1
            
        else:
            print(" Resposta inválida. Digite sim ou não.")

print("Resultado ")
print("Total de sim:", contador_sim)
print("Total de não:", contador_nao)

if contador_sim == 2:
    print("Classificação: Suspeita")
elif 3< contador_sim <= 4:
    print("Classificação: Cúmplice")
elif contador_sim == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")