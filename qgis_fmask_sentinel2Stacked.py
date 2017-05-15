#Definition of inputs and outputs
#==================================
##FMask=group
##Sentinel 2 Stacked=name
##ParameterFile|toa|Input stack of TOA reflectance (as supplied by ESA)|False|False|tif
##ParameterFile|anglesfile|Input angles file containing satellite and sun azimuth and zenith|False|False|
##OutputFile|output|Output cloud mask|tif
##*ParameterBoolean|verbose|verbose output|False
##*ParameterBoolean|keepintermediates|Keep intermediate temporary files (normally deleted)|False
##*ParameterFile|tempdir|Temp directory to use (default: same as infile)|True|True
##ParameterNumber|mincloudsize|Mininum cloud size (in pixels) to retain, before any buffering|0|None|0
##ParameterNumber|cloudbufferdistance|Distance (in metres) to buffer final cloud objects|0|None|150
##ParameterNumber|shadowbufferdistance|Distance (in metres) to buffer final cloud shadow objects|0|None|300
##ParameterNumber|cloudprobthreshold|Cloud probability threshold (percentage) (Eqn 17)|0|100|20
##ParameterNumber|nirsnowthreshold|Threshold for NIR reflectance for snow detection (Eqn 20). Increase this to reduce snow commission errors|0|1|0.11
##ParameterNumber|greensnowthreshold|Threshold for Green reflectance for snow detection (Eqn 20). Increase this to reduce snow commission errors|0|1|0.1

from argparse import Namespace
import sys
import os.path

here = os.path.dirname(scriptDescriptionFile)
if here not in sys.path:
    sys.path.append(here)

from interfaces.fmask_sentinel2Stacked import mainRoutine

cmdargs = Namespace(
        toa=toa,
        anglesfile=anglesfile,
        output=output,
        verbose=verbose,
        keepintermediates=keepintermediates,
        tempdir=tempdir,
        mincloudsize=mincloudsize,
        cloudbufferdistance=cloudbufferdistance,
        shadowbufferdistance=shadowbufferdistance,
        cloudprobthreshold=cloudprobthreshold,
        nirsnowthreshold=nirsnowthreshold,
        greensnowthreshold=greensnowthreshold)

mainRoutine(cmdargs)
