import forca
import adivinhacao


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")


print("(1)Forca  (2)Adivinhação")

jogo=  int(input("QUAL JOGO?"))

if (jogo == 1 ):
    print("forca")
    forca.jogar()
elif(jogo ==2):
    print("adivinhação")
    adivinhacao.jogar()
    