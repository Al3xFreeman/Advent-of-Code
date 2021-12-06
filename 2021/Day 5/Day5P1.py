






#I Really want to change this one, I made it trying to generalice too much lol









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

    coordinates = list(filter(lambda x: (x[0][0] == x[1][0] or x[0][1] == x[1][1]), coordinates))

    cols = []
    for i in range(1000):
        cols.append([0] * 1000)

    print(len(coordinates))
    for coord in coordinates:
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
                count += 1
#        print("COUNT", count)
    
    tope = 0
    count = 0
    for row in cols:
        for elem in row:
            if elem > 1:
                count += 1
            if elem > tope:
                tope = elem

    print(count)
    print(tope)