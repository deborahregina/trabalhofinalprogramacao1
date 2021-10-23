from random import seed
from random import randint

listaalunos = []

def menuNovaInscricao():
    nome = input("Digite seu nome: ")
    email = input("Digite email: ")
    telefone = input("Digite telefone: ")
    curso = input("Digite curso: ")
    seed(100)
    voucher = randint(100, 400)
    dicionario = {
        "Voucher": voucher,
        "Nome": nome,
        "Email": email,
        "Telefone": telefone,
        "Curso": curso
    }
    listaalunos.append(dicionario)



def menuVisualizaInscricao(lista):
    print(lista)


def menuPrincipal():
    op = True
    while (op):
        print("*********Menu*********");
        menuop = int(input("1- Nova inscrição \n2- Visualizar inscrição \n0- Encerrar \nOpção escolhida: "));
        if menuop == 1:
            menuNovaInscricao()
        elif menuop == 2:
            if len(listaalunos) != 0:
                print("---------------Lista inscritos---------------")
                menuVisualizaInscricao(listaalunos)
                print("---------------")
            else:
                print("Nenhuma inscrição cadastrada")
        elif menuop == 0:
            op = False;
        else:
            print("Erro: digite uma opção válida!")


listaalunos = []
menuPrincipal();
