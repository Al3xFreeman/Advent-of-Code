import os
from queue import PriorityQueue
import copy
import time

from numpy import equal
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day15Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    data = [[int(num) + i for i in range(0, 5) for num in row.strip()] for row in file]

newdata = [[num + k for num in row] for k in range(0,5) for row in data]
data = [[num % 9 if num !=9 else 9 for num in row] for row in newdata]


firstLine = [99999] * ((len(data[0])) * 5 + 2)
linesFixed = []
linesFixed.append(firstLine)


for line in data:
    tmpLine = []
    tmpLine.insert(0, 99999)
    for elem in line:
        tmpLine.append(elem)
    tmpLine.append(99999)

    linesFixed.append(tmpLine)

linesFixed.append(firstLine)

goal_pos = (500, 500)
start_pos = (1,1)

pq = PriorityQueue()
closed = copy.deepcopy(linesFixed)

pq.put((0, start_pos))
current_pos = start_pos

i = 0

def indexTuple(arr, tuple):
    anw = arr
    for elem in tuple:
        anw = anw[elem]
    return anw

while current_pos != goal_pos:
    cost, current_pos = pq.get()
    #print("Cost: ", cost, "Current Pos:", current_pos)

    cost_right = cost + linesFixed[current_pos[0]][current_pos[1] + 1]
    cost_left = cost + linesFixed[current_pos[0]][current_pos[1] - 1]
    cost_up = cost + linesFixed[current_pos[0] - 1][current_pos[1]]
    cost_down = cost + linesFixed[current_pos[0] + 1][current_pos[1]]

    pos_right = (current_pos[0], current_pos[1] + 1)
    pos_left = (current_pos[0], current_pos[1] - 1)
    pos_up = (current_pos[0] - 1, current_pos[1])
    pos_down = (current_pos[0] + 1, current_pos[1])
    if indexTuple(closed, pos_right) != -1:
        pq.put((cost_right, pos_right))
        closed[current_pos[0]][current_pos[1] + 1] = -1
    
    if indexTuple(closed, pos_left) != -1:
        pq.put((cost_left, pos_left))
        closed[current_pos[0]][current_pos[1] - 1] = -1


    if indexTuple(closed, pos_up) != -1:
        pq.put((cost_up, pos_up))
        closed[current_pos[0] - 1][current_pos[1]] = -1

    if indexTuple(closed, pos_down) != -1:
        pq.put((cost_down, pos_down))
        closed[current_pos[0] + 1][current_pos[1]] = -1

    i += 1


print("OLEEE", cost, "ITERATIONS: ", i)