import fileinput
import numpy as np
import ast
import sys
input_file = sys.argv[1]

for i in fileinput.input(files=(input_file)):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    ii = ast.literal_eval(i)
    for m in range(2,len(ii)):
        list1.append(ii[m][0])
        list2.append(ii[m][1])
        list3.append(ii[m][2])
        list4.append(ii[m][3])
        list5.append(ii[m][4])

    d1 = "-".join(list1)
    d2 = "-".join(list2)
    d3 = "-".join(list3)
    d4 = "-".join(list4)
    d5 = "-".join(list5)
    print(ii[0]+','+ii[1]+','+d1+','+d2+','+d3+','+d4+','+d5)
