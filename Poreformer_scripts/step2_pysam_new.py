import sys
import pysam


in_filev1 = sys.argv[1]


samfile = pysam.AlignmentFile(in_filev1, "rb")
while True:
    try:
        reads1 = next(samfile)
        pre_pos_pair=reads1.get_aligned_pairs(matches_only=True)
        pos_pair=[j for j in pre_pos_pair]
        #reads1 = next(samfile)
        real_m = len(pos_pair)
        all_long = reads1.query_length
        identiy = real_m / all_long
        pair=reads1.cigartuples
        if identiy >= 0.75 and reads1.query_alignment_length >=50:
            #pre_pos_pair=reads1.get_aligned_pairs(matches_only=True)
            #pos_pair=[j for j in pre_pos_pair if reads1.seq[j[0]]==base]
            reads_pos=[int(i[0]) for i in pos_pair]
            ref_pos=[i[1]+1 for i in pos_pair]
            d1 = [reads1.get_tag('d1')[j] for j in reads_pos]
            d2 = [reads1.get_tag('d2')[j] for j in reads_pos]
            d3 = [reads1.get_tag('d3')[j] for j in reads_pos]
            d4 = [reads1.get_tag('d4')[j] for j in reads_pos]
            d5 = [reads1.get_tag('d5')[j] for j in reads_pos]
            reads_seq1 = [reads1.seq[j] for j in reads_pos]
            for m in range(len(ref_pos)):
                print(reads_seq1[m],ref_pos[m],d1[m],d2[m],d3[m],d4[m],d5[m])
    except StopIteration:
        break






