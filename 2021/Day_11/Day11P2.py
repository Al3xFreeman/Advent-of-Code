import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day11Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def flashSurround(i, j, luz):
    elemsToAdd = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (i + x < 0 or i + x > 9 or j + y < 0 or j + y > 9):
                elemsToAdd.add((i+x, j+y))
    return elemsToAdd

def allFlash(luz):
    allCero = True
    for line in luz:
        for elem in line:
            if elem != 0:
                allCero = False

    return allCero


with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
    count = 0
    lvl = []

    for line in lines:
        tmp = list(map(int, line))
        lvl.append(tmp)

    queue = []
    flashCount = 0

    for k in range(1000):

        #Increase all
        for i,linea in enumerate(lvl):
            for j,elem in enumerate(linea):
                lvl[i][j] += 1
                if(lvl[i][j] > 9):
                    queue.append((i, j))

        
        #If any one is going to flash, increase every neighbour
        for elem in queue:
            x, y = elem
            hit = flashSurround(x, y, queue)
            for squid in hit:
                lvl[squid[0]][squid[1]] += 1
                if lvl[squid[0]][squid[1]] > 9 and (squid[0], squid[1]) not in queue:
                    queue.append((squid[0], squid[1]))
        

        #Flashes
        for i,linea in enumerate(lvl):
            for j,elem in enumerate(linea):
                if(lvl[i][j] > 9):
                    lvl[i][j] = 0
                    flashCount += 1

        queue = []
        if(allFlash(lvl)):
            cycle = k + 1
            break

    print(cycle)