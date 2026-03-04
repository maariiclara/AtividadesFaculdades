escolha = 0
escolha1 = 0
escolha2 = 0
escolha3 = 0
escolha4 = 0

pontos = 0
cont = 0
dado = ""

print("")
print("------- Seja Bem-vindo(a) ao Jogo Explorando o Planeta ClaraStar -------")
print("")

nome = str(input("Para começar, digite seu nome de usuário: "))
print("")


def inicio_jogo():
    print("")
    print(f"Vamos contextualizar a situação para vocë, {nome}")
    print("")
    print("Em um futuro distante, a humanidade alcançou as estrelas e iniciou a exploração de planetas distantes. " \
    "A bordo da nave intergaláctica 'Exploradora Estelar', uma tripulação composta por cientistas, engenheiros e aventureiros " \
    "chega ao planeta Alphara-7, um mundo misterioso repleto de paisagens alienígenas. ")
    print("")
    print("○ Ao aterrissar em Alphara-7, a tripulação sente a expectativa no ar. Equipados com trajes espaciais avançados, " \
    "eles começam a explorar a superfície do planeta, ansiosos por desvendar seus segredos.")
    condicao_de_exploracao()


def condicao_de_exploracao():
    global pontos
    print("")
    print("A tripulação já está explorando por um bom tempo, vocës encontaram algum um obstáculo físico no caminho (como uma montanha)?")
    while True:
        print("")
        print("******* Escolha Uma Opção: *******")
        print("* 1. Sim, encontramos!           *")
        print("* 2. Não, não encontramos!       *")
        print("**********************************")

        escolha = int(input("Escolha o número desejado: "))

        if escolha == 1:
            print("Felizmente vocës encontraram algo físico no jogo. Vocës ganharam 10 pontos! :) ")
            pontos += 10
            superar_obstaculo()
            break
        elif escolha == 2:
            print("Infelizmente vocës náo encontraram nada e terão que voltar ao início do jogo. Vocës perderam 10 pontos! :( ")
            pontos -= 10
            inicio_jogo()
            break
        else:
            print("** Opção inválida! Tente novamente. **")


def superar_obstaculo():
    global pontos
    print("")
    print("A tripulação tem que tomar uma decisão:")
    while True:
        print("")
        print("******* Escolha Uma Opção: *******")
        print("* 1. Queremos escalar!           *")
        print("* 2. Queremos contornar!         *")
        print("**********************************")

        escolha1 = int(input("Escolha o número desejado: "))

        if escolha1 == 1:
            print("A tripulação está tentanto escalar a montanha... ")
            escalar_montanha()
            break
        elif escolha1 == 2:
            print("A tripulação está contornando a montanha com sucesso... e continua a sua exploração! Vocës ganharam 10 pontos! :) ")
            pontos += 10
            condicao_cientifica()
            break
        else:
            print("** Opção inválida! Tente novamente. **")


def escalar_montanha():
    global pontos, cont
    print("")
    print("A tripulação...")
    while True:
        print("")
        print("******* Escolha Uma Opção: *******")
        print("* 1. Conseguiram escalar!        *")
        print("* 2. Não conseguiram escalar!    *")
        print("**********************************")

        escolha2 = int(input("Escolha o número desejado: "))

        if escolha2 == 1:
            print("A tripulação conseguiu escalar com sucesso! Vocës ganharam 20 pontos! :) ")
            pontos += 20
            condicao_cientifica()
            break
        elif escolha2 == 2:
            cont += 1
            pontos -= 10
            print("Falharam! -10 pontos")

            if cont >= 5:
                print("A tripulação não está se empenhando. Vocës perderam 20 pontos e voltaram ao início! :( ")
                pontos -= 20
                inicio_jogo()
                break
            else:
                superar_obstaculo()
                break
        else:
            print("** Opção inválida! Tente novamente. **")


def condicao_cientifica():
    global pontos, dado
    
    print("")
    print("A tripulação já está explorando por um bom tempo novamente, vocës encontaram alguma área rica em minerais ou sinais de vida? ")
    while True:
        print("")
        print("******* Escolha Uma Opção: *******")
        print("* 1. Sim, encontramos!           *")
        print("* 2. Não, não encontramos!       *")
        print("**********************************")

        escolha3 = int(input("Escolha o número desejado: "))

        if escolha3 == 1:
            print("Felizmente vocës coletaram dados científicos valiosos na área identificada! Vocës ganharam 10 pontos! :) ")
            dado = input("Quais dados vocës coletaram? ")
            pontos += 10
            dados_cientificos()
            break
        elif escolha3 == 2:
            print("Infelizmente vocës náo encontraram nada e terão que voltar a exploraçãoo. Vocës perderam 10 pontos! :( ")
            pontos -= 10
            condicao_de_exploracao()
            break
        else:
            print("** Opção inválida! Tente novamente. **")


def dados_cientificos():
    global pontos
    print("")
    print("A tripulação tem que tomar uma decisão:")
    while True:
        print("")
        print("******* Escolha Uma Opção: *******")
        print("* 1. Queremos prosseguir!        *")
        print("* 2. Queremos retornar à nave!   *")
        print("**********************************")

        escolha4 = int(input("Escolha o número desejado: "))

        if escolha4 == 1:
            print("Vocës decidiram prosseguir, portanto retornaram ao início da exploração. Vocës ganharam 20 pontos! :) ")
            pontos += 20
            condicao_de_exploracao()
            break
        elif escolha4 == 2:
            print("A tripulação retorna à Exploradora Estelar e parte de volta para a Terra, trazendo consigo as descobertas incríveis feitas durante a expedição. Vocës ganharam 10 pontos! :)")
            pontos += 10
            fim_jogo()
            break
        else:
            print("** Opção inválida! Tente novamente. **")


def fim_jogo():
    global pontos, dado
    print("")
    print("A tripulação retorna à Exploradora Estelar e parte de volta para a Terra, " \
    "trazendo consigo as descobertas incríveis feitas durante a expedição.")
    print("")
    print(f"Parabéns, {nome} vocë chegou ao fim do jogo!")
    print("")
    print(f"Dados Coletado(s): {dado}")
    print(f"Pontuação Final: {pontos} pontos")


# estrutura em si mesmo
while True:
    print("")
    print("***************** MENU *****************")
    print("* 1. Iniciar Jogo                      *")
    print("* 2. Sair do Jogo                      *")
    print("****************************************")
    print("")

    escolha = int(input("Escolha o número desejado: "))

    if escolha == 1:
        inicio_jogo()

    elif escolha == 2:
        print("")
        print("**** Infelizmente vocë não quer mais jogar ! :( ****")
        print("")
        break
    else:
        print("** Opção inválida! **")