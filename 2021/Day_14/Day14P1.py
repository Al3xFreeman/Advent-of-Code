import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day14Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


seq = lines[0]

dictPairs = dict(list(map(lambda x: x.split(' -> '), lines[2:])))
print(dictPairs)
seqTmp = lines[0]
seqPairs = []
for j in range(len(seqTmp) - 1):
    seqPairs.append((seqTmp[j] + seqTmp[j + 1]))

print(seq)
for i in range(10):

    newSeq = []
    
    for pair in seqPairs:
        for key in dictPairs:
            if pair in dictPairs:
                val = dictPairs[pair]
                newSeq.append(pair[0])
                newSeq.append(val)
                break
    
    #print(newSeq)
    newSeq.append(seqPairs[-1][1])
    print(i, len(newSeq))
    seqTmp = newSeq
    seqPairs = []
    for j in range(len(seqTmp) - 1):
        seqPairs.append((seqTmp[j] + seqTmp[j + 1]))

results = dict()

for elem in newSeq:
    if elem not in results:
        results[elem] = 1
    else:
        results[elem] += 1

print(max(results.values()) - min(results.values()))