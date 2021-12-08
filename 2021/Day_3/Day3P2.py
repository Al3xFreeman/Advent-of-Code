import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day3P1Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def binList_to_dec(list):
    num_dec = 0
    i = len(list)
    for elem in list:
        i -= 1
        num_dec += int(elem)*(pow(2, i))
    
    return num_dec

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    oxigenList = lines.copy()
    co2List = lines.copy()
    bit = 0

    while ((bit < len(lines[0])) and ((len(oxigenList) > 1) or (len(co2List) > 1))):
        oxigencount = 0
        co2Count = 0
        for line in oxigenList:
            oxigencount += int(line[bit])

        for line in co2List:
            co2Count += int(line[bit])

        selectOxigen = (oxigencount >= (len(oxigenList)/2))
        selectCo2 = (co2Count < (len(co2List)/2))

        oxigenList = list(filter(lambda l: (int(l[bit]) == selectOxigen), oxigenList))
        if(len(co2List) > 1):
            co2List = list(filter(lambda l: (int(l[bit]) == selectCo2), co2List))

        bit += 1

    #transform the binary number to decimal
    oxigen = binList_to_dec(oxigenList[0])
    co2 = binList_to_dec(co2List[0])

    print("Oxigen: ", oxigen, "| CO2: ", co2)
    print(oxigen * co2)
   