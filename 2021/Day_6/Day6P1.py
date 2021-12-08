import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day6Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    peces = []
    tmp = peces.copy()
    peces = lines[0]
    peces = peces.split(',')
    peces = list(map(int, peces))

    for j in range(80):

        for i, pez in enumerate(tmp):
            if pez == 0:
                peces.append(9)
                peces[i] = 7
            else:
                peces[i] = pez
        
        tmp = list(map(lambda x : x - 1, peces))

        peces = tmp.copy()

        print("ITER: ", j + 1, " | Num peces: ", len(peces))