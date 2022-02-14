import random


print("*********************************")
print("Bem vindo ao jogo de Advinhação!")
print("*********************************")


numero_secreto = (random.randrange(1,101))
tentativas = 0
rodada = 1 
pontos = 1000

print("Qual dificuldade deseja? \n")
print("1-fácil\n2-Médio\n3-Difícil\n")
nivel = int( input("Digite o nivel"))

while(nivel>3 or nivel<1):
    print("Erro, selecione uma dificuldade valida\n")
    print("Qual dificuldade deseja? \n")
    print("1-fácil\n2-Médio\n3-Difícil\n")
    nivel = int( input("Digite o nivel"))

if nivel ==1:
        tentativas = 20
elif nivel ==2:
        tentativas =10
elif nivel ==3:
        tentativas =5

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
        print("você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou!! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Você errou!! O seu chute foi menor que o numero secreto.") 
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        
if rodada == tentativas:
    print("O numero secreto era:",numero_secreto)
print("Fim de jogo")
