# Installation 
#### First, install Miniconda, a minimal installation of Anaconda, which is much smaller and has a faster installation:
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
#### Go through all the prompts (installation in $HOME is recommended). After Anaconda is installed successfully, simply run:
```
git clone https://github.com/Bessyyi/Poreformer.git
conda env create -f Poreformer/environment.yml
conda activate Poreformer
```
#### download ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz (or newer version) and set HDF5_PLUGIN_PATH
```
wget https://github.com/nanoporetech/vbz_compression/releases/download/v1.0.1/ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz
tar zxvf ont-vbz-hdf-plugin-1.0.1-Linux-x86_64.tar.gz
export HDF5_PLUGIN_PATH=/abslolute/path/to/ont-vbz-hdf-plugin-1.0.1-Linux/usr/local/hdf5/lib/plugin
```
#### Download Guppy basecaller
```
wget -qO- https://cdn.oxfordnanoportal.com/software/analysis/ont-guppy_4.5.4_linux64.tar.gz| tar xzf - -C ${INPUT_DIR}
```
After installing, run python Poreformer/poreformer --help to see the run options.
