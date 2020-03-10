import os
import fnmatch

from .buildvrt import buildvrt


def recursive_glob(rootdir, pattern="*"):
    matches = []
    for root, _, filenames in os.walk(rootdir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def create_sentinel_stack(granuledir, outfile):
    infiles = []
    for fnpattern in ["*_B0[1-8].jp2", "*_B8A.jp2", "*_B09.jp2", "*_B1[0-2].jp2"]:
        bandfiles = recursive_glob(rootdir=granuledir, pattern=fnpattern)
        if not bandfiles:
            raise RuntimeError("No files found for pattern '{}'.".format(fnpattern))
        infiles += bandfiles
    buildvrt(
        infiles, outfile, resolution="user", separate=True, extra=["-tr", "20", "20"]
    )
