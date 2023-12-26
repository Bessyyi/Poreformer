import fileinput
import sys
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]


dict1 = {}
for i in fileinput.input(files=(input_file1)):
    j = i.strip().split(':')
    a = 'pos'+j[0]
    dict1[a]=j[1]


for i in fileinput.input(files=(input_file2)):
    j = i.strip().split(',')
    if j[0] in dict1.keys():
        print(dict1[j[0]])
    else:
        print(0)
