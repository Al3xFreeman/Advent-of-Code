import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day10Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    score = []
    pending = []

    for line in lines:
        bad = False
        expected = []

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
                    bad = True
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
        
        if(not bad):
            pending.append(expected)
    print(len(pending))
    for pendiente in pending:
        score_temp = 0
        #print(len(pendiente))
        for elem in reversed(pendiente):
            score_temp *= 5
            if(elem == ')'):
                score_temp += 1
            elif(elem == ']'):
                score_temp += 2
            elif(elem == '}'):
                score_temp += 3
            elif(elem == '>'):
                score_temp += 4
        score.append(score_temp)

    score.sort()
    print(len(score), score)
    print(score[len(score)//2])