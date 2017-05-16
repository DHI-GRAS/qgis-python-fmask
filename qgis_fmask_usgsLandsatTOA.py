#Definition of inputs and outputs
#==================================
##FMask=group
##Landsat TOA=name
##ParameterFile|infile|Input raw DN radiance image|False|False
##ParameterFile|mtl|.MTL file|False|False|MTL
##OutputFile|outfile|Output angles image file|tif

from argparse import Namespace
import sys
import os.path
import numpy as np

here = os.path.dirname(scriptDescriptionFile)
if here not in sys.path:
    sys.path.append(here)

from interfaces.fmask_usgsLandsatTOA import mainRoutine

cmdargs = Namespace(
        infile=infile,
        mtl=mtl,
        anglesfile=anglesfile,
        outfile=outfile)

with np.errstate(invalid='ignore'):
    mainRoutine(cmdargs)
