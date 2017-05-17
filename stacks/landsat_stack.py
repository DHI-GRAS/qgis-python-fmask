import os
import glob

from .buildvrt import buildvrt


bandfile_patterns = {
        'ref': 'LC8*_B[1-7,9].TIF',
        'thermal': 'LC8*_B1[0,1].TIF'}


def create_landsat_stack(productdir, outfile, patternkey):
    pattern = os.path.join(productdir, bandfile_patterns[patternkey])
    infiles = sorted(glob.glob(pattern))
    if not infiles:
        raise RuntimeError('No files found for pattern \'{}\'.'.format(pattern))
    buildvrt(infiles, outfile, separate=True)
