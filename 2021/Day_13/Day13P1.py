import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day13Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    
    points = [tuple(map(int, x.split(','))) for x in lines[:-13]]
    
    setPoints = set(points)
    folds = [x.split('=') for x in lines[-12:]]
    folds = list(map(lambda x: [x[0][-1], int(x[1])], folds))

    for fold in folds:
        newFold = set()
        if fold[0] == 'x': #fold through axis x
            for point in setPoints:
                if(point[0] > fold[1]):
                    x = fold[1] - (point[0] - fold[1]) #x
                else:
                    x = point[0]

                newFold.add((x, point[1]))
        else: #fold through axis y
            for point in setPoints:
                if(point[1] > fold[1]):
                    y = fold[1] - (point[1] - fold[1]) #y
                else:
                    y = point[1]

                newFold.add((point[0], y))
        print(len(newFold))
        setPoints = newFold

    print(len(setPoints))

    
