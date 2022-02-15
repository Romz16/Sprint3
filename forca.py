import random
def jogar():
    
    
    mensagem_inicial()
    palavra_secreta=carrega_palavra()
    letras_acertadas =["_" for letra in palavra_secreta]
    letras_tentadas = []
    print(letras_acertadas)
    enforcou =False
    acertou = False
    erros = 0
    tentativas =0
    
    print("\n ")
    while(not enforcou and not acertou):
        chute = pega_chute()
        
        if chute in letras_tentadas:
            if tentativas == 0: 
                print("\nVocê ja tentou essa letra!Se tentar novamente vai para a forca\n") 
                tentativas= tentativas +1
            elif tentativas > 0:
                print("VOCÊ JÀ TENTOU ESSA LETRA!!!!")
                erros+=1
                desenha_forca(erros)
                tentativas = tentativas +1
             
    
        if chute in palavra_secreta:
           confere_chute(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        letras_tentadas.append(chute)
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        
        
        
        print(letras_acertadas)
        print("\n ") 

    if acertou:
        imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor(palavra_secreta)
    
    print("Fim de jogo")
    
    
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
        
        
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")
    
def carrega_palavra():
    arquivo = open("palavras.txt","r")
    palavras=[]
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def pega_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()
    return chute

def confere_chute(chute,letras_acertadas,palavra_secreta):
     index = 0
     for letra in palavra_secreta:
                if(chute== letra):
                    letras_acertadas[index]=letra
                index = index +1
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    
  
    
if (__name__=="__main__"):
    jogar()
