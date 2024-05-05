## Conda Installation 
First, install Miniconda, a minimal installation of Anaconda, which is much smaller and has a faster installation:
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
Go through all the prompts (installation in $HOME is recommended). After Anaconda is installed successfully, simply run:
```
git clone https://github.com/Bessyyi/Poreformer.git
conda env create -f Poreformer/environment.yml
conda activate Poreformer
```
After installing, run python Poreformer/poreformer --help to see the run options.
