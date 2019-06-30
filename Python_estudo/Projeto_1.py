
#Este jogo consiste em acertar o número secreto, envolvendo várias regras simples

print("***********************************")
print("*bem vindo no jogo de adivinhação!*")
print("***********************************")

numero_secreto = 10
numero_de_tentativas = 3
rodada = 1

while(rodada <= numero_de_tentativas):
    print("tentativa {} de {}".format(rodada, numero_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = numero_secreto < chute
    menor   = numero_secreto > chute

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Seu chute ultrapassou o número secreto!")
        elif(menor):
            print("seu chute foi menor que o nmero secreto")
    rodada = rodada + 1
    

print("Fim do Jogo!")