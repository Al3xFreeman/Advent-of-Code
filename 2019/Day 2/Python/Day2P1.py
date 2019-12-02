

f = open("Day 2 Problem 1 input.txt", "r")

f1 = f.readlines()
my_list_int = []
my_list = f1[0].split(",")
for x in my_list:
    my_list_int.append(int(x))


i = 0
while i < len(my_list_int):
    if my_list_int[i] == 1:
        first_number = my_list_int[my_list_int[i+1]]
        second_number = my_list_int[my_list_int[i+2]]
        position_index = my_list_int[i+3]

        my_list_int[position_index] = first_number + second_number
    elif my_list_int[i] == 2:
        first_number = my_list_int[my_list_int[i + 1]]
        second_number = my_list_int[my_list_int[i + 2]]
        position_index = my_list_int[i + 3]

        my_list_int[position_index] = first_number * second_number
    else:
        break

    i += 4

print(my_list_int[0])
