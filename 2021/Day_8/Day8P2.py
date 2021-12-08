import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Day8Input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def findSegments(numbers):
    
    for num in numbers:
        if len(num) == 2:
            one = num
        if len(num) == 3:
            seven = num
        if len(num) == 4:
            four = num
        if len(num) == 7:
            eight = num
    
    one_set = set(one)
    seven_set = set(seven)
    four_set = set(four)
    eight_set = set(eight)

    segment_a = seven_set.difference(one_set)
    segment_b_d = four_set.difference(one_set)

    segment_a_b_c_d_f = set.union(one_set, segment_a, segment_b_d)
    #Select the element that has the suitable segments to be '9'
    count = 0
    for num in numbers:
        if (len(set(num).difference(segment_a_b_c_d_f)) == 1 and len(num) > len(segment_a_b_c_d_f)):
            segment_g = set(num).difference(segment_a_b_c_d_f)
            count += 1
            #print(count, segment_g, "LEN: ", len(set(num).difference(segment_a_b_c_d_f)), "Len num: ", len(num), set(num), "Len segment: ", len(segment_a_b_c_d_f), segment_a_b_c_d_f)
    
    segment_a_c_f_g = set.union(one_set, segment_a, segment_g)
    #Select the element that has the suitable segments to be '3'
    for num in numbers:
        diff = set(num).difference(segment_a_c_f_g)
        if (len(diff) == 1 and len(num) > len(segment_a_c_f_g)):
            segment_d = diff
    segment_a_d_c_f_g = set.union(segment_a, segment_d, segment_g, one_set)
    #Select the element that has the suitable segments to be '5'
    for num in numbers:
        if (len(set(num).difference(segment_a_d_c_f_g)) == 1 and len(num) > len(segment_a_d_c_f_g)):
            segment_b = set(num).difference(segment_a_d_c_f_g)

    segment_a_b_c_d_f_g = set.union(segment_a, segment_b, segment_d, one_set, segment_g)
    segment_e = eight_set.difference(segment_a_b_c_d_f_g)

    #Select the element that has the suitable segments to be '6'
    segment_a_b_d_e_g = set.union(segment_a, segment_b, segment_d, segment_e, segment_g)
    for num in numbers:
        if(len(set(num).difference(segment_a_b_d_e_g)) == 1 and len(num) > len(segment_a_b_d_e_g)):
            segment_f = set(num).difference(segment_a_b_d_e_g)

    segment_c = eight_set.difference(set.union(segment_a, segment_b, segment_d, segment_e, segment_g, segment_f))

    segments_final = {'a':list(segment_a)[0], 'b':list(segment_b)[0], 'c':list(segment_c)[0], 'd':list(segment_d)[0], 'e':list(segment_e)[0], 'f':list(segment_f)[0], 'g':list(segment_g)[0]}
    print(segments_final)
    return segments_final

def num_decode(num, segments):
    realSegment = []
    dec = list(segments.values())
    key_list = list(segments.keys())
    print(num)
    for segment in num:
        ind = dec.index(segment)
        print(segment, ind, key_list[ind])
        realSegment.append(key_list[ind])

    print(realSegment)

    if(set(realSegment) == set('abcefg')):
        return 0
    elif(set(realSegment) == set('cf')):
        return 1
    elif(set(realSegment) == set('acdeg')):
        return 2
    elif(set(realSegment) == set('acdfg')):
        return 3
    elif(set(realSegment) == set('bcdf')):
        return 4
    elif(set(realSegment) == set('abdfg')):
        return 5
    elif(set(realSegment) == set('abdefg')):
        return 6
    elif(set(realSegment) == set('acf')):
        return 7
    elif(set(realSegment) == set('abcdefg')):
        return 8
    elif(set(realSegment) == set('abcdfg')):
        return 9



def result(nums, segments):
    i = 3
    res = 0
    for num in nums:
        res += num_decode(num, segments) * (pow(10, i))
        print(res)
        i -= 1
    print(res)
    return res

with open(abs_file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    output = []
    decode = []

    for line in lines:
        parts = line.split('|')
        output.append(parts[0].split())
        decode.append(parts[1].split())
        
    count = 0
    for out, dec in zip(output, decode):

        segments = findSegments(out)
        
        count += result(dec, segments)


    print(count)
    print(len(output))
