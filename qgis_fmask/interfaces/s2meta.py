import os
import fnmatch


def recursive_glob(rootdir, pattern="*"):
    matches = []
    for root, _, filenames in os.walk(rootdir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def find_xml_in_granule_dir(granuledir):
    pattern = os.path.join(granuledir, "*.xml")
    xmlfiles = recursive_glob(granuledir, pattern="*MTD*TL*.xml")
    if len(xmlfiles) != 1:
        raise RuntimeError(
            "Expecting exactly one XML file in granules dir. Found {} with pattern '{}'.".format(
                len(xmlfiles), pattern
            )
        )
    return xmlfiles[0]
