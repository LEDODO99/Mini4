import random as rand
import copy
class Tablero():
    def __init__(self):
        self.jugador1_casa=[4,4,4,4,4,4]
        self.jugador1_final=0
        self.jugador2_casa=[4,4,4,4,4,4]
        self.jugador2_final=0
        self.turno=1
    def get_possible_moves(self,turno):
        pos=[]
        if (turno==1):
            for i in range(6):
                if(self.jugador1_casa[i]>0):
                    pos.append(i)
        else:
            for i in range(6):
                if(self.jugador2_casa[i]>0):
                    pos.append(i)
        return pos       
    def get_board(self):
        return self.jugador1_casa,self.jugador1_final,self.jugador2_casa,self.jugador2_final,self.turno
    def checkOver(self):
        over=True
        if (self.turno==1):
            for i in self.jugador1_casa:
                if (i>0):
                    over=False
                    break
        else:
            for i in self.jugador2_casa:
                if (i>0):
                    over=False
                    break
        return over
    def checkWinner(self):
        jugador1_total=sum(self.jugador1_casa)+self.jugador1_final
        jugador2_total=sum(self.jugador2_casa)+self.jugador2_final
        self.jugador1_final=jugador1_total
        self.jugador2_final=jugador2_total
        self.jugador1_casa=[0,0,0,0,0,0]
        self.jugador2_casa=[0,0,0,0,0,0]
        if(jugador1_total>jugador2_total):
            return 1
        if(jugador1_total<jugador2_total):
            return 2
        if(jugador1_total==jugador2_total):
            return 3
    def get_turno(self):
        return (self.turno)
    def imprimir(self):
        print('/'+' | '+str(self.jugador2_casa[5])+' | '+str(self.jugador2_casa[4])+' | '+str(self.jugador2_casa[3])+' | '+str(self.jugador2_casa[2])+' | '+str(self.jugador2_casa[1])+' | '+str(self.jugador2_casa[0])+' | '+"\\")
        print(str(self.jugador2_final)+' |   |   |   |   |   |   | '+str(self.jugador1_final))
        print('\\'+' | '+str(self.jugador1_casa[0])+' | '+str(self.jugador1_casa[1])+' | '+str(self.jugador1_casa[2])+' | '+str(self.jugador1_casa[3])+' | '+str(self.jugador1_casa[4])+' | '+str(self.jugador1_casa[5])+' | '+"/")
    def caido_vacio(self,jugador,pos):
        if (jugador==1):
            self.jugador1_final=self.jugador1_final+self.jugador1_casa[pos]+self.jugador2_casa[5-pos]
            self.jugador1_casa[pos]=0
            self.jugador2_casa[5-pos]=0
        else:
            self.jugador2_final=self.jugador2_final+self.jugador2_casa[pos]+self.jugador1_casa[5-pos]
            self.jugador2_casa[pos]=0
            self.jugador1_casa[5-pos]=0
    def movimiento(self,jugador,casa):
        if(self.turno==jugador):
            if(jugador==1):
                cant=self.jugador1_casa[casa]
                if(cant>0):
                    self.jugador1_casa[casa]=0
                    current=casa
                    while cant>0:
                        if (current==0):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current]=self.jugador1_casa[current]+1
                        elif (current==1):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current]=self.jugador1_casa[current]+1
                        elif (current==2):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current]=self.jugador1_casa[current]+1
                        elif (current==3):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current]=self.jugador1_casa[current]+1
                        elif (current==4):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current]=self.jugador1_casa[current]+1
                        elif (current==5):
                            current=current+1
                            cant=cant-1
                            self.jugador1_final=self.jugador1_final+1
                        elif (current==6):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==7):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==8):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==9):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==10):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==11):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current-7]=self.jugador2_casa[current-7]+1
                        elif (current==12):
                            current=0
                            cant=cant-1
                            self.jugador1_casa[0]=self.jugador1_casa[0]+1
                    if(current<6):
                        if(self.jugador1_casa[current]==1):
                            self.caido_vacio(1,current)
                    if (current!=6):
                        self.turno=2
            else:
                cant=self.jugador2_casa[casa]
                if(cant>0):
                    self.jugador2_casa[casa]=0
                    current=casa
                    while cant>0:
                        if (current==0):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current]=self.jugador2_casa[current]+1
                        elif (current==1):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current]=self.jugador2_casa[current]+1
                        elif (current==2):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current]=self.jugador2_casa[current]+1
                        elif (current==3):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current]=self.jugador2_casa[current]+1
                        elif (current==4):
                            current=current+1
                            cant=cant-1
                            self.jugador2_casa[current]=self.jugador2_casa[current]+1
                        elif (current==5):
                            current=current+1
                            cant=cant-1
                            self.jugador2_final=self.jugador2_final+1
                        elif (current==6):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==7):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==8):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==9):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==10):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==11):
                            current=current+1
                            cant=cant-1
                            self.jugador1_casa[current-7]=self.jugador1_casa[current-7]+1
                        elif (current==12):
                            current=1
                            cant=cant-1
                            self.jugador2_casa[0]=self.jugador2_casa[0]+1
                    if(current<6):
                        if(self.jugador2_casa[current]==1):
                            self.caido_vacio(2,current)
                    if (current!=6):
                        self.turno=1
class bot():
    def __init__(self,dificulty):
        self.dificulty=dificulty
    def randomMove(self,board):
        over=board.checkOver()
        while(not over):
            moves=board.get_possible_moves(board.get_turno())
            
            movimiento=rand.randint(0,len(moves)-1)
            board.movimiento(board.get_turno(),moves[movimiento])
            over=board.checkOver()
        if(board.checkWinner()==2):
            return 1
        else:
            return 0
    def move(self,board):
        moves=board.get_possible_moves(2)
        if(self.dificulty=="1"):
            movimiento=rand.randint(0,len(moves)-1)
            return(moves[movimiento])
        else:
            iterations=0
            results=[]
            for i in range(len(moves)):
                results.append(0)
            if (self.dificulty=="2"):
                iterations=500
            else:
                iterations=10000
            for i in range(iterations):
                bord=copy.deepcopy(board)
                movimiento=rand.randint(0,len(moves)-1)
                bord.movimiento(2,moves[movimiento])
                results[movimiento]=results[movimiento]+self.randomMove(bord)
            print("results:",results)
            print("chosen:",moves[results.index(max(results))])
            return results.index(max(results))

#### print("Bienvenido a Mancala")
print("Elija su dificultad:")
print("1. Noob")
print("2. Avanzado")
print("3. Pro")
hard=input("Escriba 1, 2 o 3 dependiendo de la dificultad: ")
tablero=Tablero()
over=tablero.checkOver()
cpu=bot(hard)
while (not over):
    if(tablero.get_turno()==1):
        print("Turno de jugador 1")
        tablero.imprimir()
        print(str('  | 0 | 1 | 2 | 3 | 4 | 5 |  '))
        casa=int(input("Ingrese el numero de la casa que desea hacer: "))
        tablero.movimiento(1,casa)
    else:
        print("Turno de jugador 2")
        tablero.imprimir()
        tablero.movimiento(2,cpu.move(tablero))
    over=tablero.checkOver()
print("Fin del juego\n Tablero final:")
tablero.imprimir()
ganador=tablero.checkWinner()
print("Tablero de puntos:")
tablero.imprimir()
print("Ganador: Jugador",ganador)
