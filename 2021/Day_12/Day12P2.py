import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day12Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def bfd(cave, connections, caveStat, caveVis, uniqueCaves, path, twice):
    copyPath = []
    copyCaveVis = []
    copyCaveStat = []
    for p in path:
        copyPath.append(p)

    for v, s in zip(caveVis, caveStat):
        copyCaveVis.append(v)
        copyCaveStat.append(s)
    count = 0
    copyPath.append(cave)
    caveIndex = uniqueCaves.index(cave)


    if cave == "end" and twice:
        valid = True
        if twice:
            #print("Check")
            #print("CHECKKKKKKK", copyPath[1:len(copyPath) - 1], "TWICE???", twice, copyCaveVis[1:len(copyCaveVis) - 1])
            for c in copyPath[1:len(copyPath) - 1]:
                #print(c)
                indexOfC = uniqueCaves.index(c)
                if(not copyCaveStat[indexOfC] and not copyCaveVis[indexOfC]):
                    valid = False
        
        if valid:
            #print("Current cave: ", uniqueCaves[caveIndex], "|| PATH: ", copyPath, " END??? ", cave == "end", "TWICE", twice)
            return 1
        else:
            return 0


    if not caveStatus[caveIndex]: 
        copyCaveVis[caveIndex] = True

    indexOfCave = uniqueCaves.index(cave)
    for adj in connections[indexOfCave]:
        indexOfAdj = uniqueCaves.index(adj)
        
        if not caveVis[indexOfAdj]:

            if(not twice):
                count += bfd(adj, connections, copyCaveStat, copyCaveVis, uniqueCaves, copyPath, False)

                auxCopyCaveVis = []
                for cV in copyCaveVis:
                    auxCopyCaveVis.append(cV)

                if(cave != "start"):
                    auxCopyCaveVis[indexOfCave] = False
                if(not caveStat[indexOfCave]):
                    count += bfd(adj, connections, copyCaveStat, auxCopyCaveVis, uniqueCaves, copyPath, True)
            else:
                count += bfd(adj, connections, copyCaveStat, copyCaveVis, uniqueCaves, copyPath, True)

    return count
    


with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    caveLinks = []

    for line in lines:
        link = line.split('-')
        caveLinks.append(link)
    
    uniqueCaves = []
    caveStatus = []

    for cavePair in caveLinks:
        for cave in cavePair:
            if not cave in uniqueCaves:
                caveStatus.append(cave.isupper())
                uniqueCaves.append(cave)

    caveVisited = [False] * len(uniqueCaves)

    cavesConnections = [[] for _ in range(len(uniqueCaves))]
    for cavePair in caveLinks:
        cavesConnections[uniqueCaves.index(cavePair[0])].append(cavePair[1])
        cavesConnections[uniqueCaves.index(cavePair[1])].append(cavePair[0])

    startIndex = uniqueCaves.index("start")
    endIndex = uniqueCaves.index("end")
    print(uniqueCaves)
    print(bfd(uniqueCaves[startIndex], cavesConnections, caveStatus, caveVisited, uniqueCaves, [], False))