
import random

casaNome = "" #Variável que mostra o nome da cada do tabuleiro
terrenos = "" #Variável que mostra os respectivos terrenos, com seu id, preço e aluguel, formatado em (00)ID, (000)Preço, (000)Aluguel
#IDs = 00 = Sem proprietário / 06 = Ponto de partida / 01~05 = Reservado a jogadores / 07 = Imposto / 08 = Vá para prisão / 09 = Prisão / 10 = Jackpot

#CÓDIGO
numJogadores = int(input("Digite o número de jogadores (De 2 a 5 jogadores): "))
while(numJogadores<2 or numJogadores>5):
    print("Apenas 2 a 5 jogadores")
    numJogadores = int(input("Digite o número de jogadores (De 2 a 5 jogadores): "))
for i in range(0, numJogadores):
    print("Digite o nome do" ,(i+1), "jogador")
    nome = input()
    if(i==0):
        nome1 = nome
    elif(i==1):
        nome2 = nome
    elif(i==2):
        nome3 = nome
    elif (i==3):
        nome4 = nome
    elif(i==4):
        nome5 = nome
status1 = ""
status2 = ""
status3 = ""
status4 = ""
status5 = ""
posicao1 = 0
posicao2 = 0
posicao3 = 0
posicao4 = 0
posicao5 = 0
casaNome1 = ""
casaNome2 = ""
casaNome3 = ""
casaNome4 = ""
casaNome5 = ""
spacecoins1 = 10000
spacecoins2 = 10000
spacecoins3 = 10000
spacecoins4 = 10000
spacecoins5 = 10000
pertence1=""
pertence2=""
pertence3=""
pertence4=""
pertence5=""
pertence6=""
pertence7=""
pertence8=""
pertence9=""
pertence10=""
pertence11=""
pertence12=""
pertence13=""
pertence14=""
pertence15=""
pertence16=""
pertence17=""
pertence18=""
pertence19=""
pertence20=""
pertence21=""
pertence22=""
pertence23=""
pertence24=""
entendo1 = ""
entendo2 = ""
entendo3 = ""
entendo4 = ""
entendo5 = ""
while True:
    for i in range (0, numJogadores):
        if(i==0):
            if(entendo1=="entendo"):
                continue;
            else:
                print()
                print(nome1, "sua vez de jogar")
                jogar = ""
                if(spacecoins1<=0):
                    print("Você ficou sem dinheiro, fim de jogo pra você!")
                    while (entendo1 != "entendo"):
                        print("Digite entendo para concordar que faliu")
                        entendo1 = input()
                    continue;
                else:
                    while(jogar != "encerrar"):
                        print()
                        print(nome1, ", digite:")
                        print("1 - Para saber sua posição na galáxia")
                        print("2 - Para saber quantos Spacecoins possui")
                        print("3 - Para ver seus territórios comprados")
                        print("sair - Para sair do jogo")
                        print("jogar - Para jogar os dados")
                        jogada = input()
                        if (jogada=="1"):
                            print("Posição:" ,posicao1,casaNome1)
                        elif (jogada=="2"):
                            print("Spacecoins:" ,spacecoins1)
                        elif(jogada=="sair"):
                            entendo1 = "entendo"
                            break;
                        elif (jogada=="3"):
                            print("Seus terrenos:")
                            if(pertence1!=nome1 and pertence2!=nome1 and pertence3!=nome1 and pertence4!=nome1 and pertence5!=nome1 and pertence6!=nome1 and pertence7!=nome1 and pertence8!=nome1 and pertence9!=nome1 and pertence10!=nome1 and pertence11!=nome1 and pertence12!=nome1 and pertence15!=nome1 and pertence16!=nome1 and pertence17!=nome1 and pertence18!=nome1 and pertence19!=nome1 and pertence20!=nome1 and pertence21!=nome1 and pertence22!=nome1 and pertence23!=nome1 and pertence24!=nome1):
                                print("Você nao possui nenhum terreno")
                            if(pertence1==nome1):
                                print(id1)
                            if(pertence2==nome1):
                                print(id2)
                            if(pertence3==nome1):
                                print(id3)
                            if(pertence4==nome1):
                                print(id4)
                            if(pertence5==nome1):
                                print(id5)
                            if(pertence6==nome1):
                                print(id6)
                            if(pertence7==nome1):
                                print(id7)
                            if(pertence8==nome1):
                                print(id8)
                            if(pertence9==nome1):
                                print(id9)
                            if(pertence10==nome1):
                                print(id10)
                            if(pertence11==nome1):
                                print(id11)
                            if(pertence12==nome1):
                                print(id12)
                            if(pertence13==nome1):
                                print(id13)
                            if(pertence14==nome1):
                                print(id14)
                            if(pertence15==nome1):
                                print(id15)
                            if(pertence16==nome1):
                                print(id16)
                            if(pertence17==nome1):
                                print(id17)
                            if(pertence18==nome1):
                                print(id18)
                            if(pertence19==nome1):
                                print(id19)
                            if(pertence20==nome1):
                                print(id20)
                            if(pertence21==nome1):
                                print(id21)
                            if(pertence22==nome1):
                                print(id22)
                            if(pertence23==nome1):
                                print(id23)
                            if(pertence24==nome1):
                                print(id24)

                        elif (jogada=="jogar" or jogada=="Jogar"):
                            if(status1=="preso"):
                                dado = 0
                            else:
                                dado = random.randint(1,6)
                            posicao1 += dado
                            if (posicao1==1):
                                casaNome1 = "- Fronteira Intergalática/Portões do Universo"
                                id1 = "1 - Fronteira Intergalática/Portões do Universo"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if(pertence1=="" or pertence1==nome1):
                                    print("Você deseja comprar este território por" ,preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if(comprar=="sim"):
                                        if(preco!=0):
                                            if(pertence1==nome1):
                                                print("Esse território já é seu")
                                                while(jogar!="encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif(pertence1==""):
                                                spacecoins1-=preco
                                                pertence1=nome1
                                                print("Território adquirido")
                                                print("Agora você possui" ,spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é" ,aluguel, "Spacecoins")
                                    spacecoins1-=aluguel
                                    print("Agora você possui" ,spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==2):
                                casaNome1 = "- Base Interplanetária de Vênus"
                                id2 = "2 - Base Interplanetária de Vênus"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence2 == "" or pertence2 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence2 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence2 == ""):
                                                spacecoins1 -= preco
                                                pertence2 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==3):
                                id3 = "3 - Base Interplanetária da Terra"
                                casaNome1 = "- Base Interplanetária da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence3 == "" or pertence3 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence3 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence3 == ""):
                                                spacecoins1 -= preco
                                                pertence3 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==4):
                                id4 = "4 - Base Interplanetária de Marte"
                                casaNome1 = "- Base Interplanetária de Marte"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence4 == "" or pertence4 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence4 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence4 == ""):
                                                spacecoins1 -= preco
                                                pertence4 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==5):
                                id5 = "5 - Base Interplanetária de Júpiter"
                                casaNome1 = "- Base Interplanetária de Júpiter"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence5 == "" or pertence5 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence5 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence5 == ""):
                                                spacecoins1 -= preco
                                                pertence5 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==6):
                                id6 = "6 - Base Interplanetária de Saturno"
                                casaNome1 = "- Base Interplanetária de Saturno"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence6 == "" or pertence6 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence6 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence6 == ""):
                                                spacecoins1 -= preco
                                                pertence6 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==7):
                                id7 = "7 - Prisão Univeral/Passagem de Visitantes"
                                casaNome1 = "- Prisão Univeral/Passagem de Visitantes"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (status1 == "preso"):
                                    print("Você está preso e não pode jogar")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                    status1 = ""
                                else:
                                    if (pertence7 == "" or pertence7 == nome1):
                                        print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                        comprar = input()
                                        if (comprar == "sim"):
                                            if (preco != 0):
                                                if (pertence7 == nome1):
                                                    print("Esse território já é seu")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                                elif (pertence7 == ""):
                                                    spacecoins1 -= preco
                                                    pertence7 = nome1
                                                    print("Território adquirido")
                                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                            else:
                                                print("Este terreno não pode ser comprado")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                        spacecoins1 -= aluguel
                                        print("Agora você possui", spacecoins1, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()

                            elif(posicao1==8):
                                id8 = "8 - Base Lunar da Terra"
                                casaNome1 = "- Base Lunar da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence8 == "" or pertence8 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence8 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence8 == ""):
                                                spacecoins1 -= preco
                                                pertence8 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==9):
                                id9 = "9 - Base Lunar de Fobos"
                                casaNome1  = "- Base Lunar de Fobos"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence9 == "" or pertence9 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence9 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence9 == ""):
                                                spacecoins1 -= preco
                                                pertence9 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==10):
                                id10 = "10 - Base Lunar Europa"
                                casaNome1 = "- Base Lunar Europa"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence10 == "" or pertence10 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence10 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence10 == ""):
                                                spacecoins1 -= preco
                                                pertence10 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==11):
                                id11 = "11 - Base Lunar de Pandora"
                                casaNome1 = "- Base Lunar de Pandora"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence11 == "" or pertence11 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence11 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence11 == ""):
                                                spacecoins1 -= preco
                                                pertence11 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==12):
                                id12 = "12 - Base Lunar de Talassa"
                                casaNome1 = "- Base Lunar de Talassa"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence12 == "" or pertence12 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence12 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence12 == ""):
                                                spacecoins1 -= preco
                                                pertence12 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==13):
                                id13 = "13 - Satélite da sorte: JACKPOT"
                                casaNome1 = "- Satélite da sorte: JACKPOT"
                                preco = 0
                                aluguel = 0
                                print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                                print("Você precisa pensar em um número e lançar um dado. Se os números forem iguais você ganha 200 Spacecoins, mas se forem diferentes você perde 100 Spacecoins")
                                print("Digite um número de 1 a 6")
                                num = int(input())
                                dadoJack = random.randint(1,6)
                                if(num==dadoJack):
                                    spacecoins1+=200
                                    print("Parabéns você conseguiu!")
                                    print("Agora você possui" ,spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                else:
                                    spacecoins1-=100
                                    print("Não foi dessa vez!")
                                    print("Agora você possui" ,spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()

                            elif(posicao1==14):
                                id14 = "14 - Planeta anão: Plutão"
                                casaNome1 = "- Planeta anão: Plutão"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence14 == "" or pertence14 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence14 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence14 == ""):
                                                spacecoins1 -= preco
                                                pertence14 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==15):
                                id15 = "15 - Planeta anão: Éris"
                                casaNome1 = "- Planeta anão: Éris"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence15 == "" or pertence15 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence15 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence15 == ""):
                                                spacecoins1 -= preco
                                                pertence15 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==16):
                                id16 = "16 - Planeta anão: Haumea"
                                casaNome1 = "- Planeta anão: Haumea"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence16 == "" or pertence16 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence16 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence16 == ""):
                                                spacecoins1 -= preco
                                                pertence16 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==17):
                                id17 = "17 - Planeta anão: Ceres"
                                casaNome1 = "- Planeta anão: Ceres"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence17 == "" or pertence17 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence17 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence17 == ""):
                                                spacecoins1 -= preco
                                                pertence17 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==18):
                                id18 = "18 - Planeta anão: Makemake"
                                casaNome1 = "- Planeta anão: Makemake"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence18 == "" or pertence18 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence18 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence18 == ""):
                                                spacecoins1 -= preco
                                                pertence18 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==19):
                                id19 = "19 - Vá para a prisão universal!"
                                casaNome1 = "- Vá para a prisão universal!"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao1, casaNome1)
                                print("Você foi preso, será movido para casa 7(prisão) e ficará 1 rodada sem jogar")
                                posicao1 = 7
                                casaNome1 = "Prisão Univeral/Passagem de Visitantes"
                                status1 = "preso"
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao1==20):
                                id20 = "20 - Base extra-solar Gliese 581 d"
                                casaNome1 = "- Base extra-solar Gliese 581 d"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence20 == "" or pertence20 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence20 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence20 == ""):
                                                spacecoins1 -= preco
                                                pertence20 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==21):
                                id21 = "21 - Base extra-solar Upsilon Andromedae"
                                casaNome1 = "- Base extra-solar Upsilon Andromedae"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence21 == "" or pertence21 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence21 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence21 == ""):
                                                spacecoins1 -= preco
                                                pertence21 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==22):
                                id22 = "22 - Base extra-solar X0-3b"
                                casaNome1 = "- Base extra-solar X0-3b"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence22 == "" or pertence22 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence22 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence22 == ""):
                                                spacecoins1 -= preco
                                                pertence22 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==23):
                                id23 = "23 - Base extra-solar C0R0T-Exo-1b"
                                casaNome1 = "- Base extra-solar C0R0T-Exo-1b"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao1, casaNome1)
                                if (pertence23 == "" or pertence23 == nome1):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence23 == nome1):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence23 == ""):
                                                spacecoins1 -= preco
                                                pertence23 = nome1
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins1, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins1 -= aluguel
                                    print("Agora você possui", spacecoins1, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao1==24):
                                id24 = "24 - Imposto espacial"
                                casaNome1 = "- Imposto espacial"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao1, casaNome1)
                                print("Você pagará 150 Spacecoins")
                                spacecoins1-=150
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao1>24):
                                print("Você deu a vonta completa no universo e voltará para a posição 1")
                                print("Você receberá 200 Spacecoins")
                                spacecoins1+=200
                                posicao1 = 1
                                casaNome1 = "- Fronteira Intergalática/Portões do Universo"


        elif(i==1):
            print()
            if (entendo2 == "entendo"):
                continue;
            else:
                print(nome2, "sua vez de jogar")
                jogar = ""
                if (spacecoins2 <= 0):
                    print("Você ficou sem dinheiro, fim de jogo pra você!")
                    while (entendo2 != "entendo"):
                        print("Digite entendo para concordar que faliu")
                        entendo2 = input()
                    continue;
                else:
                    while(jogar != "encerrar"):
                        print()
                        print(nome2, ", digite:")
                        print("1 - Para saber sua posição na galáxia")
                        print("2 - Para saber quantos Spacecoins possui")
                        print("3 - Para ver seus territórios comprados")
                        print("sair - Para sair do jogo")
                        print("jogar - Para jogar os dados")
                        jogada = input()
                        if (jogada=="1"):
                            print("Posição:" ,posicao2,casaNome2)
                        elif(jogada=="2"):
                            print("Spacecoins:" ,spacecoins2)
                        elif(jogada=="sair"):
                            entendo2="entendo"
                            break;
                        elif(jogada=="3"):
                            print("Seus terrenos:")
                            if (pertence1 != nome2 and pertence2 != nome2 and pertence3 != nome2 and pertence4 != nome2 and pertence5 != nome2 and pertence6 != nome2 and pertence7 != nome2 and pertence8 != nome2 and pertence9 != nome2 and pertence10 != nome2 and pertence11 != nome2 and pertence12 != nome2 and pertence15 != nome2 and pertence16 != nome2 and pertence17 != nome2 and pertence18 != nome2 and pertence19 != nome2 and pertence20 != nome2 and pertence21 != nome2 and pertence22 != nome2 and pertence23 != nome2 and pertence24 != nome2):
                                print("Você nao possui nenhum terreno")
                            if (pertence1 == nome2):
                                print(id1)
                            if (pertence2 == nome2):
                                print(id2)
                            if (pertence3 == nome2):
                                print(id3)
                            if (pertence4 == nome2):
                                print(id4)
                            if (pertence5 == nome2):
                                print(id5)
                            if (pertence6 == nome2):
                                print(id6)
                            if (pertence7 == nome2):
                                print(id7)
                            if (pertence8 == nome2):
                                print(id8)
                            if (pertence9 == nome2):
                                print(id9)
                            if (pertence10 == nome2):
                                print(id10)
                            if (pertence11 == nome2):
                                print(id11)
                            if (pertence12 == nome2):
                                print(id12)
                            if (pertence13 == nome2):
                                print(id13)
                            if (pertence14 == nome2):
                                print(id14)
                            if (pertence15 == nome2):
                                print(id15)
                            if (pertence16 == nome2):
                                print(id16)
                            if (pertence17 == nome2):
                                print(id17)
                            if (pertence18 == nome2):
                                print(id18)
                            if (pertence19 == nome2):
                                print(id19)
                            if (pertence20 == nome2):
                                print(id20)
                            if (pertence21 == nome2):
                                print(id21)
                            if (pertence22 == nome2):
                                print(id22)
                            if (pertence23 == nome2):
                                print(id23)
                            if (pertence24 == nome2):
                                print(id24)

                        elif(jogada=="jogar" or jogada=="Jogar"):
                            if(status2=="preso"):
                                dado = 0
                            else:
                                dado = random.randint(1,6)
                            posicao2 += dado
                            if (posicao2==1):
                                id1 = "1 - Fronteira Intergalática/Portões do Universo"
                                casaNome2 = "- Fronteira Intergalática/Portões do Universo"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence1 == "" or pertence1 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence1 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence1 == ""):
                                                spacecoins2 -= preco
                                                pertence1 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==2):
                                id2 = "2 - Base Interplanetária de Vênus"
                                casaNome2 = "- Base Interplanetária de Vênus"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence2 == "" or pertence2 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence2 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence2 == ""):
                                                spacecoins2 -= preco
                                                pertence2 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==3):
                                id3 = "3 - Base Interplanetária da Terra"
                                casaNome2 = "- Base Interplanetária da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence3 == "" or pertence3 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence3 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence3 == ""):
                                                spacecoins2 -= preco
                                                pertence3 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==4):
                                id4 = "4 - Base Interplanetária de Marte"
                                casaNome2 = "- Base Interplanetária de Marte"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence4 == "" or pertence4 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence4 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence4 == ""):
                                                spacecoins2 -= preco
                                                pertence4 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==5):
                                id5 = "5 - Base Interplanetária de Júpiter"
                                casaNome2 = "- Base Interplanetária de Júpiter"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence5 == "" or pertence5 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence5 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence5 == ""):
                                                spacecoins2 -= preco
                                                pertence5 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==6):
                                id6 = "6 - Base Interplanetária de Saturno"
                                casaNome2 = "- Base Interplanetária de Saturno"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence6 == "" or pertence6 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence6 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence6 == ""):
                                                spacecoins2 -= preco
                                                pertence6 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==7):
                                id7 = "7 - Prisão Univeral/Passagem de Visitantes"
                                casaNome2 = "- Prisão Univeral/Passagem de Visitantes"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (status2 == "preso"):
                                    print("Você está preso e não pode jogar")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                    status2 = ""
                                else:
                                    if (pertence7 == "" or pertence7 == nome2):
                                        print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                        comprar = input()
                                        if (comprar == "sim"):
                                            if (preco != 0):
                                                if (pertence7 == nome2):
                                                    print("Esse território já é seu")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                                elif (pertence7 == ""):
                                                    spacecoins2 -= preco
                                                    pertence7 = nome2
                                                    print("Território adquirido")
                                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                            else:
                                                print("Este terreno não pode ser comprado")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                        spacecoins2 -= aluguel
                                        print("Agora você possui", spacecoins2, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()

                            elif(posicao2==8):
                                id8 = "8 - Base Lunar da Terra"
                                casaNome2 = "- Base Lunar da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence8 == "" or pertence8 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence8 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence8 == ""):
                                                spacecoins2 -= preco
                                                pertence8 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==9):
                                id9 = "9 - Base Lunar de Fobos"
                                casaNome2  = "- Base Lunar de Fobos"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence9 == "" or pertence9 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence9 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence9 == ""):
                                                spacecoins2 -= preco
                                                pertence9 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==10):
                                id10 = "10 - Base Lunar Europa"
                                casaNome2 = "- Base Lunar Europa"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence10 == "" or pertence10 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence10 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence10 == ""):
                                                spacecoins2 -= preco
                                                pertence10 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==11):
                                id11 = "11 - Base Lunar de Pandora"
                                casaNome2 = "- Base Lunar de Pandora"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence11 == "" or pertence11 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence11 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence11 == ""):
                                                spacecoins2 -= preco
                                                pertence11 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==12):
                                id12 = "12 - Base Lunar de Talassa"
                                casaNome2 = "- Base Lunar de Talassa"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence12 == "" or pertence12 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence12 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence12 == ""):
                                                spacecoins2 -= preco
                                                pertence12 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==13):
                                id13 = "13 - Satélite da sorte: JACKPOT"
                                casaNome2 = "- Satélite da sorte: JACKPOT"
                                preco = 0
                                aluguel = 0
                                print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                                print("Você precisa pensar em um número e lançar um dado. Se os números forem iguais você ganha 200 Spacecoins, mas se forem diferentes você perde 100 Spacecoins")
                                print("Digite um número de 1 a 6")
                                num = int(input())
                                dadoJack = random.randint(1, 6)
                                if (num == dadoJack):
                                    spacecoins2 += 200
                                    print("Parabéns você conseguiu!")
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                else:
                                    spacecoins2 -= 100
                                    print("Não foi dessa vez!")
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()

                            elif(posicao2==14):
                                id14 = "14 - Planeta anão: Plutão"
                                casaNome2 = "- Planeta anão: Plutão"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence14 == "" or pertence14 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence14 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence14 == ""):
                                                spacecoins2 -= preco
                                                pertence14 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==15):
                                id15 = "15 - Planeta anão: Éris"
                                casaNome2 = "- Planeta anão: Éris"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence15 == "" or pertence15 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence15 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence15 == ""):
                                                spacecoins2 -= preco
                                                pertence15 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==16):
                                id16 = "16 - Planeta anão: Haumea"
                                casaNome2 = "- Planeta anão: Haumea"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence16 == "" or pertence16 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence16 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence16 == ""):
                                                spacecoins2 -= preco
                                                pertence16 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==17):
                                id17 = "17 - Planeta anão: Ceres"
                                casaNome2 = "- Planeta anão: Ceres"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence17 == "" or pertence17 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence17 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence17 == ""):
                                                spacecoins2 -= preco
                                                pertence17 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==18):
                                id18 = "18 - Planeta anão: Makemake"
                                casaNome2 = "- Planeta anão: Makemake"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence18 == "" or pertence18 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence18 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence18 == ""):
                                                spacecoins2 -= preco
                                                pertence18 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==19):
                                id19 = "19 - Vá para a prisão universal!"
                                casaNome2 = "- Vá para a prisão universal!"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao2, casaNome2)
                                print("Você foi preso, será movido para casa 7(prisão) e ficará 1 rodada sem jogar")
                                posicao2 = 7
                                casaNome2 = "Prisão Univeral/Passagem de Visitantes"
                                status2 = "preso"
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao2==20):
                                id20 = "20 - Base extra-solar Gliese 581 d"
                                casaNome2 = "- Base extra-solar Gliese 581 d"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence20 == "" or pertence20 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence20 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence20 == ""):
                                                spacecoins2 -= preco
                                                pertence20 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==21):
                                id21 = "21 - Base extra-solar Upsilon Andromedae"
                                casaNome2 = "- Base extra-solar Upsilon Andromedae"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence21 == "" or pertence21 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence21 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence21 == ""):
                                                spacecoins2 -= preco
                                                pertence21 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==22):
                                id22 = "22 - Base extra-solar X0-3b"
                                casaNome2 = "- Base extra-solar X0-3b"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence22 == "" or pertence22 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence22 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence22 == ""):
                                                spacecoins2 -= preco
                                                pertence22 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==23):
                                id23 = "23 - Base extra-solar C0R0T-Exo-1b"
                                casaNome2 = "- Base extra-solar C0R0T-Exo-1b"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao2, casaNome2)
                                if (pertence23 == "" or pertence23 == nome2):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence23 == nome2):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence23 == ""):
                                                spacecoins2 -= preco
                                                pertence23 = nome2
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins2, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins2 -= aluguel
                                    print("Agora você possui", spacecoins2, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao2==24):
                                id24 = "24 - Imposto espacial"
                                casaNome2 = "- Imposto espacial"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao2, casaNome2)
                                print("Você pagará 150 Spacecoins")
                                spacecoins2 -= 150
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao2>24):
                                print("Você deu a vonta completa no universo e voltará para a posição 1")
                                print("Você receberá 200 Spacecoins")
                                spacecoins2 += 200
                                posicao2 = 1
                                casaNome2 = "- Fronteira Intergalática/Portões do Universo"

        elif(i==2):
            print()
            if (entendo3 == "entendo"):
                continue;
            else:
                print(nome3, "sua vez de jogar")
                jogar = ""
                if (spacecoins3 <= 0):
                    print("Você ficou sem dinheiro, fim de jogo pra você!")
                    while (entendo3 != "entendo"):
                        print("Digite entendo para concordar que faliu")
                        entendo3 = input()
                    continue;
                else:
                    while (jogar != "encerrar"):
                        print()
                        print(nome3, ", digite:")
                        print("1 - Para saber sua posição na galáxia")
                        print("2 - Para saber quantos Spacecoins possui")
                        print("3 - Para ver seus territórios comprados")
                        print("sair - Para sair do jogo")
                        print("jogar - Para jogar os dados")
                        jogada = input()
                        if (jogada == "1"):
                            print("Posição:", posicao3,casaNome3)
                        elif (jogada == "2"):
                            print("Spacecoins:", spacecoins3)
                        elif(jogada=="sair"):
                            entendo3="entendo"
                            break;
                        elif (jogada == "3"):
                            print("Seus terrenos:")
                            if (pertence1 != nome3 and pertence2 != nome3 and pertence3 != nome3 and pertence4 != nome3 and pertence5 != nome3 and pertence6 != nome3 and pertence7 != nome3 and pertence8 != nome3 and pertence9 != nome3 and pertence10 != nome3 and pertence11 != nome3 and pertence12 != nome3 and pertence15 != nome3 and pertence16 != nome3 and pertence17 != nome3 and pertence18 != nome3 and pertence19 != nome3 and pertence20 != nome3 and pertence21 != nome3 and pertence22 != nome3 and pertence23 != nome3 and pertence24 != nome3):
                                print("Você nao possui nenhum terreno")
                            if (pertence1 == nome3):
                                print(id1)
                            if (pertence2 == nome3):
                                print(id2)
                            if (pertence3 == nome3):
                                print(id3)
                            if (pertence4 == nome3):
                                print(id4)
                            if (pertence5 == nome3):
                                print(id5)
                            if (pertence6 == nome3):
                                print(id6)
                            if (pertence7 == nome3):
                                print(id7)
                            if (pertence8 == nome3):
                                print(id8)
                            if (pertence9 == nome3):
                                print(id9)
                            if (pertence10 == nome3):
                                print(id10)
                            if (pertence11 == nome3):
                                print(id11)
                            if (pertence12 == nome3):
                                print(id12)
                            if (pertence13 == nome3):
                                print(id13)
                            if (pertence14 == nome3):
                                print(id14)
                            if (pertence15 == nome3):
                                print(id15)
                            if (pertence16 == nome3):
                                print(id16)
                            if (pertence17 == nome3):
                                print(id17)
                            if (pertence18 == nome3):
                                print(id18)
                            if (pertence19 == nome3):
                                print(id19)
                            if (pertence20 == nome3):
                                print(id20)
                            if (pertence21 == nome3):
                                print(id21)
                            if (pertence22 == nome3):
                                print(id22)
                            if (pertence23 == nome3):
                                print(id23)
                            if (pertence24 == nome3):
                                print(id24)

                        elif (jogada == "jogar" or jogada == "Jogar"):
                            if(status3=="preso"):
                                dado = 0
                            else:
                                dado = random.randint(1, 6)
                            posicao3 += dado
                            if (posicao3==1):
                                id1 = "1 - Fronteira Intergalática/Portões do Universo"
                                casaNome3 = "- Fronteira Intergalática/Portões do Universo"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence1 == "" or pertence1 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence1 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence1 == ""):
                                                spacecoins3 -= preco
                                                pertence1 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==2):
                                id2 = "2 - Base Interplanetária de Vênus"
                                casaNome3 = "- Base Interplanetária de Vênus"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence2 == "" or pertence2 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence2 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence2 == ""):
                                                spacecoins3 -= preco
                                                pertence2 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==3):
                                id3 = "3 - Base Interplanetária da Terra"
                                casaNome3 = "- Base Interplanetária da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence3 == "" or pertence3 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence3 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence3 == ""):
                                                spacecoins3 -= preco
                                                pertence3 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==4):
                                id4 = "4 - Base Interplanetária de Marte"
                                casaNome3 = "- Base Interplanetária de Marte"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence4 == "" or pertence4 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence4 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence4 == ""):
                                                spacecoins3 -= preco
                                                pertence4 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==5):
                                id5 = "5 - Base Interplanetária de Júpiter"
                                casaNome3 = "- Base Interplanetária de Júpiter"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence5 == "" or pertence5 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence5 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence5 == ""):
                                                spacecoins3 -= preco
                                                pertence5 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==6):
                                id6 = "6 - Base Interplanetária de Saturno"
                                casaNome3 = "- Base Interplanetária de Saturno"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence6 == "" or pertence6 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence6 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence6 == ""):
                                                spacecoins3 -= preco
                                                pertence6 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==7):
                                id7 = "7 - Prisão Univeral/Passagem de Visitantes"
                                casaNome3 = "- Prisão Univeral/Passagem de Visitantes"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (status3 == "preso"):
                                    print("Você está preso e não pode jogar")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                    status3 = ""
                                else:
                                    if (pertence7 == "" or pertence7 == nome3):
                                        print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                        comprar = input()
                                        if (comprar == "sim"):
                                            if (preco != 0):
                                                if (pertence7 == nome3):
                                                    print("Esse território já é seu")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                                elif (pertence7 == ""):
                                                    spacecoins3 -= preco
                                                    pertence7 = nome3
                                                    print("Território adquirido")
                                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                            else:
                                                print("Este terreno não pode ser comprado")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                        spacecoins3 -= aluguel
                                        print("Agora você possui", spacecoins3, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()

                            elif(posicao3==8):
                                id8 = "8 - Base Lunar da Terra"
                                casaNome3 = "- Base Lunar da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence8 == "" or pertence8 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence8 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence8 == ""):
                                                spacecoins3 -= preco
                                                pertence8 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==9):
                                id9 = "9 - Base Lunar de Fobos"
                                casaNome3  = "- Base Lunar de Fobos"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence9 == "" or pertence9 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence9 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence9 == ""):
                                                spacecoins3 -= preco
                                                pertence9 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==10):
                                id10 = "10 - Base Lunar Europa"
                                casaNome3 = "- Base Lunar Europa"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence10 == "" or pertence10 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence10 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence10 == ""):
                                                spacecoins3 -= preco
                                                pertence10 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==11):
                                id11 = "11 - Base Lunar de Pandora"
                                casaNome3 = "- Base Lunar de Pandora"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence11 == "" or pertence11 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence11 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence11 == ""):
                                                spacecoins3 -= preco
                                                pertence11 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==12):
                                id12 = "12 - Base Lunar de Talassa"
                                casaNome3 = "- Base Lunar de Talassa"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence12 == "" or pertence12 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence12 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence12 == ""):
                                                spacecoins3 -= preco
                                                pertence12 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==13):
                                id13 = "13 - Satélite da sorte: JACKPOT"
                                casaNome3 = "- Satélite da sorte: JACKPOT"
                                preco = 0
                                aluguel = 0
                                print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                                print("Você precisa pensar em um número e lançar um dado. Se os números forem iguais você ganha 200 Spacecoins, mas se forem diferentes você perde 100 Spacecoins")
                                print("Digite um número de 1 a 6")
                                num = int(input())
                                dadoJack = random.randint(1, 6)
                                if (num == dadoJack):
                                    spacecoins3 += 200
                                    print("Parabéns você conseguiu!")
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                else:
                                    spacecoins3 -= 100
                                    print("Não foi dessa vez!")
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()

                            elif(posicao3==14):
                                id14 = "14 - Planeta anão: Plutão"
                                casaNome3 = "- Planeta anão: Plutão"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence14 == "" or pertence14 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence14 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence14 == ""):
                                                spacecoins3 -= preco
                                                pertence14 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==15):
                                id15 = "15 - Planeta anão: Éris"
                                casaNome3 = "- Planeta anão: Éris"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence15 == "" or pertence15 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence15 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence15 == ""):
                                                spacecoins3 -= preco
                                                pertence15 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==16):
                                id16 = "16 - Planeta anão: Haumea"
                                casaNome3 = "- Planeta anão: Haumea"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence16 == "" or pertence16 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence16 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence16 == ""):
                                                spacecoins3 -= preco
                                                pertence16 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==17):
                                id17 = "17 - Planeta anão: Ceres"
                                casaNome3 = "- Planeta anão: Ceres"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence17 == "" or pertence17 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence17 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence17 == ""):
                                                spacecoins3 -= preco
                                                pertence17 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==18):
                                id18 = "18 - Planeta anão: Makemake"
                                casaNome3 = "- Planeta anão: Makemake"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence18 == "" or pertence18 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence18 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence18 == ""):
                                                spacecoins3 -= preco
                                                pertence18 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==19):
                                id19 = "19 - Vá para a prisão universal!"
                                casaNome3 = "- Vá para a prisão universal!"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao3, casaNome3)
                                print("Você foi preso, será movido para casa 7(prisão) e ficará 1 rodada sem jogar")
                                posicao3 = 7
                                casaNome3 = "Prisão Univeral/Passagem de Visitantes"
                                status3 = "preso"
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao3==20):
                                id20 = "20 - Base extra-solar Gliese 581 d"
                                casaNome3 = "- Base extra-solar Gliese 581 d"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence20 == "" or pertence20 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence20 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence20 == ""):
                                                spacecoins3 -= preco
                                                pertence20 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==21):
                                id21 = "21 - Base extra-solar Upsilon Andromedae"
                                casaNome3 = "- Base extra-solar Upsilon Andromedae"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence21 == "" or pertence21 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence21 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence21 == ""):
                                                spacecoins3 -= preco
                                                pertence21 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==22):
                                id22 = "22 - Base extra-solar X0-3b"
                                casaNome3 = "- Base extra-solar X0-3b"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence22 == "" or pertence22 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence22 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence22 == ""):
                                                spacecoins3 -= preco
                                                pertence22 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==23):
                                id23 = "23 - Base extra-solar C0R0T-Exo-1b"
                                casaNome3 = "- Base extra-solar C0R0T-Exo-1b"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao3, casaNome3)
                                if (pertence23 == "" or pertence23 == nome3):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence23 == nome3):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence23 == ""):
                                                spacecoins3 -= preco
                                                pertence23 = nome3
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins3, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins3 -= aluguel
                                    print("Agora você possui", spacecoins3, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao3==24):
                                id24 = "24 - Imposto espacial"
                                casaNome3 = "- Imposto espacial"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao3, casaNome3)
                                print("Você pagará 150 Spacecoins")
                                spacecoins3 -= 150
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao3>24):
                                print("Você deu a vonta completa no universo e voltará para a posição 1")
                                print("Você receberá 200 Spacecoins")
                                spacecoins3 += 200
                                posicao3 = 1
                                casaNome3 = "- Fronteira Intergalática/Portões do Universo"

        elif(i==3):
            print()
            if (entendo4 == "entendo"):
                continue;
            else:
                print(nome4, "sua vez de jogar")
                jogar = ""
                if (spacecoins4 <= 0):
                    print("Você ficou sem dinheiro, fim de jogo pra você!")
                    while (entendo4 != "entendo"):
                        print("Digite entendo para concordar que faliu")
                        entendo4 = input()
                    continue;
                else:
                    while (jogar != "encerrar"):
                        print()
                        print(nome4, ", digite:")
                        print("1 - Para saber sua posição na galáxia")
                        print("2 - Para saber quantos Spacecoins possui")
                        print("3 - Para ver seus territórios comprados")
                        print("sair - Para sair do jogo")
                        print("jogar - Para jogar os dados")
                        jogada = input()
                        if (jogada == "1"):
                            print("Posição:", posicao4, casaNome4)
                        elif (jogada == "2"):
                            print("Spacecoins:", spacecoins4)
                        elif(jogada=="sair"):
                            entendo4="entendo"
                            break;
                        elif (jogada == "3"):
                            print("Seus terrenos:")
                            if (pertence1 != nome4 and pertence2 != nome4 and pertence3 != nome4 and pertence4 != nome4 and pertence5 != nome4 and pertence6 != nome4 and pertence7 != nome4 and pertence8 != nome4 and pertence9 != nome4 and pertence10 != nome4 and pertence11 != nome4 and pertence12 != nome4 and pertence15 != nome4 and pertence16 != nome4 and pertence17 != nome4 and pertence18 != nome4 and pertence19 != nome4 and pertence20 != nome4 and pertence21 != nome4 and pertence22 != nome4 and pertence23 != nome4 and pertence24 != nome4):
                                print("Você nao possui nenhum terreno")
                            if (pertence1 == nome4):
                                print(id1)
                            if (pertence2 == nome4):
                                print(id2)
                            if (pertence3 == nome4):
                                print(id3)
                            if (pertence4 == nome4):
                                print(id4)
                            if (pertence5 == nome4):
                                print(id5)
                            if (pertence6 == nome4):
                                print(id6)
                            if (pertence7 == nome4):
                                print(id7)
                            if (pertence8 == nome4):
                                print(id8)
                            if (pertence9 == nome4):
                                print(id9)
                            if (pertence10 == nome4):
                                print(id10)
                            if (pertence11 == nome4):
                                print(id11)
                            if (pertence12 == nome4):
                                print(id12)
                            if (pertence13 == nome4):
                                print(id13)
                            if (pertence14 == nome4):
                                print(id14)
                            if (pertence15 == nome4):
                                print(id15)
                            if (pertence16 == nome4):
                                print(id16)
                            if (pertence17 == nome4):
                                print(id17)
                            if (pertence18 == nome4):
                                print(id18)
                            if (pertence19 == nome4):
                                print(id19)
                            if (pertence20 == nome4):
                                print(id20)
                            if (pertence21 == nome4):
                                print(id21)
                            if (pertence22 == nome4):
                                print(id22)
                            if (pertence23 == nome4):
                                print(id23)
                            if (pertence24 == nome4):
                                print(id24)

                        elif (jogada == "jogar" or jogada == "Jogar"):
                            if(status3=="preso"):
                                dado = 0
                            else:
                                dado = random.randint(1, 6)
                            posicao4 += dado
                            if (posicao4==1):
                                id1 = "1 - Fronteira Intergalática/Portões do Universo"
                                casaNome4 = "- Fronteira Intergalática/Portões do Universo"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence1 == "" or pertence1 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence1 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence1 == ""):
                                                spacecoins4 -= preco
                                                pertence1 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==2):
                                id2 = "2 - Base Interplanetária de Vênus"
                                casaNome4 = "- Base Interplanetária de Vênus"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence2 == "" or pertence2 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence2 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence2 == ""):
                                                spacecoins4 -= preco
                                                pertence2 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==3):
                                id3 = "3 - Base Interplanetária da Terra"
                                casaNome4 = "- Base Interplanetária da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence3 == "" or pertence3 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence3 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence3 == ""):
                                                spacecoins4 -= preco
                                                pertence3 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==4):
                                id4 = "4 - Base Interplanetária de Marte"
                                casaNome4 = "- Base Interplanetária de Marte"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence4 == "" or pertence4 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence4 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence4 == ""):
                                                spacecoins4 -= preco
                                                pertence4 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==5):
                                id5 = "5 - Base Interplanetária de Júpiter"
                                casaNome4 = "- Base Interplanetária de Júpiter"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence5 == "" or pertence5 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence5 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence5 == ""):
                                                spacecoins4 -= preco
                                                pertence5 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==6):
                                id6 = "6 - Base Interplanetária de Saturno"
                                casaNome4 = "- Base Interplanetária de Saturno"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence6 == "" or pertence6 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence6 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence6 == ""):
                                                spacecoins4 -= preco
                                                pertence6 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==7):
                                id7 = "7 - Prisão Univeral/Passagem de Visitantes"
                                casaNome4 = "- Prisão Univeral/Passagem de Visitantes"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (status4 == "preso"):
                                    print("Você está preso e não pode jogar")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                    status4 = ""
                                else:
                                    if (pertence7 == "" or pertence7 == nome4):
                                        print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                        comprar = input()
                                        if (comprar == "sim"):
                                            if (preco != 0):
                                                if (pertence7 == nome4):
                                                    print("Esse território já é seu")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                                elif (pertence7 == ""):
                                                    spacecoins4 -= preco
                                                    pertence7 = nome4
                                                    print("Território adquirido")
                                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                            else:
                                                print("Este terreno não pode ser comprado")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                        spacecoins4 -= aluguel
                                        print("Agora você possui", spacecoins4, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()

                            elif(posicao4==8):
                                id8 = "8 - Base Lunar da Terra"
                                casaNome4 = "- Base Lunar da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence8 == "" or pertence8 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence8 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence8 == ""):
                                                spacecoins4 -= preco
                                                pertence8 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==9):
                                id9 = "9 - Base Lunar de Fobos"
                                casaNome4  = "- Base Lunar de Fobos"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence9 == "" or pertence9 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence9 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence9 == ""):
                                                spacecoins4 -= preco
                                                pertence9 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==10):
                                id10 = "10 - Base Lunar Europa"
                                casaNome4 = "- Base Lunar Europa"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence10 == "" or pertence10 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence10 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence10 == ""):
                                                spacecoins4 -= preco
                                                pertence10 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==11):
                                id11 = "11 - Base Lunar de Pandora"
                                casaNome4 = "- Base Lunar de Pandora"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence11 == "" or pertence11 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence11 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence11 == ""):
                                                spacecoins4 -= preco
                                                pertence11 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==12):
                                id12 = "12 - Base Lunar de Talassa"
                                casaNome4 = "- Base Lunar de Talassa"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence12 == "" or pertence12 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence12 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence12 == ""):
                                                spacecoins4 -= preco
                                                pertence12 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==13):
                                id13 = "13 - Satélite da sorte: JACKPOT"
                                casaNome4 = "- Satélite da sorte: JACKPOT"
                                preco = 0
                                aluguel = 0
                                print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                                print("Você precisa pensar em um número e lançar um dado. Se os números forem iguais você ganha 200 Spacecoins, mas se forem diferentes você perde 100 Spacecoins")
                                print("Digite um número de 1 a 6")
                                num = int(input())
                                dadoJack = random.randint(1, 6)
                                if (num == dadoJack):
                                    spacecoins4 += 200
                                    print("Parabéns você conseguiu!")
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                else:
                                    spacecoins4 -= 100
                                    print("Não foi dessa vez!")
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()

                            elif(posicao4==14):
                                id14 = "14 - Planeta anão: Plutão"
                                casaNome4 = "- Planeta anão: Plutão"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence14 == "" or pertence14 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence14 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence14 == ""):
                                                spacecoins4 -= preco
                                                pertence14 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==15):
                                id15 = "15 - Planeta anão: Éris"
                                casaNome4 = "- Planeta anão: Éris"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence15 == "" or pertence15 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence15 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence15 == ""):
                                                spacecoins4 -= preco
                                                pertence15 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==16):
                                id16 = "16 - Planeta anão: Haumea"
                                casaNome4 = "- Planeta anão: Haumea"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence16 == "" or pertence16 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence16 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence16 == ""):
                                                spacecoins4 -= preco
                                                pertence16 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==17):
                                id17 = "17 - Planeta anão: Ceres"
                                casaNome4 = "- Planeta anão: Ceres"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence17 == "" or pertence17 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence17 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence17 == ""):
                                                spacecoins4 -= preco
                                                pertence17 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==18):
                                id18 = "18 - Planeta anão: Makemake"
                                casaNome4 = "- Planeta anão: Makemake"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence18 == "" or pertence18 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence18 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence18 == ""):
                                                spacecoins4 -= preco
                                                pertence18 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==19):
                                id19 = "19 - Vá para a prisão universal!"
                                casaNome4 = "- Vá para a prisão universal!"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao4, casaNome4)
                                print("Você foi preso, será movido para casa 7(prisão) e ficará 1 rodada sem jogar")
                                posicao4 = 7
                                casaNome4 = "Prisão Univeral/Passagem de Visitantes"
                                status4 = "preso"
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao4==20):
                                id20 = "20 - Base extra-solar Gliese 581 d"
                                casaNome4 = "- Base extra-solar Gliese 581 d"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence20 == "" or pertence20 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence20 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence20 == ""):
                                                spacecoins4 -= preco
                                                pertence20 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==21):
                                id21 = "21 - Base extra-solar Upsilon Andromedae"
                                casaNome4 = "- Base extra-solar Upsilon Andromedae"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence21 == "" or pertence21 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence21 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence21 == ""):
                                                spacecoins4 -= preco
                                                pertence21 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==22):
                                id22 = "22 - Base extra-solar X0-3b"
                                casaNome4 = "- Base extra-solar X0-3b"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence22 == "" or pertence22 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence22 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence22 == ""):
                                                spacecoins4 -= preco
                                                pertence22 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==23):
                                id23 = "23 - Base extra-solar C0R0T-Exo-1b"
                                casaNome4 = "- Base extra-solar C0R0T-Exo-1b"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao4, casaNome4)
                                if (pertence23 == "" or pertence23 == nome4):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence23 == nome4):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence23 == ""):
                                                spacecoins4 -= preco
                                                pertence23 = nome4
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins4, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins4 -= aluguel
                                    print("Agora você possui", spacecoins4, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao4==24):
                                id24 = "24 - Imposto espacial"
                                casaNome4 = "- Imposto espacial"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao4, casaNome4)
                                print("Você pagará 150 Spacecoins")
                                spacecoins4 -= 150
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao4>24):
                                print("Você deu a vonta completa no universo e voltará para a posição 1")
                                print("Você receberá 200 Spacecoins")
                                spacecoins4 += 200
                                posicao4 = 1
                                casaNome4 = "- Fronteira Intergalática/Portões do Universo"

        elif(i==4):
            print()
            if (entendo5 == "entendo"):
                continue;
            else:
                print(nome5, "sua vez de jogar")
                jogar = ""
                if (spacecoins5 <= 0):
                    print("Você ficou sem dinheiro, fim de jogo pra você!")
                    while (entendo5 != "entendo"):
                        print("Digite entendo para concordar que faliu")
                        entendo5 = input()
                    continue;
                else:
                    while (jogar != "encerrar"):
                        print()
                        print(nome5, ", digite:")
                        print("1 - Para saber sua posição na galáxia")
                        print("2 - Para saber quantos Spacecoins possui")
                        print("3 - Para ver seus territórios comprados")
                        print("jogar - Para jogar os dados")
                        jogada = input()
                        if (jogada == "1"):
                            print("Posição:", posicao5, casaNome5)
                        elif (jogada == "2"):
                            print("Spacecoins:", spacecoins5)
                        elif(jogada=="sair"):
                            entendo5="entendo"
                            break;
                        elif (jogada == "3"):
                            print("Seus terrenos:")
                            if (pertence1 != nome5 and pertence2 != nome5 and pertence3 != nome5 and pertence4 != nome5 and pertence5 != nome5 and pertence6 != nome5 and pertence7 != nome5 and pertence8 != nome5 and pertence9 != nome5 and pertence10 != nome5 and pertence11 != nome5 and pertence12 != nome5 and pertence15 != nome5 and pertence16 != nome5 and pertence17 != nome5 and pertence18 != nome5 and pertence19 != nome5 and pertence20 != nome5 and pertence21 != nome5 and pertence22 != nome5 and pertence23 != nome5 and pertence24 != nome5):
                                print("Você nao possui nenhum terreno")
                            if (pertence1 == nome5):
                                print(id1)
                            if (pertence2 == nome5):
                                print(id2)
                            if (pertence3 == nome5):
                                print(id3)
                            if (pertence4 == nome5):
                                print(id4)
                            if (pertence5 == nome5):
                                print(id5)
                            if (pertence6 == nome5):
                                print(id6)
                            if (pertence7 == nome5):
                                print(id7)
                            if (pertence8 == nome5):
                                print(id8)
                            if (pertence9 == nome5):
                                print(id9)
                            if (pertence10 == nome5):
                                print(id10)
                            if (pertence11 == nome5):
                                print(id11)
                            if (pertence12 == nome5):
                                print(id12)
                            if (pertence13 == nome5):
                                print(id13)
                            if (pertence14 == nome5):
                                print(id14)
                            if (pertence15 == nome5):
                                print(id15)
                            if (pertence16 == nome5):
                                print(id16)
                            if (pertence17 == nome5):
                                print(id17)
                            if (pertence18 == nome5):
                                print(id18)
                            if (pertence19 == nome5):
                                print(id19)
                            if (pertence20 == nome5):
                                print(id20)
                            if (pertence21 == nome5):
                                print(id21)
                            if (pertence22 == nome5):
                                print(id22)
                            if (pertence23 == nome5):
                                print(id23)
                            if (pertence24 == nome5):
                                print(id24)

                        elif (jogada == "jogar" or jogada == "Jogar"):
                            if(status5=="preso"):
                                dado = 0
                            else:
                                dado = random.randint(1,6)
                            posicao5 += dado
                            if (posicao5==1):
                                id1 = "1 - Fronteira Intergalática/Portões do Universo"
                                casaNome5 = "- Fronteira Intergalática/Portões do Universo"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence1 == "" or pertence1 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence1 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence1 == ""):
                                                spacecoins5 -= preco
                                                pertence1 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==2):
                                id2 = "2 - Base Interplanetária de Vênus"
                                casaNome5 = "- Base Interplanetária de Vênus"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence2 == "" or pertence2 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence2 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence2 == ""):
                                                spacecoins5 -= preco
                                                pertence2 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==3):
                                id3 = "3 - Base Interplanetária da Terra"
                                casaNome5 = "- Base Interplanetária da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence3 == "" or pertence3 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence3 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence3 == ""):
                                                spacecoins5 -= preco
                                                pertence3 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif (posicao5==4):
                                id4 = "4 - Base Interplanetária de Marte"
                                casaNome5 = "- Base Interplanetária de Marte"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence4 == "" or pertence4 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence4 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence4 == ""):
                                                spacecoins5 -= preco
                                                pertence4 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==5):
                                id5 = "5 - Base Interplanetária de Júpiter"
                                casaNome5 = "- Base Interplanetária de Júpiter"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence5 == "" or pertence5 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence5 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence5 == ""):
                                                spacecoins5 -= preco
                                                pertence5 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==6):
                                id6 = "6 - Base Interplanetária de Saturno"
                                casaNome5 = "- Base Interplanetária de Saturno"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence6 == "" or pertence6 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence6 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence6 == ""):
                                                spacecoins5 -= preco
                                                pertence6 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==7):
                                id7 = "7 - Prisão Univeral/Passagem de Visitantes"
                                casaNome5 = "- Prisão Univeral/Passagem de Visitantes"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (status5 == "preso"):
                                    print("Você está preso e não pode jogar")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                    status5 = ""
                                else:
                                    if (pertence7 == "" or pertence7 == nome5):
                                        print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                        comprar = input()
                                        if (comprar == "sim"):
                                            if (preco != 0):
                                                if (pertence7 == nome5):
                                                    print("Esse território já é seu")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                                elif (pertence7 == ""):
                                                    spacecoins5 -= preco
                                                    pertence7 = nome5
                                                    print("Território adquirido")
                                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                                    while (jogar != "encerrar"):
                                                        print("Digite encerrar para encerrar sua jogada")
                                                        jogar = input()
                                            else:
                                                print("Este terreno não pode ser comprado")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                        spacecoins5 -= aluguel
                                        print("Agora você possui", spacecoins5, "Spacecoins")
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()


                            elif(posicao5==8):
                                id8 = "8 - Base Lunar da Terra"
                                casaNome5 = "- Base Lunar da Terra"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence8 == "" or pertence8 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence8 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence8 == ""):
                                                spacecoins5 -= preco
                                                pertence8 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==9):
                                id9 = "9 - Base Lunar de Fobos"
                                casaNome5  = "- Base Lunar de Fobos"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence9 == "" or pertence9 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence9 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence9 == ""):
                                                spacecoins5 -= preco
                                                pertence9 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==10):
                                id10 = "10 - Base Lunar Europa"
                                casaNome5 = "- Base Lunar Europa"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence10 == "" or pertence10 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence10 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence10 == ""):
                                                spacecoins5 -= preco
                                                pertence10 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==11):
                                id11 = "11 - Base Lunar de Pandora"
                                casaNome5 = "- Base Lunar de Pandora"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence11 == "" or pertence11 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence11 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence11 == ""):
                                                spacecoins5 -= preco
                                                pertence11 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==12):
                                id12 = "12 - Base Lunar de Talassa"
                                casaNome5 = "- Base Lunar de Talassa"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence12 == "" or pertence12 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence12 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence12 == ""):
                                                spacecoins5 -= preco
                                                pertence12 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==13):
                                id13 = "13 - Satélite da sorte: JACKPOT"
                                casaNome5 = "- Satélite da sorte: JACKPOT"
                                preco = 0
                                aluguel = 0
                                print("Você encontrou o satélite perdido! Ele pode te trazer muitas sortes ou dívidas!")
                                print("Você precisa pensar em um número e lançar um dado. Se os números forem iguais você ganha 200 Spacecoins, mas se forem diferentes você perde 100 Spacecoins")
                                print("Digite um número de 1 a 6")
                                num = int(input())
                                dadoJack = random.randint(1, 6)
                                if (num == dadoJack):
                                    spacecoins5 += 200
                                    print("Parabéns você conseguiu!")
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                                else:
                                    spacecoins5 -= 100
                                    print("Não foi dessa vez!")
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()

                            elif(posicao5==14):
                                id14 = "14 - Planeta anão: Plutão"
                                casaNome5 = "- Planeta anão: Plutão"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence14 == "" or pertence14 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence14 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence14 == ""):
                                                spacecoins5 -= preco
                                                pertence14 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==15):
                                id15 = "15 - Planeta anão: Éris"
                                casaNome5 = "- Planeta anão: Éris"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence15 == "" or pertence15 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence15 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence15 == ""):
                                                spacecoins5 -= preco
                                                pertence15 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==16):
                                id16 = "16 - Planeta anão: Haumea"
                                casaNome5 = "- Planeta anão: Haumea"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence16 == "" or pertence16 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence16 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence16 == ""):
                                                spacecoins5 -= preco
                                                pertence16 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==17):
                                id17 = "17 - Planeta anão: Ceres"
                                casaNome5 = "- Planeta anão: Ceres"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence17 == "" or pertence17 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence17 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence17 == ""):
                                                spacecoins5 -= preco
                                                pertence17 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==18):
                                id18 = "18 - Planeta anão: Makemake"
                                casaNome5 = "- Planeta anão: Makemake"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence18 == "" or pertence18 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence18 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence18 == ""):
                                                spacecoins5 -= preco
                                                pertence18 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==19):
                                id19 = "19 - Vá para a prisão universal!"
                                casaNome5 = "- Vá para a prisão universal!"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao5, casaNome5)
                                print("Você foi preso, será movido para casa 7(prisão) e ficará 1 rodada sem jogar")
                                posicao5 = 7
                                casaNome5 = "Prisão Univeral/Passagem de Visitantes"
                                status5 = "preso"
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao5==20):
                                id20 = "20 - Base extra-solar Gliese 581 d"
                                casaNome5 = "- Base extra-solar Gliese 581 d"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence20 == "" or pertence20 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence20 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence20 == ""):
                                                spacecoins5 -= preco
                                                pertence20 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==21):
                                id21 = "21 - Base extra-solar Upsilon Andromedae"
                                casaNome5 = "- Base extra-solar Upsilon Andromedae"
                                preco = 450
                                aluguel = 45
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence21 == "" or pertence21 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence21 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence21 == ""):
                                                spacecoins5 -= preco
                                                pertence21 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==22):
                                id22 = "22 - Base extra-solar X0-3b"
                                casaNome5 = "- Base extra-solar X0-3b"
                                preco = 600
                                aluguel = 60
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence22 == "" or pertence22 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence22 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence22 == ""):
                                                spacecoins5 -= preco
                                                pertence22 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==23):
                                id23 = "23 - Base extra-solar C0R0T-Exo-1b"
                                casaNome5 = "- Base extra-solar C0R0T-Exo-1b"
                                preco = 250
                                aluguel = 25
                                print("Você caiu na posição:", posicao5, casaNome5)
                                if (pertence23 == "" or pertence23 == nome5):
                                    print("Você deseja comprar este território por", preco, "Spacecoins (sim/nao)?")
                                    comprar = input()
                                    if (comprar == "sim"):
                                        if (preco != 0):
                                            if (pertence23 == nome5):
                                                print("Esse território já é seu")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                            elif (pertence23 == ""):
                                                spacecoins5 -= preco
                                                pertence23 = nome5
                                                print("Território adquirido")
                                                print("Agora você possui", spacecoins5, "Spacecoins")
                                                while (jogar != "encerrar"):
                                                    print("Digite encerrar para encerrar sua jogada")
                                                    jogar = input()
                                        else:
                                            print("Este terreno não pode ser comprado")
                                            while (jogar != "encerrar"):
                                                print("Digite encerrar para encerrar sua jogada")
                                                jogar = input()
                                    else:
                                        while (jogar != "encerrar"):
                                            print("Digite encerrar para encerrar sua jogada")
                                            jogar = input()
                                else:
                                    print("Esse território já tem dono, o aluguel é", aluguel, "Spacecoins")
                                    spacecoins5 -= aluguel
                                    print("Agora você possui", spacecoins5, "Spacecoins")
                                    while (jogar != "encerrar"):
                                        print("Digite encerrar para encerrar sua jogada")
                                        jogar = input()
                            elif(posicao5==24):
                                id24 = "24 - Imposto espacial"
                                casaNome5 = "- Imposto espacial"
                                preco = 0
                                aluguel = 0
                                print("Você caiu na posição:", posicao5, casaNome5)
                                print("Você pagará 150 Spacecoins")
                                spacecoins5 -= 150
                                while (jogar != "encerrar"):
                                    print("Digite encerrar para encerrar sua jogada")
                                    jogar = input()

                            elif(posicao5>24):
                                print("Você deu a vonta completa no universo e voltará para a posição 1")
                                print("Você receberá 200 Spacecoins")
                                spacecoins5 += 200
                                posicao5 = 1
                                casaNome5 = "- Fronteira Intergalática/Portões do Universo"
    if (numJogadores == 2):
        if (entendo1 == "entendo" and entendo2 == "entendo"):
            print("Fim de jogo")
            break;
    elif (numJogadores == 3):
        if (entendo1 == "entendo" and entendo2 == "entendo" and entendo3 == "entendo"):
            print("Fim de jogo")
            break;
    elif (numJogadores == 4):
        if (entendo1 == "entendo" and entendo2 == "entendo" and entendo3 == "entendo" and entendo4 == "entendo"):
            print("Fim de jogo")
            break;
    elif (numJogadores == 5):
        if (
                            entendo1 == "entendo" and entendo2 == "entendo" and entendo3 == "entendo" and entendo4 == "entendo" and entendo5 == "entendo"):
            print("Fim de jogo")
            break;
