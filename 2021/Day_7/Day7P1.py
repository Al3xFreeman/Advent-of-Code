import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day7Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    crabs = list(map(int, lines[0].split(',')))

    maxPos = max(crabs)
    fuel = []

    for pos in range(maxPos):
        fuelCount = 0
        for i in crabs:
            fuelCount += abs(pos - i)
        fuel.append(fuelCount)
    
    print(min(fuel), "Index: ", fuel.index(min(fuel)))
