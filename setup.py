"""
ColorPalette python modules.

Colin Page <cwpage@umich.edu>
"""

from setuptools import setup

setup(
    name='ColorPalette',
    version='0.1.0',
    packages=['ColorPalette'],
    include_package_data=True,
    install_requires=[
        'Pillow==9.0.1',
        'matplotlib==3.0.3',
        'scipy==1.3.1',
        'pandas==0.24.2',
        'click==6.7'
    ],
    entry_points={
        'console_scripts': [
            'colorpalette = ColorPalette.__main__:main',
        ]
    },
)

