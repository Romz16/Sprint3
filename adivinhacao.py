print("*********************************")
print("Bem vindo ao jogo de Advinhação!")
print("*********************************")

numero_secreto = 42
chute =  int( input("Digite o seu número: "))
print("você digitou o número : ", chute)
if (numero_secreto == chute):
    print("você acertou")
else:
    print("voce errou")