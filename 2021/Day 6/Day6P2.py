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

    pecesDict = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }
    
    #Populate the initial array
    for pez in peces:
        pecesDict[pez] += 1

    for j in range(256):
        nuevos = pecesDict[0]
        for i in range(len(pecesDict) - 1):
            pecesDict[i] = pecesDict[i + 1]
        pecesDict[8] = nuevos
        pecesDict[6] += nuevos

    num_peces = sum(pecesDict.values())

    print(num_peces)