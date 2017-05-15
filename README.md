# QGIS_python_fmask
QGIS interface to python-fmask

We want to make Python FMask available in QGIS.

Making the QGIS interface is easy. But FMask has to be built for the particular system.

The plan is to take the ready-built versions of [`python-fmask`](https://anaconda.org/conda-forge/python-fmask) and [`rios`](https://anaconda.org/conda-forge/rios) from `conda-forge` and just dump them somewhere in QGIS's PYTHONPATH.

Too bad QGIS is not using `conda`.
