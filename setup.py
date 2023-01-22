from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'TOPSIS implementation'
LONG_DESCRIPTION = 'A package to perform TOPSIS function on Command-line arguments'

# Setting up
setup(
    name="Topsis-Diptesh-102003562",
    version=VERSION,
    author="Diptesh Mohanta",
    author_email="dmohanta_be20@thapar.edu",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy','pandas','sys'],
    keywords=['topsis','diptesh mohanta','python topsis'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)