import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day10Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    score = 0
    expected = []

    for line in lines:
        if(line[0] == '('):
            expected.append(')')
        elif(line[0] == '['):
            expected.append(']')
        elif(line[0] == '{'):
            expected.append('}')
        elif(line[0] == '<'):
            expected.append('>')

        for elem in line[1:]:
            #print("elem: ", elem, "expected: ", expected, elem not in {'(', '[', '{', '<'} and elem != expected[-1])
            if(elem not in {'(', '[', '{', '<'}):
                if(elem != expected[-1]):
                    if(elem == ')'):
                        score += 3
                    elif(elem == ']'):
                        score += 57
                    elif(elem == '}'):
                        score += 1197
                    elif(elem == '>'):
                        score += 25137
                    #print("Chao")
                    break
                expected.pop()

            if(elem == '('):
                expected.append(')')
            elif(elem == '['):
                expected.append(']')
            elif(elem == '{'):
                expected.append('}')
            elif(elem == '<'):
                expected.append('>')
            
    print(score)