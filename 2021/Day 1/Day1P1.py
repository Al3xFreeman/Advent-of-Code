import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day1P1Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

prev = count = 0

with open(abs_file_path) as file:

    for line in file:
        if(int(line) > prev):
            count += 1
        
        prev = int(line)

print(count - 1) #Removes the first increment (from 0 to the first value)

