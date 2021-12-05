import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day1P1Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

rolling_window = 3
prev = count = 0
roll = []

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    #Compute 3-value rolling window
    i = 0
    while(i < len(lines) - rolling_window + 1):
        sum = 0
        for j in range(rolling_window):
            sum += int(lines[i + j])
        
        roll.append(sum)
        i += 1

    for val in roll:
        if(val > prev):
            count += 1
        
        prev = val

print(count - 1) #Removes the first increment (from 0 to the first value)

