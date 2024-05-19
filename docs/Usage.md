## Poreformer Usage
## 1. Methylation Calling from FAST5 files with Guppy basecalling
Prepare Directories
```
INPUT_DIR=data
OUTPUT_DIR=mod

mkdir -p ${INPUT_DIR}
mkdir -p ${OUTPUT_DIR}
```
Download Software Packges
```
# Install Poreformer
git clone https://github.com/Bessyyi/Poreformer.git ${INPUT_DIR}/Poreformer
conda env create -f ${INPUT_DIR}/Poreformer/docs/environment.yml
conda activate Poreformer
conda install samtools minimap2 -y

# download ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz (or newer version) and set HDF5_PLUGIN_PATH
wget https://github.com/nanoporetech/vbz_compression/releases/download/v1.0.1/ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz
tar zxvf ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz
export HDF5_PLUGIN_PATH=/abslolute/path/to/ont-vbz-hdf-plugin-1.0.1-Linux/usr/local/hdf5/lib/plugin

# Download Guppy basecaller
wget -qO- https://cdn.oxfordnanoportal.com/software/analysis/ont-guppy_4.5.4_linux64.tar.gz| tar xzf - -C ${INPUT_DIR}
```
Download Nanopore data and reference genome
```
# Download reference genome
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/007/827/165/GCA_007827165.1_ASM782716v1/GCA_007827165.1_ASM782716v1_genomic.fna.gz -O -| gunzip -c > ${INPUT_DIR}/Bacillus_amyloliquefaciens.fa
# Download FAST5 files
mkdir -p ${INPUT_DIR}/nanopore_raw_data

wget -qO- https://sra-pub-src-1.s3.amazonaws.com/SRR10032566/MinION_BA_WGA.tar.gz.1| tar xzf - -C ${INPUT_DIR}/BA_WGA
wget -qO- https://sra-pub-src-2.s3.amazonaws.com/SRR10032567/MinION_BA_NAT.tar.gz.1| tar xzf - -C ${INPUT_DIR}/BA_NAT
```
## 2. Reference Anchored Methylation Calling
First we will perform basecalling of our nanopore signal file using Guppy basecaller. It is possible to align the reads during basecalling or align the reads after basecalling. Both options are shown below. Since we need move table for our basecalled DNA sequences.
## 2.1 Guppy Basecalling using GPU
If the fast5 files are in single-read FAST5 format, please use single_to_multi_fast5 command from the [ont_fast5_api](https://github.com/nanoporetech/ont_fast5_api) package to convert the fast5 files before using Guppy.
## This script converts folders containing single_read_fast5 files into multi_read_fast5 files:
```
single_to_multi_fast5 --input_path ${INPUT_DIR}/BA_NAT --save_path ${INPUT_DIR}/BA_NAT_multi
single_to_multi_fast5 --input_path ${INPUT_DIR}/BA_WGA --save_path ${INPUT_DIR}/BA_WGA_multi
```
## Guppy Basecalling
Guppy has the option to perform read alignment using minimap2 during basecalling if a reference FASTA file is provided as --align_ref option. This can be be helpful in reducing the number of steps needed to run.
```
ont-guppy/bin/guppy_basecaller -i ${INPUT_DIR}/BA_NAT -s ${INPUT_DIR}/BA_NAT_guppy -c ont-guppy/data/dna_r9.4.1_450bps_hac.cfg -x cuda:all:100% -r --fast5_out
ont-guppy/bin/guppy_basecaller -i ${INPUT_DIR}/BA_WGA -s ${INPUT_DIR}/BA_WGA_guppy -c ont-guppy/data/dna_r9.4.1_450bps_hac.cfg -x cuda:all:100% -r --fast5_out
```
## 2.2 extract signal and location
```
#extract fastq and signal information from fast5 file and Align reads using minimap2 and then sort and index the BAM file
./align_index.sh -ref Bacillus_amyloliquefaciens.fa -fast5 ${INPUT_DIR}/BA_NAT_guppy/.fast5 -ref_rev Bacillus_amyloliquefaciens_rev.fa
```
## 3. Extract features
Features of targeted sites can be extracted for training or testing.

For the example data
```
sh extra_feature.sh -ref Bacillus_amyloliquefaciens.fa -forward_current all_zheng_fin_sort_fin.txt -ref_rev Bacillus_amyloliquefaciens_rev.fa -reversed_current all_fan_fin_sort_fin.txt
```
## 4. Methylation Calling with Poreformer
```
sh Poreformer.sh -meth_type mC -feature all_mC_reversed_current_mean_kmeans_6_5.txt
sh Poreformer.sh -meth_type 6mA -feature all_6mA_reversed_current_mean_kmeans_7_6.txt

```
