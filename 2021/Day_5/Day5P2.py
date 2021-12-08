import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day5Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    coordinates = []
    
    for line in lines:
        tmp = []
        for coord in line.split(' -> '):
            tmp.append(coord.split(','))
        coordinates.append(tmp)

    coordinates_rect = list(filter(lambda x: (x[0][0] == x[1][0] or x[0][1] == x[1][1]), coordinates))
    coordinates_diago = list(filter(lambda x: not (x[0][0] == x[1][0] or x[0][1] == x[1][1]), coordinates))

    cols = []
    for i in range(1000):
        cols.append([0] * 1000)

    for coord in coordinates_rect:
        #print(coord)
        count = 0
        
        if coord[0][0] == coord[1][0]:
            rn_i = 1
        else: 
            rn_i = abs(int(coord[0][0]) - int(coord[1][0])) + 1
        if coord[0][1] == coord[1][1]:
            rn_j = 1
        else: 
            rn_j = abs(int(coord[0][1]) - int(coord[1][1])) + 1
        
        coord_i = min(int(coord[0][0]), int(coord[1][0]))
        coord_j = min(int(coord[0][1]), int(coord[1][1]))
        
        for i in range(rn_i):
            for j in range(rn_j):
                cols[i + coord_i][j + coord_j] += 1
    

    count = 0
    for row in cols:
        for elem in row:
            if elem > 1:
                count += 1


    print(count)

    for coord in coordinates_diago:
        if(int(coord[0][0]) > int(coord[1][0])): #va hacia arriba
            if(int(coord[0][1]) > int(coord[1][1])): #va hacia la izq
                dir = 0 #arriba-izq
            else:
                dir = 1 #arriba-derecha
        else:
            dir = "abajo"
            if(int(coord[0][1]) > int(coord[1][1])): #va hacia la izq
                dir = 2 #abajo-izq
            else:
                dir = 3 #abajo-derecha


        coord_i = min(int(coord[0][0]), int(coord[1][0]))
        coord_j = min(int(coord[0][1]), int(coord[1][1]))
        print("AAAAAAAAAAAAAAAAAAAAA", abs(int(coord[0][0]) - int(coord[1][0])), coord, dir, "<- DIR")
        for i in range(abs(int(coord[0][0]) - int(coord[1][0])) + 1):
            if(dir == 0):
                cols[int(coord[0][0]) - i][int(coord[0][1]) - i] += 1
            elif(dir == 1):
                cols[int(coord[0][0]) - i][int(coord[0][1]) + i] += 1
            elif(dir == 2):
                cols[int(coord[0][0]) + i][int(coord[0][1]) - i] += 1
            elif(dir == 3):
                cols[int(coord[0][0]) + i][int(coord[0][1]) + i] += 1

    count = 0
    for row in cols:
        for elem in row:
            if elem > 1:
                count += 1

    print(count)

