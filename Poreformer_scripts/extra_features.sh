#!/bin/bash
meth_type=""
reference=""
forward_current=""
reference_rev=""
reversed_current=""

# 函数：显示帮助信息
function show_help {
    echo "Usage: $(basename $0) -meth_type <meth_type> -ref <reference.fa> -forward_current <current_file> -ref_rev <reference_rev> -reversed_current <current_file>"
}

# 解析命令行选项
while [ $# -gt 0 ]; do
  case "$1" in
    -h | --help )
        show_help
        exit 0
      ;;
	-meth_type )
        shift
        meth_type="$1"
      ;;
    -ref )
        shift
        reference="$1"
      ;;
    -forward_current )
        shift
        forward_current="$1"
      ;;
    -ref_rev )
        shift
        reference_rev="$1"
      ;;
	-reversed_current )
        shift
        reversed_current="$1"
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
if [ -z "$meth_type" ] || [ -z "$reference" ] || [ -z "forward_current" ] || [ -z "$reference_rev" ] || [ -z "$reversed_current" ]; then
    echo "Error: All parameters must be provided."
    show_help
    exit 1
fi
if [ $meth_type==6mA ];then
	python3 6mA_meth_pos.py $reference >6ma_forward_pos.txt
	python3 6mA_meth_pos.py $reference_rev >6ma_reversed_pos.txt
	python3 6mA_meth_pos_6.py $reference >6ma_forward_pos_6.txt
	python3 6mA_meth_pos_6.py $reference_rev >6ma_reversed_pos_6.txt
	grep -F -wf 6ma_forward_pos_6.txt $forward_current > 6mA_forward_current_6wei.txt
	grep -F -wf 6ma_reversed_pos_6.txt $reversed_current > 6mA_reversed_current_6wei.txt
	python3 kmeans_cluster_7.py 6mA_forward_current_6wei.txt $forward_current > 6mA_forward_current_kmeans_7.txt
	python3 kmeans_cluster_7.py 6mA_reversed_current_6wei.txt $reversed_current > 6mA_reversed_current_kmeans_7.txt
	python3 get_mean.py $forward_current 6ma_forward_pos.txt >all_6mA_forward_current_mean.txt
	python3 get_mean.py $reversed_current 6ma_reversed_pos.txt >all_6mA_reversed_current_mean.txt
	paste -d "," all_6mA_forward_current_mean.txt 6mA_forward_current_kmeans_7.txt >6mA_forward_current_mean_kmeans_7_6.txt
	paste -d "," all_6mA_reversed_current_mean.txt 6mA_reversed_current_kmeans_7.txt >6mA_reversed_current_mean_kmeans_7_6.txt
	cat 6mA_forward_current_mean_kmeans_7_6.txt 6mA_reversed_current_mean_kmeans_7_6.txt >all_6mA_reversed_current_mean_kmeans_7_6.txt
else
	python3 mC_meth_pos.py $reference >mC_forward_pos.txt
	python3 mC_meth_pos.py $reference_rev >mC_reversed_pos.txt
	python3 mC_meth_pos_5.py $reference >mC_forward_pos_5.txt
	python3 mC_meth_pos_5.py $reference_rev >mC_reversed_pos_5.txt
	grep -F -wf mC_forward_pos_5.txt $forward_current > mC_forward_current_5wei.txt
	grep -F -wf mC_reversed_pos_5.txt $reversed_current > mC_reversed_current_5wei.txt
	python3 kmeans_cluster_6.py $forward_current > mC_forward_current_kmeans_6.txt
	python3 kmeans_cluster_6.py $reversed_current > mC_reversed_current_kmeans_6.txt
	python3 get_mean.py $forward_current mC_forward_pos.txt >all_mC_forward_current_mean.txt
	python3 get_mean.py $reversed_current mC_reversed_pos.txt >all_mC_reversed_current_mean.txt
	paste -d "," all_mC_forward_current_mean.txt mC_forward_current_kmeans_6.txt >mC_forward_current_mean_kmeans_6_5.txt
	paste -d "," all_mC_reversed_current_mean.txt mC_reversed_current_kmeans_6.txt >mC_reversed_current_mean_kmeans_6_5.txt
	cat mC_forward_current_mean_kmeans_6_5.txt mC_reversed_current_mean_kmeans_6_5.txt >all_mC_reversed_current_mean_kmeans_6_5.txt
fi