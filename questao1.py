opcao = 1


def imprimirinfos(nomeCrianca, idadeCrianca, grauInstrucao):    # método para imprimir infos do aluno
    print('A criança ' + nomeCrianca + ' tem ' + idadeCrianca + ' anos e está em ' + grauInstrucao)


while opcao != '0':     # Roda instruções até que pessoa escolha não continuar
    nomeCrianca = input('Nome da criança: ')
    idadeCrianca = int(input('Idade da criança: '))
    if (idadeCrianca < 1):
        print('Digite uma idade válida.')
    if (idadeCrianca >= 1 and idadeCrianca <= 5):
        grauinstrucao = 'Educação Infantil'
        imprimirinfos(nomeCrianca, str(idadeCrianca), grauinstrucao)
    elif (idadeCrianca >= 6 and idadeCrianca <= 10):
        grauinstrucao = 'Ensino Fundamental I'
        imprimirinfos(nomeCrianca, str(idadeCrianca), grauinstrucao)
    elif (idadeCrianca >= 11 and idadeCrianca <= 14):
        grauinstrucao = 'Ensino Fundamental II'
        imprimirinfos(nomeCrianca, str(idadeCrianca), grauinstrucao)
    elif (idadeCrianca >= 15):
        grauinstrucao = 'Ensino médio'
        imprimirinfos(nomeCrianca, str(idadeCrianca), grauinstrucao)

    print('Deseja continuar?  0 - Não   1 - Sim')
    opcao = input()
