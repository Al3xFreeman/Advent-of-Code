import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day3P1Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    occurences = []
    gamma = []
    for x in range(len(lines[0])):
        occurences.append(0)


    for line in lines:
        for i, elem in enumerate(line):
            occurences[i] += int(elem)
        print(occurences)
    
    for pos in occurences:
        if pos >= (len(lines)/2):
            gamma.append(1)
        else:
            gamma.append(0)
    

    #transform the binary number to decimal
    gamma_dec = 0
    i = len(gamma)
    for elem in gamma:
        i -= 1
        gamma_dec += elem*(pow(2, i))
    
    
    epsilon = (pow(2, len(lines[0])) - 1) - gamma_dec

    print(epsilon * gamma_dec)