import sys
in_file=sys.argv[1]
with open (in_file) as f:
    m=""
    for i in f:
        m+=i
with open("6mA_forward_pos.txt","w") as fw,open("6mA_forward_pos_6.txt")as fw1:
    for pos in range(6,len(m)-6,12):
        if m[pos] =="A":
			print("pos"+str(pos),file=fw)
            for n1 in range(6,0,-1):
                print("pos"+str(pos-n1),file=fw1)
            for n2 in range(6):
                print("pos"+str(pos+n2),file=fw1)