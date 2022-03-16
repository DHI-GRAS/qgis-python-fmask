import os
import fnmatch

import sys

if os.path.dirname(__file__) not in sys.path:
    sys.path.append(os.path.dirname(__file__))
import buildvrt as bv

from fmask.cmdline import sentinel2Stacked


def recursive_glob(rootdir, pattern="*"):
    matches = []
    for root, _, filenames in os.walk(os.path.join(rootdir, "IMG_DATA")):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def create_sentinel_stack(safedir, outfile):
    granuledir = sentinel2Stacked.findGranuleDir(safedir)
    infiles = []
    for fnpattern in ["*_B0[1-8].jp2", "*_B8A.jp2", "*_B09.jp2", "*_B1[0-2].jp2"]:
        bandfiles = recursive_glob(rootdir=granuledir, pattern=fnpattern)
        if not bandfiles:
            raise RuntimeError("No files found for pattern '{}'.".format(fnpattern))
        infiles += bandfiles
    bv.buildvrt(
        infiles, outfile, resolution="user", separate=True, extra=["-tr", "20", "20"]
    )
