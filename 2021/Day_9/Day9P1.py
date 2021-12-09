import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day9Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    firstLine = ['9'] * (len(lines[1]) + 2)
    linesFixed = []
    linesFixed.append(firstLine)

    for line in lines:
        linesFixed.append('9' + line + '9')
    
    linesFixed.append(firstLine)

    count = 0
    for i, line in enumerate(linesFixed):
        for j, elem in enumerate(line):
            if(not i == 0 and not j == 0 and not i == (len(linesFixed) - 1) and not j == (len(line) - 1)):
                elem_int = int(elem)
                if elem_int < int(linesFixed[i][j - 1]) and elem_int < int(linesFixed[i][j + 1]) and elem_int < int(linesFixed[i - 1][j]) and elem_int < int(linesFixed[i + 1][j]):
                    count += elem_int + 1

    print(count)
