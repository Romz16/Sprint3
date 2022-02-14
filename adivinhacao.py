import random


print("*********************************")
print("Bem vindo ao jogo de Advinhação!")
print("*********************************")

numero_secreto = (random.randrange(1,101))

tentativas = 3
rodada = 1 

for rodada in range (1,tentativas+1):
    print("Tentativa: {} de {}".format(rodada,tentativas))
    chute =  int( input("Digite um número entre 1 e 100: "))
    if(chute < 1 or  chute>100 ):
        print("Você deve digitar um número entre 1 e 100")
        continue
    
    print("você digitou o número : ", chute)

    acertou = numero_secreto == chute
    maior = numero_secreto <chute
    menor = numero_secreto > chute

    if (acertou):
        print("você acertou!")
        break
    else:
        if(maior):
            print("Você errou!! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Você errou!! O seu chute foi menor que o numero secreto.") 
            
if rodada == 3:
    print("O numero secreto era:",numero_secreto)
print("Fim de jogo")
