
#Este jogo consiste em acertar o número secreto, envolvendo várias regras simples
import random
print("***********************************")
print("*bem vindo no jogo de adivinhação!*")
print("***********************************")

numero_secreto = random.randrange(1, 11)
numero_de_tentativas = 0
pontos = 100

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("define o nível: "))
# Define o Nível de dificuldade com número de tentativas

if(nivel == 1):
    numero_de_tentativas = 7
elif(nivel == 2):
    numero_de_tentativas = 5
else:
    numero_de_tentativas = 3

    #Estrutura de repetição for .
for rodada in range (1, numero_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, numero_de_tentativas))
    chute_str = input("Digite um número entre 1 e 10: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)
    
    if (chute <1 or chute > 10):
        print("você deve digitar um número entre 1 e 10!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    
    

    if(acertou):
        print("Parabéns, você acertou, seu total de pontos foi {}!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! Seu chute ultrapassou o número secreto!")
        elif(menor):
            print(" Você errou! Seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim do Jogo!")
#Fim do Jogo
