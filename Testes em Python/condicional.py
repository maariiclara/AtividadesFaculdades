idd = int(input("Digite sua idade: "))

if (idd >= 18):
    print("Adulto")
elif (idd > 13) and (idd <= 17):
    print("Juvenil")
elif (idd > 5) and (idd <= 12):
    print("Juvenil")
else:
    print("Idade Inválida")

'''
(IF, ELIF, ELSE):
Exercício: Desenvolva um programa que receba a idade de um nadador e
classifique-o em uma das seguintes categorias:
• Infantil: 5 a 12 anos;

• Juvenil: 13 a 17 anos;
• Adulto: 18 anos ou mais;
• Inválido: Menor que 5 anos.
'''