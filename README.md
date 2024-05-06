## Poreformer
Identification of methylation for Nanopore DNA sequencing.

Poreformer is a computational tool for detecting DNA 5mC、4mC and 6mA methylation from Oxford Nanopore reads. It uses a Transfomer model to predict per-read and per-site 5mC、4mC and 6mA methylations and produces a methylation file. Poreformer can call methylation from FAST5 files basecalled with Guppy and provides models for R9.4.1 flowcells.
<p align="center"> <img src="https://github.com/WGLab/DeepMod2/assets/35819083/e0ef0b41-a469-427d-abaa-af2ba6292809"  width="50%" > </p>
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
## Quick start
```
# 1.To call modifications, the raw fast5 files should be basecalled by Guppy. At last, modifications of specified motifs can be called by poreformer.

ont-guppy/bin/guppy_basecaller -i ${INPUT_DIR}/BA_NAT -s ${INPUT_DIR}/BA_NAT_guppy -c ont-guppy/data/dna_r9.4.1_450bps_hac.cfg -x cuda:all:100% -r --fast5_out

# 2. extract fastq and signal information from fast5 file and Align reads using minimap2 and then sort and index the BAM file

./align_index.sh -ref Bacillus_amyloliquefaciens.fa -fast5 ${INPUT_DIR}/BA_NAT_guppy/.fast5 -ref_rev Bacillus_amyloliquefaciens_rev.fa
# 3. extract features

```
