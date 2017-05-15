#Definition of inputs and outputs
#==================================
##FMask=group
##Sentinel 2 Stacked=name
##ParameterFile|granulesdir|Directory of target granule|True|False
##ParameterFile|anglesfile|Input angles file containing satellite and sun azimuth and zenith|False|False|
##OutputFile|output|Output cloud mask|tif
##*ParameterBoolean|verbose|verbose output|True
##*ParameterBoolean|keepintermediates|Keep intermediate temporary files (normally deleted)|False
##*ParameterFile|tempdir|Temp directory to use (default: same as infile)|True|True
##ParameterNumber|mincloudsize|Mininum cloud size (in pixels) to retain, before any buffering|0|None|0
##ParameterNumber|cloudbufferdistance|Distance (in metres) to buffer final cloud objects|0|None|150
##ParameterNumber|shadowbufferdistance|Distance (in metres) to buffer final cloud shadow objects|0|None|300
##ParameterNumber|cloudprobthreshold|Cloud probability threshold (percentage) (Eqn 17)|0|100|20
##*ParameterNumber|nirsnowthreshold|Threshold for NIR reflectance for snow detection (Eqn 20). Increase this to reduce snow commission errors|0|1|0.11
##*ParameterNumber|greensnowthreshold|Threshold for Green reflectance for snow detection (Eqn 20). Increase this to reduce snow commission errors|0|1|0.1

from argparse import Namespace
import sys
import os.path
import tempfile
import shutil
from processing.tools import dataobjects

here = os.path.dirname(scriptDescriptionFile)
if here not in sys.path:
    sys.path.append(here)

from stacks.sentinel_stack import create_sentinel_stack
from interfaces.fmask_sentinel2Stacked import mainRoutine
from interfaces.redirect_print import redirect_print

cmdargs = Namespace(
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


tempdir = tempfile.mkdtemp()
try:
    progress.setConsoleInfo('Creating Sentinel 2 band stack VRT file ...')
    tempvrt = os.path.join(tempdir, 'temp.vrt')
    create_sentinel_stack(granulesdir, outfile=tempvrt)
    progress.setConsoleInfo('Done.')
    cmdargs.toa = tempvrt
    progress.setConsoleInfo('Running FMask (this may take a while) ...')
    with redirect_print(progress):
        mainRoutine(cmdargs)
finally:
    try:
        shutil.rmtree(tempdir)
    except OSError:
        pass

progress.setConsoleInfo('Done.')
dataobjects.load(output, os.path.basename(output))
