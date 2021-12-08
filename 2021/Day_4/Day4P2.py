import os
import numpy as np

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day4Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

bingo_size = 5
currentLine = 2

def calcScoreTablero(tablero, visit):
    score = 0
    for filaNum, filaVisit in zip(tablero, visit):
        for num, visit in zip(filaNum, filaVisit):
            if(visit == None):
                score += int(num)
    return score

def isBoardWinner(tablero, visit):
    for filaVisit in visit:
        if all(filaVisit):
            return True, calcScoreTablero(tablero, visit)
    for filaVisitT in np.transpose(visit):
        if all(filaVisitT):
            return True, calcScoreTablero(tablero, visit)

    return False

def isThereWinner(tablerosVisit, winners):
    i = 0
    for tableroVisit, winner in zip(tablerosVisit, winners):
        if not winner:
            for filaVisit in tableroVisit:
                if all(filaVisit):
                    winners[i] = True
            
            for filaVisitT in np.transpose(tableroVisit):
                if all(filaVisitT):
                    winners[i] = True
        i += 1

    return winners


def drawNumber(number, tableros, tablerosVisit):
    for tablero, tableroVisit in zip(tableros, tablerosVisit):
        for filaTablero, filaVisit in zip(tablero, tableroVisit):
            for k, elemTablero in enumerate(filaTablero):
                if(number == elemTablero):
                    filaVisit[k] = True


with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    order = lines[0].split(',')

    tableros = []
    tablerosVisit = []

    while currentLine < len(lines):
        tmp = []
        tmpVisit = []
        for i in range(bingo_size):
            tmp.append(lines[currentLine].split())
            tmpVisit.append([None] * bingo_size)
            currentLine += 1
        currentLine += 1

        tableros.append(tmp)
        tablerosVisit.append(tmpVisit)

    
    win = False
    winBoards = [False] * len(tableros)
    while( (len(winBoards) - sum(winBoards) != 1 ) and len(order) > 0):
        num = order.pop(0)
        drawNumber(num, tableros, tablerosVisit)
        winBoards = isThereWinner(tablerosVisit, winBoards)
    
    #get last  winning board
    lastBoard = winBoards.index(False)

    while(not isBoardWinner(tableros[lastBoard], tablerosVisit[lastBoard])):
        num = order.pop(0)
        drawNumber(num, tableros, tablerosVisit)

    score = calcScoreTablero(tableros[lastBoard], tablerosVisit[lastBoard])
    print(len(winBoards) - sum(winBoards))
    print(score)
    print(int(num) * score)
    print(isBoardWinner(tableros[lastBoard], tablerosVisit[lastBoard]))