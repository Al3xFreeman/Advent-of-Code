import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day9Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

marks = []

def checkAdjacent(i, j, l):
    global marks

    count = 0
    if(((l[i][j] == '9') or marks[i][j] or i < 0 or j < 0 or i > 100 or j > 100)):
        return count
    
    marks[i][j] = True
    count += 1
    
    count += checkAdjacent(i - 1, j, l) #arriba
    count += checkAdjacent(i + 1, j, l) #abajo
    count += checkAdjacent(i, j - 1, l) #izq
    count += checkAdjacent(i, j + 1, l) #drcha
    
    return count
    
with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
    firstLine = ['9'] * (len(lines[1]) + 2)
    linesFixed = []
    linesFixed.append(firstLine)
    marks.append([False] * (len(lines[0]) + 2))

    for line in lines:
        linesFixed.append('9' + line + '9')
        marks.append([False] * (len(line) + 2))
    
    marks.append([False] * (len(lines[0]) + 2))
    
    linesFixed.append(firstLine)

    count = []
    for i, line in enumerate(linesFixed):
        for j, elem in enumerate(line):
            if(not i == 0 and not j == 0 and not i == (len(linesFixed) - 1) and not j == (len(line) - 1)):
                elem_int = int(elem)
                if elem_int < int(linesFixed[i][j - 1]) and elem_int < int(linesFixed[i][j + 1]) and elem_int < int(linesFixed[i - 1][j]) and elem_int < int(linesFixed[i + 1][j]):
                    count.append(checkAdjacent(i, j, linesFixed))

    count_int = list(map(int, count))
    count_int.sort()
    
    total = 1
    for elem in count_int[-3:]:
        total *= elem

    print(total)