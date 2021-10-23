
progranaOn = True
while (progranaOn):

    print \
        ('Bem vindo a fase 1!\nNa fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos: \n')
    print("['*', '*', '-', 'G']\n['R', '-' ,'*', '*']")
    listaJogo = [['*', '*', '-', 'G'], ['R', '-', '*', '*']]
    print("em qual posição quer alocar o RATO?")
    i = int(input())
    if i == 3:
            frasefinal = "Game Over!"
    print("em qual posição quer alocar o GATO?")
    j = int(input())

    if j == 6:
        frasefinal = "Game Over!"

    if i == 6 and j == 3:
       frasefinal = "você passou para proxima fase!"

    if frasefinal == "Game Over!":
         print(frasefinal)
         progranaOn = False
         break;
    else:
        print(frasefinal)

