#############################################################

import random

matriz = []
sensePoco = []
senseOuro = []
senseWumpus = []
memoria = []
coluna = None
linha = None

class gerarMatriz(object):

    linha = None
    coluna = None


    def gerar(self, y, x):

        global coluna
        global linha

        linha = y
        coluna = x

        self.linha = linha
        self.coluna = coluna

        #gera matriz principal
        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            matriz.append(LINHA)

        #gera matriz com sensacao poco
        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            sensePoco.append(LINHA)

        #gera matriz com sensacao ouro
        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            senseOuro.append(LINHA)

        #gera matriz com sensacao wumpus
        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            senseWumpus.append(LINHA)

        #gera matriz de memoria
        for i in range(linha):
            LINHA = []
            for j in range(coluna):
                LINHA.append(' ')
            memoria.append(LINHA)

    def plot(self):
        print('\n#################\nPlot')
        for i in range(self.coluna):
            print("\n")
            for j in range(self.linha):
                print(matriz[j])
            break

    def plotPoco(self):
        print('\n#################\nsensePoco')
        for i in range(self.coluna):
            print("\n")
            for j in range(self.linha):
                print(sensePoco[j])
            break

    def plotOuro(self):
        print('\n#################\nsenseOuro')
        for i in range(self.coluna):
            print("\n")
            for j in range(self.linha):
                print(senseOuro[j])
            break

    def plotWumpus(self):
        print('\n#################\nsenseWumpus')
        for i in range(self.coluna):
            print("\n")
            for j in range(self.linha):
                print(senseWumpus[j])
            break

    def plotMemoria(self):
        print('\n#################\nmemoria')
        for i in range(self.coluna):
            print("\n")
            for j in range(self.linha):
                print(memoria[j])
            break

    def pocos(self):
        for i in range(self.coluna-1):
            while True:

                temp1 = random.randint(0, self.linha-1)
                temp2 = random.randint(0, self.coluna-1)
                if temp1 != 0 and temp2 != 0:

                    if matriz[temp1][temp2] != 'P':
                        matriz[temp1][temp2] = 'P'

                        break
        #print(self.pocos)

    def ouro(self):
        while True:

            temp1 = random.randint(0, self.linha - 1)
            temp2 = random.randint(0, self.coluna - 1)
            if temp1 != 0 and temp2 != 0:

                if matriz[temp1][temp2] != 'P':
                    matriz[temp1][temp2] = 'O'
                    break

    def wumpus(self):
        while True:

            temp1 = random.randint(0, self.linha - 1)
            temp2 = random.randint(0, self.coluna - 1)
            if temp1 != 0 and temp2 != 0:

                if matriz[temp1][temp2] != 'P' and matriz[temp1][temp2] != 'O':
                    matriz[temp1][temp2] = 'W'
                    break

    def sense_Poco(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == 'P':
                    if i - 1 > self.linha-1:
                        pass
                    else:
                        sensePoco[i - 1][j] = 'b'
                    if i + 1 > self.linha-1:
                        pass
                    else:
                        sensePoco[i + 1][j] = 'b'
                    if j - 1 > self.linha - 1:
                        pass
                    else:
                        sensePoco[i][j - 1] = 'b'
                    if j + 1 > self.linha - 1:
                        pass
                    else:
                        sensePoco[i][j + 1] = 'b'

    def sense_Ouro(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == 'O':
                    senseOuro[i][j] = 'B'


    def sense_Wumpus(self):
        for i in range(self.coluna):
            for j in range(self.linha):
                senseWumpus[i][j] = ' '
        for i in range(self.coluna):
            for j in range(self.linha):
                if matriz[i][j] == 'W':
                    if i - 1 > self.linha-1:
                        pass
                    else:
                        senseWumpus[i - 1][j] = 'F'
                    if i + 1 > self.linha-1:
                        pass
                    else:
                        senseWumpus[i + 1][j] = 'F'
                    if j - 1 > self.linha - 1:
                        pass
                    else:
                        senseWumpus[i][j - 1] = 'F'
                    if j + 1 > self.linha - 1:
                        pass
                    else:
                        senseWumpus[i][j + 1] = 'F'

    def setAgente(self):
        matriz[0][0] = 'A'


class doppleganger(object):
    flecha = True
    ouro = False
    wumpus = True
    agente = 'A'
    estado_anterior_linha = None
    estado_anterior_coluna = None

    def mover(self):
        doppleganger.ganhar(doppleganger)
        variavel = 0

        ##cantos
        if matriz[0][0] == self.agente or matriz[linha-1][0] == self.agente or matriz[0][coluna-1] == self.agente or matriz[linha-1][coluna-1] == self.agente:
            if matriz[0][0] == self.agente:
                print('CANTO1')
                doppleganger.moverSe(doppleganger, 0, 0, 'CANTO1')
            if matriz[linha-1][0] == self.agente:
                print('CANTO2')
                doppleganger.moverSe(doppleganger, linha-1, 0, 'CANTO2')
            if matriz[0][coluna-1] == self.agente:
                print('CANTO3')
                doppleganger.moverSe(doppleganger, 0, coluna-1, 'CANTO3')
            if matriz[linha-1][coluna-1] == self.agente:
                print('CANTO4')
                doppleganger.moverSe(doppleganger, linha-1, coluna - 1, 'CANTO4')
        else:
            variavel = 1

        ##paredes
        if variavel == 1:
            #parede superior X
            for i in range(coluna-1):
                if matriz[0][i+1] == self.agente:
                    print(0)
                    print(i + 1)
                    print('SUPERIOR')
                    doppleganger.moverSe(doppleganger, 0, i+1, 'SUPERIOR')
                    variavel = 2
                    break
            #parede inferior X
            if variavel != 2:
                for i in range(coluna-1):
                    if matriz[linha-1][i+1] == self.agente:
                        print(linha-1)
                        print(i + 1)
                        print('INFERIOR')
                        doppleganger.moverSe(doppleganger, linha-1, i + 1, 'INFERIOR')
                        variavel = 2
                        break
            #parede esquerda Y
            if variavel != 2:
                for i in range(linha-1):
                    if matriz[i+1][0] == self.agente:
                        print(i + 1)
                        print(0)
                        print('ESQUERDA')
                        doppleganger.moverSe(doppleganger, i + 1, 0, 'ESQUERDA')
                        variavel = 2
                        break
            #parede direita Y
            if variavel != 2:
                for i in range(linha-1):
                    if matriz[i+1][coluna-1] == self.agente:
                        print(i + 1)
                        print(coluna-1)
                        print('DIREITA')
                        doppleganger.moverSe(doppleganger, i + 1, coluna - 1, 'DIREITA')
                        variavel = 2
                        break
            if variavel == 2:
                variavel = 0
            else:
                variavel = 2
        else:
            if variavel == 0:
                pass
            else:
                variavel = 2

        ##Centro
        if variavel == 2:
            temp = False
            #Matriz central sem cantos e paredes
            for i in range(coluna-2):
                if temp:
                    break
                else:
                    for j in range(linha-2):
                        if matriz[j+1][i+1] == self.agente:
                            print(j+1)
                            print(i+1)
                            print("CENTRO")
                            doppleganger.moverSe(doppleganger, j + 1, i + 1, 'CENTRO')
                            temp = True
                            break



    def moverSe(self, linha, coluna, info):
        if info == 'CANTO1':
            temp = random.randint(0, 1)
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):#trocar por função de lista dps
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha + 1, coluna)
                    matriz[linha + 1][coluna] = self.agente
            else:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna + 1)
                    matriz[linha][coluna + 1] = self.agente
        if info == 'CANTO2':
            temp = random.randint(0, 1)
            if temp == 1:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha-1, coluna)
                matriz[linha - 1][coluna] = self.agente
            else:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha, coluna+1)
                matriz[linha][coluna + 1] = self.agente
        if info == 'CANTO3':
            temp = random.randint(0, 1)
            if temp == 1:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha+1, coluna)
                matriz[linha + 1][coluna] = self.agente
            else:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha, coluna-1)
                matriz[linha][coluna - 1] = self.agente
        if info == 'CANTO4':
            temp = random.randint(0, 1)
            if temp == 1:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha-1, coluna)
                matriz[linha - 1][coluna] = self.agente
            else:
                doppleganger.seguranca(doppleganger, linha, coluna)
                doppleganger.consequencia(doppleganger, linha, coluna-1)
                matriz[linha][coluna - 1] = self.agente
        if info == 'SUPERIOR':
            temp = random.randint(0, 2)
            if temp == 0:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna-1)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 2:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
        if info == 'INFERIOR':
            temp = random.randint(0, 2)
            if temp == 0:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha-1, coluna)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 2:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'ESQUERDA':
            temp = random.randint(0, 2)
            if temp == 0:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna+1)
                    matriz[linha][coluna+1] = self.agente
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
            if temp == 2:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'DIREITA':
            temp = random.randint(0, 2)
            if temp == 0:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna-1)
                    matriz[linha][coluna-1] = self.agente
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha+1, coluna)
                    matriz[linha+1][coluna] = self.agente
            if temp == 2:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha-1, coluna)
                    matriz[linha-1][coluna] = self.agente
        if info == 'CENTRO':
            temp = random.randint(0, 3)
            if temp == 0:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna-1)
                    matriz[linha][coluna - 1] = self.agente
            if temp == 1:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha+1, coluna)
                    matriz[linha + 1][coluna] = self.agente
            if temp == 2:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha-1, coluna)
                    matriz[linha - 1][coluna] = self.agente
            if temp == 3:
                if doppleganger.seguranca(doppleganger, linha, coluna):
                    return True
                else:
                    doppleganger.consequencia(doppleganger, linha, coluna+1)
                    matriz[linha][coluna + 1] = self.agente
        if self.agente == 'W':
                teste.sense_Wumpus()
                
    def sentir(self):
        return

    def seguranca(self, linha, coluna):
        if sensePoco[0][0] == 'b' or senseWumpus[0][0] == 'F':
            temp = random.randint(0, 1)
            if temp == 0:
                matriz[0][0] = 's'
                matriz[1][0] = self.agente
            if temp == 1:
                matriz[0][0] = 's'
                matriz[0][1] = self.agente
            return True

        if sensePoco[linha][coluna] == 'b' or senseWumpus[linha][coluna] == 'F':
            matriz[self.estado_anterior_linha][self.estado_anterior_coluna] = self.agente
            matriz[linha][coluna] = 's'
            if sensePoco[linha][coluna] == 'b':
                memoria[linha][coluna] = 'b'
                doppleganger.definirPoco(doppleganger, linha, coluna)
                print('Brisa')
            if senseWumpus[linha][coluna] == 'F':
                memoria[linha][coluna] = 'f'
                print('fedor')
            return True
        else:
            matriz[linha][coluna] = 's'
            self.estado_anterior_linha = linha
            self.estado_anterior_coluna = coluna
            return False

        return False

    def definirPoco(self, linha, coluna):
        print('fodase')
        if memoria[linha+1][coluna+1] == 'b':
            print('fodase2')
            memoria[linha][coluna+1] = 'p'


    def consequencia(self, linha, coluna):
        if matriz[linha][coluna] == 'O' and self.agente == 'A':
            self.ouro = True
            matriz[linha][coluna] = 'V'
            teste.plot()
            print('Peguei Ouro :O')
        if self.agente == 'A':
            if matriz[linha][coluna] == 'P' or matriz[linha][coluna] == 'W':
                matriz[linha][coluna] = 'X'
                teste.plot()
                print('Morri :(')
                exit()
        if self.agente == 'W':
            if matriz[linha][coluna] == 'P':
                matriz[linha][coluna] = 'M'
                teste.plot()
                print('Wumpus Morreu :D')
                exit()

        else:
            pass

    def ganhar(self):
        if matriz[0][0] == self.agente and self.ouro == True:
            print('Ganhei :)')
            exit()












teste = gerarMatriz()
x = 5
teste.gerar(x, x)
teste.plot()
teste.pocos()
teste.plot()
teste.ouro()
teste.plot()
teste.wumpus()
########################
teste.plot()
teste.sense_Poco()
teste.plotPoco()
########################
teste.plot()
teste.sense_Ouro()
teste.plotOuro()
########################
teste.plot()
teste.sense_Wumpus()
teste.plotWumpus()
########################
teste.setAgente()
teste.plot()
########################
test = doppleganger()
test.mover()
teste.plot()
i = 1

#while True:
for j in range(140):
    print(str(i) + ' movimentos')
    test.mover()
    teste.plot()
    i = i + 1


teste.plotMemoria()
#teste.plotWumpus()
