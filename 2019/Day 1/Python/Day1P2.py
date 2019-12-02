import math


def calc_fuel(mass):
    fuel_fun = (math.trunc(mass / 3) - 2)
    if fuel_fun > 0:
        return calc_fuel(fuel_fun) + fuel_fun
    else:
        return 0

f = open("Day 1 Problem 1 input.txt", "r")

f1 = f.readlines()

fuel = 0
for x in f1:
    x = int(x)
    fuel += calc_fuel(x)

print(fuel)
