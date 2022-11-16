# Welcome to the APEC 8222 (python) course repository!

Here you will find all of the information related to the Python-specific component of APEC 8222. 

## Installation

Pip installing Hazelbean will attempt to install required libraries, but many of these must be compiled for your computer. You can solve each one manually for your chosen opperating system, or you can use these Anaconda-based steps here:

- Install Mambaforge from https://github.com/conda-forge/miniforge#mambaforge
- For convenience, during installation, I select yes for "Add Mambaforge to my PATH environment Variable"
- (PC) Open the Miniforge Prompt (search for it in the start menu) or (Mac) just type "mamba init"
- Create a new mamba environment with the following commands (here it is named 8222env1):

```mamba create -n 8222env1 -c conda-forge```

- Activate the environment 
  
```mamba activate 8222env1```

- Install libraries using conda command: 

```mamba install -c conda-forge natcap.invest geopandas rasterstats netCDF4 cartopy xlrd markdown qtpy qtawesome plotly descartes pygeoprocessing taskgraph cython rioxarray dask google-cloud-datastore google-cloud-storage aenum anytree statsmodels openpyxl seaborn twine pyqt ipykernel imageio```

- And then finally, install hazelbean via pip:

```pip install mglearn datascience hazelbean```


## Numpy errors

If numpy throws "wrong size or changes size binary": upgrade numpy at the end of the installation process. See for details: https://stackoverflow.com/questions/66060487/valueerror-numpy-ndarray-size-changed-may-indicate-binary-incompatibility-exp

## Mac specific errors

Your python environment has to have permissions to access and write to the base data folder.


## License and acknowledgements.

For your convenience, I have included forks of our two textbooks in this repository. They are licensed under a creative-commons license that does not allow derivative works, so thus I leave them unmodified in their respective directories, but feel free to go to https://inferentialthinking.com and https://github.com/amueller/introduction_to_ml_with_python for the live versions of their course.
