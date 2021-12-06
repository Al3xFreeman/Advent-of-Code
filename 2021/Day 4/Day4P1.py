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

def isThereWinner(tableros, tablerosVisit):
    for tablero, tableroVisit in zip(tableros, tablerosVisit):
        for filaVisit in tableroVisit:
            if all(filaVisit):
                return True, calcScoreTablero(tablero, tableroVisit)
        
        for filaVisitT in np.transpose(tableroVisit):
            if all(filaVisitT):
                return True, calcScoreTablero(tablero, tableroVisit)

    return False, 0


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
    while(not win and len(order) > 0):
        num = order.pop(0)
        drawNumber(num, tableros, tablerosVisit)
        win, score = isThereWinner(tableros, tablerosVisit)
    

    print(int(num) * score)