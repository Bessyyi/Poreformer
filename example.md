Poreformer Run Example
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
## 2.1 Guppy Basecalling and Read Alignment to Reference Genome
First we will perform basecalling of our nanopore signal file using Guppy basecaller. It is possible to align the reads during basecalling or align the reads after basecalling. Both options are shown below. Since we need move table for our basecalled DNA sequences, we will use --moves_out while running Guppy, which will produce an aligned (Option A) or unaligned BAM file (Option B).
single_to_multi_fast5 --input_path ${INPUT_DIR}/BA_NAT --save_path ${INPUT_DIR}/BA_NAT_multi
single_to_multi_fast5 --input_path ${INPUT_DIR}/BA_WGA --save_path ${INPUT_DIR}/BA_WGA_multi

## Option A: Perform Read Alignment during Bascalling with Guppy
Guppy has the option to perform read alignment using minimap2 during basecalling if a reference FASTA file is provided as --align_ref option. This can be be helpful in reducing the number of steps needed to run.
