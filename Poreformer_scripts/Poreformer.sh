#!/bin/bash
meth_type=""
feature=""

# 函数：显示帮助信息
function show_help {
    echo "Usage: $(basename $0) -meth_type <meth_type> -feature <feature_file>"
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
    -feature )
        shift
        -feature="$1"
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
if [ -z "$meth_type" ] || [ -z "$feature" ]; then
    echo "Error: All parameters must be provided."
    show_help
    exit 1
fi
if [ $meth_type==6mA ];then
	python3 6mA_model.py $feature 
else
	python3 mC_model.py $feature 
fi