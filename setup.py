from setuptools import setup, find_packages

setup(
    name="qgis_fmask",
    version="v3.0.2",
    description="Scripts for runnning Python Fmask in QGIS",
    author="Jonas Sølvsteen",
    author_email="josl@dhigroup.com",
    python_requires=">=3.6",
    packages=find_packages(exclude=["tests"]),
)
