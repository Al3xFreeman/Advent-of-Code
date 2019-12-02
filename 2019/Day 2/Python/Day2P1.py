f = [int(x) for x in open("d2.txt").read().split(",")]

index = 0
out = False
while not out:
    opCode = f[index]
    first_index = f[index + 1]
    second_index = f[index + 2]
    placement = f[index + 3]

    if opCode == 1:
        f[placement] = f[first_index] + f[second_index]
    elif opCode == 2:
        f[placement] = f[first_index] * f[second_index]
    #   elif opCode == 99:
    #       out = True
    else:
        out = True
    index += 4

print(f[0])