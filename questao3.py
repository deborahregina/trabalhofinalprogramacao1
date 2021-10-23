progranaOn = True
while (progranaOn):

    print("HOTEL DOS ANIMAIS\nEspecificando posições: ")
    print("[1, 2, 3, 4]\n[5, 6, 7, 8]")

    print('Bem vindo a fase 1!\nNa fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os '
          'quartos: \n')
    print("['*', '*', '-', 'G']\n['R', '-' ,'*', '*']")
    listaJogo = [['*', '*', '-', 'G'], ['R', '-', '*', '*']]
    print("em qual posição quer alocar o RATO?")
    i = int(input())
    if i == 3:
        frasefinal = "você perdeu!"
    print("em qual posição quer alocar o GATO?")
    j = int(input())

    if j == 6:
        frasefinal = "você perdeu!"

    else:
        frasefinal = "você passou para proxima fase!\n"

    if frasefinal == "você perdeu!":
        print(frasefinal)
        progranaOn = False
        break;
    else:
        print(frasefinal)

    print("[1, 2, 3, 4]\n[5, 6, 7, 8]\n")
    print("Bem vindo a fase 2! Na fase 2, o jogador deve alocar CÃO, CÃO e OSSO na seguinte matriz que representa os "
          "quartos: \n")

    print("['-', '*', '*', '*']\n['*', 'C' ,'-', '-']")
    listaJogo = [['-', '*', '*', '*'], ['*', 'C', '-', '-']]
    print ("Em qual posição quer alocar o CÃO?")
    i = int(input())
    print("Em qual posição quer alocar o CÃO?")
    j = int(input())
    print("Em qual posição quer alocar o OSSO?")
    k = int(input())

    if k == 1:
        frasefinal = "você passou para proxima fase!\n"
    else:
        frasefinal = "você perdeu!"

    if frasefinal == "você perdeu!":
        print(frasefinal)
        progranaOn = False
        break;
    else:
        print(frasefinal)
    print("[1, 2, 3, 4]\n[5, 6, 7, 8]\n")
    print("Bem vindo a fase 3! Na fase 3, o jogador deve alocar GATO, RATO e OSSO na seguinte matriz que representa os "
          "quartos: \n")

    print("['-', '*', '*', '*']\n['-', 'G' ,'-', '*']")
    listaJogo = [['-', '*', '*', '*'], ['*', 'C', '-', '-']]
    print("Em qual posição quer alocar o GATO?")
    i = int(input())
    print("Em qual posição quer alocar o RATO?")
    j = int(input())
    print("Em qual posição quer alocar o OSSO?")
    k = int(input())

    if i == 7 and j == 1 and k == 5:
        frasefinal = "você passou para proxima fase!"
    else:
        frasefinal = "você perdeu!"

    if frasefinal == "você perdeu!":
        print(frasefinal)
        progranaOn = False
        break;
    else:
        print(frasefinal)
    print("[1, 2, 3, 4]\n[5, 6, 7, 8]\n")
    print("Bem vindo a fase 4! Na fase 4, o jogador deve alocar QUEIJO, QUEIJO e OSSO na seguinte matriz que representa os "
          "quartos: \n")

    print("['-', '-', '-', '*']\n['*', 'R' ,'*', '*']")
    listaJogo = [['-', '*', '*', '*'], ['*', 'C', '-', '-']]
    print("Em qual posição quer alocar o QUEIJO?")
    i = int(input())
    print("Em qual posição quer alocar o QUEIJO?")
    j = int(input())
    print("Em qual posição quer alocar o OSSO?")
    k = int(input())

    if k == 2:
        frasefinal = "você passou para proxima fase!\n"
    else:
        frasefinal = "você perdeu!"

    if frasefinal == "você perdeu!":
        print(frasefinal)
        progranaOn = False
        break;
    else:
        print("vocÊ ganhou!")