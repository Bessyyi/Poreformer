#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 15:21
# @Author  : YZY
# @FileName: qu_mean.py
# @Software: PyCharm
import fileinput
import numpy as np
import sys
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]


dict1 = {}
for i in fileinput.input(files=(input_file1)):
    j = i.strip().split(',')
    m = j[0].split('pos')[1]
    # print(m)
    # print(j)
    j1 = [int(ii) for ii in j[2].split("-")]
    # print(j1)
    j2 = [int(ii) for ii in j[3].split("-")]
    j3 = [int(ii) for ii in j[4].split("-")]
    j4 = [int(ii) for ii in j[5].split("-")]
    j5 = [int(ii) for ii in j[6].split("-")]
    jn1 = np.mean(j1).round(3)
    jn2 = np.mean(j2).round(3)
    jn3 = np.mean(j3).round(3)
    jn4 = np.mean(j4).round(3)
    jn5 = np.mean(j5).round(3)
    dict1[m] = np.mean([jn1,jn2,jn3,jn4,jn5]).round(3)
    # print(j[0],j[1],jn1,jn2,jn3,jn4,jn5)

    # print(dict1)
# h = 0
list1 = []
dict2 ={}
for i in fileinput.input(files=(input_file2)):
    j = i.strip().split('pos')[1]
    dict2[j]= []
    for m in range(int(j) - 11, int(j) + 12):
        #dict2[j].append(dict1[str(m)])
        if str(m) in dict1.keys():
            a = dict1[str(m)]
            #print(a)
            dict2[j].append(str(a))
#print(dict2)
for i in dict2.keys():
    a = ','.join(dict2[i])
    print(i+':'+a)
