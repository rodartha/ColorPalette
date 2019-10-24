"""
ColorPallete python modules.

Colin Page <cwpage@umich.edu>
"""

from setuptools import setup

setup(
    name='ColorPallete',
    version='0.1.0',
    packages=['ColorPallete'],
    include_package_data=True,
    install_requires=[
        'Pillow==6.2.1',
        'matplotlib==3.0.3',
        'scipy==1.3.1',
        'pandas==0.24.2'
    ],
)

