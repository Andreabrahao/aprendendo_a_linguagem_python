import random
def jogar():
    print("*******************************")
    print("Bem-vindo ao jogo de advinhacao")
    print("*******************************")

    numero_secreto = random.randrange(1, 51)
    total_de_tentativas = 0
    pontos = 100

    print("Qual nivel de dificuldade?")
    print("(1) Facil, (2) Medio, (3) Dificil")

    nivel = int(input("Define o nivel: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 50: ")
        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 50):
            print("Voce deve digitar um numero entre 1 e 50")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        perdeu = rodada >= total_de_tentativas

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            print("Fim do game!")
            break
        else:
            if (maior):
                print("Voce errou! o seu chute foi maior que seu numero secreto")
            elif (menor):
                print("Voce errou! o seu chute foi menor que seu numero secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        if (perdeu):
            print("Voce nao tem mais chance!")

if(__name__ == "__main__"):
    jogar()