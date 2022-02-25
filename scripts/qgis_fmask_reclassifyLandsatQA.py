# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 09:15:47 2022

@author: rmgu
"""

from qgis.processing import alg
import numpy as np
from osgeo import gdal
from processing.tools import dataobjects

_clear_land_fmask = 0
_clear_water_fmask = 1
_cloud_shadow_fmask = 2
_snow_fmask = 3
_cloud_fmask = 4
_filled_fmask = 255


@alg(
    name="reclassifylandsatqa",
    label=alg.tr("Reclassify Landsat Quality Assesment image"),
    group="fmask",
    group_label=alg.tr("FMask"),
)
@alg.input(
    type=alg.FILE,
    name="qaImage",
    label="Landsat Level-2 QA_PIXEL file",
    optional=False,
)
@alg.input(
    type=alg.RASTER_LAYER_DEST, name="outputFile", label="Reclassified output image"
)
def reclassifyLandsatQa(instance, parameters, context, feedback, inputs):
    """Reclassify Landsat QA_PIXEL image to Fmask classes"""

    def check_bit_flag(flag_array, bitmask):
        return np.bitwise_and(qaRaster, bitmask).astype(bool)

    qaRasterFile = instance.parameterAsFile(parameters, "qaImage", context)
    feedback.setProgressText(qaRasterFile)
    qaRasterImage = gdal.Open(qaRasterFile)
    qaRaster = qaRasterImage.GetRasterBand(1).ReadAsArray()

    fmaskClassRaster = np.zeros(qaRaster.shape)

    # See https://www.usgs.gov/media/images/landsat-collection-2-pixel-quality-assessment-bit-index
    # for bit flags
    fmaskClassRaster[check_bit_flag(qaRaster, 64)] = _clear_water_fmask
    fmaskClassRaster[check_bit_flag(qaRaster, 128)] = _clear_land_fmask
    fmaskClassRaster[check_bit_flag(qaRaster, 1)] = _filled_fmask
    fmaskClassRaster[check_bit_flag(qaRaster, 14)] = _cloud_fmask
    fmaskClassRaster[check_bit_flag(qaRaster, 16)] = _cloud_shadow_fmask
    fmaskClassRaster[check_bit_flag(qaRaster, 32)] = _snow_fmask
    drv = gdal.GetDriverByName("GTiff")
    outputFile = instance.parameterAsFileOutput(parameters, "outputFile", context)
    outTif = drv.Create(
        outputFile,
        qaRasterImage.RasterXSize,
        qaRasterImage.RasterYSize,
        1,
        gdal.GDT_Int16,
    )
    outTif.SetProjection(qaRasterImage.GetProjection())
    outTif.SetGeoTransform(qaRasterImage.GetGeoTransform())
    outTif.GetRasterBand(1).WriteArray(fmaskClassRaster)

    outTif = None
    qaRasterImage = None
    dataobjects.load(outputFile, isRaster=True)
