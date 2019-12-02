import math

f = open("Day 1 Problem 1 input.txt", "r")

fuel = 0

# f.mode == f.read():
f1 = f.readlines()
for x in f1:
    x = int(x)
    fuel += (math.trunc(x/3) - 2)



print(fuel)