def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secretra = "banana"
    letras_acertadas =["_","_","_","_","_","_"]
    enforcou =False
    acertou = False
    
    print(letras_acertadas)
    print("\n ")
    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip()
        index = 0
        for letra in palavra_secretra:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index]=letra
            index = index +1
                
        print(letras_acertadas)
        print("\n ")

    print("Fim de jogo")
    
if (__name__=="__main__"):
    jogar()
