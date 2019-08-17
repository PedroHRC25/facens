import os
os.system("cls")
segredo=input("PLAYER 1-Digite a palavra para o Player 2 acertar (minuscula e sem acentos):")
#as letras devem ser todas maiúsculas
tentativas=3
estado="_ " * len(segredo)
historico=""
while "_" in estado and tentativas>0:
    print(estado)
    print("")
    print(tentativas,"Tentativas")
    letra=input("Uma letra:")
    historico=historico+letra
    if letra in segredo:
        print("Letra Correta")
        os.system("cls")
    else:
        print("Letra Incorreta")
        tentativas=tentativas - 1
        print(tentativas,"Tentativas")
        os.system("cls")
    estado=""
    for elemento in segredo:
        if elemento in historico:
            estado=estado+elemento
        else:
            estado=estado+"_"
        estado=estado+" "
    
if tentativas > 0:
    print("#--------------#")
    print("| Você Venceu! |")
    print("#--------------#")
    print("A palavra era:",segredo)
else:
    print("#-----------------------#")
    print("| Errrrrouuuuuuuuu!!!!! |")
    print("#-----------------------#")
    print("A palavra era:",segredo)

