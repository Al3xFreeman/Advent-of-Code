import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day2P1Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    hor = 0
    ver = 0
    aim = 0

    for line in lines:
        dir = line.split()[0]
        ammount = int(line.split()[1])

        if(dir == "forward"):
            hor += ammount
            ver += aim * ammount
        elif(dir == "up"):
            aim -= ammount
        else:
            aim += ammount

    print(hor * ver)
