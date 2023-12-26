#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/5/30 13:36
# @Author  : YZY
# @FileName: out-dianliu.py
# @Software: PyCharm

import fileinput
import ast
import collections
import sys
in_filev1 = sys.argv[1]

dict1 ={}
dict1 = collections.OrderedDict()
list1 =[]
header = 0
for i in fileinput.input(files=(in_filev1+'002.sam')):
    if not i.strip().startswith("@"):
        j = i.strip().split('\t')
        # print(j[0])
        dict1[j[0]] = []
        dict1[j[0]].append(j[1])
    else:
        header +=1


# print(header)

for i in fileinput.input(files=(in_filev1+'001.txt')):
    # print(i)
    ii = ast.literal_eval(i)
    # print(ii)
    if dict1[ii[0]][0] == '16':

        # print(ii[1][::-1])
        dict1[ii[0]].append(ii[1][::-1])
        dict1[ii[0]].append(ii[2][::-1])
        dict1[ii[0]].append(ii[3][::-1])
        dict1[ii[0]].append(ii[4][::-1])
        dict1[ii[0]].append(ii[5][::-1])
    else:
        dict1[ii[0]].append(ii[1])
        dict1[ii[0]].append(ii[2])
        dict1[ii[0]].append(ii[3])
        dict1[ii[0]].append(ii[4])
        dict1[ii[0]].append(ii[5])
    # print(ii[1])
    # print(dict1[ii[0]][0])

    # dict1[ii[0]]= [ii[1],ii[2],ii[3],ii[4],ii[5]]
#print(dict1)
with open(in_filev1+'.chuli.txt', 'w') as fw1:
    h =0
    while h < header:
        print("",file=fw1)
        h+=1
    for i,ii in dict1.items():
        b1 = ",".join(ii[1])
        b2 = ",".join(ii[2])
        b3 = ",".join(ii[3])
        b4 = ",".join(ii[4])
        b5 = ",".join(ii[5])
        #print(ii[1],ii[2],ii[3],ii[4],ii[5])
        print("d1:B:S," + b1+ "\t" + "d2:B:S," + b2+ "\t" + "d3:B:S," + b3+ "\t" + "d4:B:S," + b4+ "\t" + "d5:B:S," + b5,file=fw1)

