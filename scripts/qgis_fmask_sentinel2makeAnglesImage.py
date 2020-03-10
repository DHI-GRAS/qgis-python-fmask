# Definition of inputs and outputs
# ==================================
##FMask=group
##Sentinel 2 Make Angles Image=name
##ParameterFile|infile|Input sentinel-2 tile metafile|False|False|xml
##OutputFile|outfile|Output angles image file|tif

from argparse import Namespace
import numpy as np

from qgis_fmask.interfaces.fmask_sentinel2makeAnglesImage import mainRoutine

cmdargs = Namespace(infile=infile, outfile=outfile)

with np.errstate(invalid="ignore"):
    mainRoutine(cmdargs)
