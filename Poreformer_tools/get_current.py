import numpy
import sys
import h5py
import re
import csv

in_filev1 = sys.argv[1]
# out_file1 = sys.argv[2]

f = h5py.File(in_filev1,'r')

for read_id in f.keys():
    rid = read_id.split("_")[1]
    n=f[read_id+'/Analyses/']
    if "Basecall_1D_001" in n:
        basecall_1d_template = f[read_id+'/Analyses/Basecall_1D_001/Summary/basecall_1d_template']
        segmentation = f[read_id+'/Analyses/Segmentation_001/Summary/segmentation']
        move = f[read_id+'/Analyses/Basecall_1D_001/BaseCalled_template/Move'][()]
    else:
        basecall_1d_template = f[read_id+'/Analyses/Basecall_1D_000/Summary/basecall_1d_template']
        segmentation = f[read_id+'/Analyses/Segmentation_000/Summary/segmentation']
        move = f[read_id+'/Analyses/Basecall_1D_000/BaseCalled_template/Move'][()]        
    block_stride = basecall_1d_template.attrs['block_stride']
    first = segmentation.attrs['first_sample_template']
    raw = list(f[read_id+'/Raw'].values())[0]

    moveindex=numpy.nonzero(move)
    mark=0
    print(rid,block_stride,end=": ")
    for i in moveindex[0]:
        if i>0:
            start_raw_index = first + moveindex[0][mark-1] * block_stride
            end_raw_index = first + moveindex[0][mark] * block_stride
            print(*raw[int(start_raw_index):int(end_raw_index)],sep=',',end=";")
            if i==moveindex[0][-1]:
                start_raw_index = first + moveindex[0][mark] * block_stride
                end_raw_index = first + len(move) * block_stride
                print(*raw[int(start_raw_index):int(end_raw_index)],sep=',')
        mark+=1

f.close()
