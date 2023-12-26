#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 9:36
# @Author  : YZY
# @FileName: dian_first_step.py
# @Software: PyCharm
import fileinput
import numpy as np
import ast

import sys
in_filev1 = sys.argv[1]
with open(in_filev1+'001.txt', 'w') as fw:
    for i in fileinput.input(files=(in_filev1+'.txt')):
        d0 = []
        d1 = []
        d2 = []
        d3 = []
        d4 = []
        d5 = []
        # print(i)
        j = i.strip().split(' ')
        # print(j)
        # print(len(j))
        dian = j[2].strip().split(';')
        # print(dian[-1])
        for event in dian:
            d = event.strip().split(',')
            # print(len(d))
            # print(d)
            # print(len(d))
            # if len(d) % 5 != 0:
            #     print("error")
            #     print(len(d))
            # else:
            #     print(0)
            x1 = []
            x2 = []
            x3 = []
            x4 = []
            x5 = []
            for m1 in range(0,len(d),5):
                #x1 = []
                # print(d[m1])
                x1.append(int(d[m1]))
            d1.append(str(int(np.mean(x1))))
            #print(x1)
            for m2 in range(1,len(d),5):
                #x2 = []
                # print(d[m2])
                x2.append(int(d[m2]))
            d2.append(str(int(np.mean(x2))))
            for m3 in range(2,len(d),5):
                #x3 = []
                # print(d[m3])
                x3.append(int(d[m3]))
            d3.append(str(int(np.mean(x3))))
            for m4 in range(3,len(d),5):
                #x4 = []
                # print(d[m4])
                x4.append(int(d[m4]))
            d4.append(str(int(np.mean(x4))))
            for m5 in range(4,len(d),5):
                #x5 = []
                # print(d[m5])
                x5.append(int(d[m5]))
            d5.append(str(int(np.mean(x5))))
        d0.append(j[0])
        d0.append(d1)
        d0.append(d2)
        d0.append(d3)
        d0.append(d4)
        d0.append(d5)
        #print(d0)
        print(d0,file=fw)
