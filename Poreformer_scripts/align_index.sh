#!/bin/bash
reference=""
fast5=""
other=""

# 函数：显示帮助信息
function show_help {
    echo "Usage: $(basename $0) -ref <reference.fa> -fast5 <fast5_file> -ref_rev <reference_rev>"
}

# 解析命令行选项
while [ $# -gt 0 ]; do
  case "$1" in
    -h | --help )
        show_help
        exit 0
      ;;
    -ref )
        shift
        reference="$1"
      ;;
    -fast5 )
        shift
        fast5="$1"
      ;;
    -ref_rev )
        shift
        reference_rev="$1"
      ;;
    * )
        echo "Error: Unknown option $1"
        show_help
        exit 1
      ;;
  esac
  shift
done

# 检查必需的参数是否已提供
if [ -z "$reference" ] || [ -z "$fast5" ] || [ -z "$other" ]; then
    echo "Error: All parameters must be provided."
    show_help
    exit 1
fi

python3 fast5_fastq.py $fast5
python3 fast5_dian.py $fast5 > $fast5.txt
minimap2 --secondary=no -ax map-ont $reference $fast5.fq > $fast5.sam
samtools view -F 256 -h $fast5.sam > $fast5_001.sam
samtools view -F 2048 -h $fast5001.sam > $fast5_002.sam
rm $fast5_001.sam
samtools view -F 16 $fast5_002.sam >$fast5_zheng003.txt
samtools view -F 16 -h $fast5_002.sam >$fast5_zheng003.sam
samtools view -f 16 $fast5.sam > $fast5_003.txt
cut -f 1 $fast5_zheng003.txt >$fast5_mulu_+.txt
grep -A 3 -F -f $fast5_mulu_+.txt $fast5.fq > $fast5_zheng.fq
cut -f 1 $fast5_003.txt > $fast5_mulu.txt
grep -A 3 -F -f $fast5_mulu.txt $fast5.fq > $fast5_fan.fq
python3 delet--.py $fast5_fan.fq > $fast5_fan1.fq
python3 delet--.py $fast5_zheng.fq >$fast5_zheng1.fq
rm $fast5_zheng.fq
rm $fast5_fan.fq
grep -F -f $fast5_mulu_+.txt $fast5.txt >$fast5_zheng.txt
grep -F -f $fast5_mulu.txt $fast5.txt > $fast5_fan.txt
minimap2 --secondary=no -ax map-ont $reference_rev $fast5_fan1.fq > $fast5_fan.sam
samtools view -F 256 -h $fast5_fan.sam > $fast5_fan001.sam
samtools view -F 2048 -h $fast5_fan001.sam > $fast5_fan002.sam
rm $fast5_fan001.sam
python3 dian_first_step.py $fast5_fan
python3 out-dianliu1.py $fast5_fan
python3 dian_first_step_zheng.py $fast5_zheng
python3 out-dianliu_zheng.py $fast5_zheng
sed 's/ /       /g' $fast5_fan.chuli.txt > $fast5_fan.chuli_fin.txt
paste $fast5_fan002.sam $fast5_fan.chuli_fin.txt >$fast5_fan_fin.sam
samtools view -F 16 -h $fast5_fan_fin.sam > $fast5_fan_fin+.sam
samtools view -Sb $fast5_fan_fin+.sam >$fast5_fan_fin+.bam
samtools sort $fast5_fan_fin+.bam > $fast5_fan_fin+_sort.bam
samtools index $fast5_fan_fin+_sort.bam
sed 's/ /       /g' $fast5_zheng.chuli.txt > $fast5_zheng.chuli_fin.txt
paste $fast5_zheng003.sam $fast5_zheng.chuli_fin.txt >$fast5_zheng_fin.sam
samtools view -Sb $fast5_zheng_fin.sam >$fast5_zheng_fin.bam
samtools sort $fast5_zheng_fin.bam >$fast5_zheng_fin_sort.bam
samtools index $fast5_zheng_fin_sort.bam

#使用pysam对bam文件进行整理输出
python3 step2_pysam_new.py $fast5_zheng_fin_sort.bam >$fast5_zheng_fin.txt
python3 step2_pysam_new.py $fast5_fan_fin+_sort.bam > $fast5_fan_fin+.txt
sort -n -k 2 $fast5_fan_fin+.txt > $fast5_fan_fin+_sort.txt 
sort -n -k 2 $fast5_zheng_fin.txt >$fast5_zheng_fin_sort.txt
python3 step3_reads_chuli.py $fast5_fan_fin+_sort.txt > $fast5_fan_fin+_sort1.txt
Python3 step4_reads_chuli.py $fast5_fan_fin+_sort1.txt >$fast5_fan_fin+_sort_fin.txt
python3 step3_reads_chuli.py $fast5_zheng_fin_sort.txt >$fast5_zheng_fin_sort1.txt
python3 step3_reads_chuli.py $fast5_zheng_fin_sort1.txt>$fast5_zheng_fin_sort_fin.txt
