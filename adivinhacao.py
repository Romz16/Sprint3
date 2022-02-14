print("*********************************")
print("Bem vindo ao jogo de Advinhação!")
print("*********************************")

numero_secreto = 42

tentativas = 3
rodada = 1 


while(rodada<=tentativas):
    print("Tentativa: ", rodada,"de", tentativas)
    chute =  int( input("Digite o seu número: "))
    print("você digitou o número : ", chute)

    acertou = numero_secreto == chute
    maior = numero_secreto <chute
    menor = numero_secreto > chute

    if (acertou):
        print("você acertou!")
        rodada = rodada +10
    else:
        if(maior):
            print("Você errou!! O seu chute foi maior que o numero secreto.")
        elif(menor):
            print("Você errou!! O seu chute foi menor que o numero secreto.") 
        rodada = rodada + 1 
print("Fim de jogo")
