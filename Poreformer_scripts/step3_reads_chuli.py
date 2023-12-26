#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 9:59
# @Author  : YZY
# @FileName: step3_red_chuli.py
# @Software: PyCharm



import fileinput
import sys

in_filev1 = sys.argv[1]

dict1 ={}
m = 0
list1 = []
# for i in fileinput.input(files=('test.txt')):
for i in fileinput.input(files=(in_filev1)):
    j = i.strip().split(' ')

# #     print(j)
# #     if j[1] in dict1.keys():
# #         dict1[j[1]].append(j)
# #     else:
# #         dict1[j[1]] = []
# #         dict1[j[1]].append(j)
# # print(dict1)
    if int(j[1]) == m:
        list1.append([j[2],j[3],j[4],j[5],j[6]])
        list2.append(j[0])

    else:
        if list1 != []:
            a = max(list2, key=list2.count)
            list1.insert(1,a)
            print(list1)
        list1 = []
        list2 = []
        list1.append(j[1])
        list2.append(j[0])
        list1.append([j[2], j[3], j[4], j[5], j[6]])
        m +=1



