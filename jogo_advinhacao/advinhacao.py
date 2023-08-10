print("*******************************")
print("Bem-vindo ao jogo de advinhacao")
print("*******************************")

numero_secreto = 42

chute_str = input("Digite o seu numero: ")

print("Voce digitou ", chute_str)

chute = int(chute_str)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Voce acertou!")
else:
    if(maior):
        print("Voce errou! o seu chute foi maior que seu numero secreto")
    elif(menor):
        print("Voce errou! o seu chute foi menor que seu numero secreto")

print("Fim do game!")