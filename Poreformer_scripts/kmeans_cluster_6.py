import fileinput
import numpy as np
import sys
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]


dict1 = {}
for i in fileinput.input(files=(input_file1)):
    j = i.strip().split(',')
    m = j[0].split('pos')[1]
    dict1[m] = j[1:]
    # print(j[0],j[1],jn1,jn2,jn3,jn4,jn5)

    # print(dict1)
# h = 0
list1 = []
dict2 ={}
for i in fileinput.input(files=(input_file2)):
    j = i.strip().split(' ')
    n = j[1].split('pos')[1]
    dict2[n]= []
    for m in range(int(n) - 6, int(n) + 7 ):
        #dict2[j].append(dict1[str(m)])
        if str(m) in dict1.keys():
            a = dict1[str(m)]
            #print(a)
            dict2[n].append(','.join(a))
#print(dict2)
for i in dict2.keys():
    a = ','.join(dict2[i])
    print('pos'+i+','+a)
