## Poreformer
Identification of methylation for Nanopore DNA sequencing.

Poreformer is a computational tool for detecting DNA 5mC、4mC and 6mA methylation from Oxford Nanopore reads. It uses a Transfomer model to predict per-read and per-site 5mC、4mC and 6mA methylations and produces a methylation file. Poreformer can call methylation from FAST5 files basecalled with Guppy and provides models for R9.4.1 flowcells.
<p align="center"> <img src="https://github.com/Bessyyi/Poreformer/blob/main/img/model.png"  width="50%" > </p>


## Installation 
Please refer to [Installation](https://github.com/Bessyyi/Poreformer/blob/main/docs/install.md) for how to install Poreformer.

## Inference
#### Quick usage guide for model inference:

  1.To call modifications, the raw fast5 files should be basecalled by Guppy.
```
ont-guppy/bin/guppy_basecaller -i ${INPUT_DIR}/BA_NAT -s ${INPUT_DIR}/BA_NAT_guppy -c ont-guppy/data/dna_r9.4.1_450bps_hac.cfg -x cuda:all:100% -r --fast5_out
```
  2. Extract fastq and signal information from fast5 file and Align reads using minimap2 and then sort and index the BAM file
```
./align_index.sh -ref Bacillus_amyloliquefaciens.fa -fast5 ${INPUT_DIR}/BA_NAT_guppy/.fast5 -ref_rev Bacillus_amyloliquefaciens_rev.fa
```
  3. Extract features
```
```
