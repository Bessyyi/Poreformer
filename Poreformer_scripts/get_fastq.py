
import h5py
import csv
import numpy as np
import sys
in_filev1 = sys.argv[1]
with open(in_filev1+'.fq', 'w') as fw:
    writer = csv.writer(fw)
    f = h5py.File(in_filev1,'r')

    for read_id in f.keys():
        n=f[read_id+'/Analyses/']
        if "Basecall_1D_001" in n:
            fastq =f[read_id+'/Analyses/Basecall_1D_001/BaseCalled_template/Fastq'][()]
        else:
            fastq =f[read_id+'/Analyses/Basecall_1D_000/BaseCalled_template/Fastq'][()]
        read_id_id = fastq.decode('utf-8').split("\n")[0]

        xulie = fastq.decode('utf-8').split("\n")[1]
        zhiliang = fastq.decode('utf-8').split("\n")[3]
        fin_xulie =[]

        for i in range(0,len(xulie)):
            fin_xulie.append(xulie[i])

        read_id1 = read_id.split("_")
        # print(read_id1[1])
        print(read_id_id,file=fw)
        # print(read_id_id)
        a = "".join(fin_xulie)
        print(a,file=fw)
        print("+",file=fw)
        print(zhiliang,file=fw)
