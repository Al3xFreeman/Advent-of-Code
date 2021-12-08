import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day8Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    output = []

    for line in lines:
        output.append(line.split('|')[1].split())
        
    count = 0
    for out in output:
        for elem in out:
            if len(elem) in {2,4,3,7}:
                count += 1

    print(count)
