f = [int(x) for x in open("d2.txt").read().split(",")]

for x in range(100):
    for y in range(100):
        l = [x for x in f]

        l[1] = x
        l[2] = y

        index = 0
        out = False
        while not out:
            opCode = l[index]
            first_index = l[index + 1]
            second_index = l[index + 2]
            placement = l[index + 3]

            if opCode == 1:
                l[placement] = l[first_index] + l[second_index]
            elif opCode == 2:
                l[placement] = l[first_index] * l[second_index]
            #   elif opCode == 99:
            #       out = True
            else:
                out = True
            index += 4

        if l[0] == 19690720:
            print("noun: " + str(x) + " verb: " + str(y))