print("*******************************")
print("Bem-vindo ao jogo de advinhacao")
print("*******************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    perdeu = rodada >= total_de_tentativas

    if(acertou):
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Voce errou! o seu chute foi maior que seu numero secreto")
        elif(menor):
            print("Voce errou! o seu chute foi menor que seu numero secreto")
    if(perdeu):
        print("Voce nao tem mais chance!")

    rodada = rodada + 1

print("Fim do game!")