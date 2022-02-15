def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secretra = "banana".upper()
    letras_acertadas =["_","_","_","_","_","_"]
    enforcou =False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    print("\n ")
    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()
        index = 0
        if chute in palavra_secretra:
            for letra in palavra_secretra:
                if(chute== letra):
                    letras_acertadas[index]=letra
                index = index +1
        else:
            erros = erros +1
            
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
                
        print(letras_acertadas)
        print("\n ")

    print("Fim de jogo")
    
if (__name__=="__main__"):
    jogar()
