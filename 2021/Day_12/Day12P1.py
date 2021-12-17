import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day12Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)


def bfd(cave, connections, caveStat, caveVis, uniqueCaves, path):
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
    if not caveStatus[caveIndex]: 
        copyCaveVis[caveIndex] = True

    print("Current cave: ", uniqueCaves[caveIndex], "|| PATH: ", copyPath, " END??? ", cave == "end")

    if cave == "end":
        return 1

    indexOfCave = uniqueCaves.index(cave)
    for adj in connections[indexOfCave]:
        indexOfAdj = uniqueCaves.index(adj)
        
        if not caveVis[indexOfAdj]:
            count += bfd(adj, connections, copyCaveStat, copyCaveVis, uniqueCaves, copyPath)

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

    print(bfd(uniqueCaves[startIndex], cavesConnections, caveStatus, caveVisited, uniqueCaves, []))