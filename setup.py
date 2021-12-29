"""
LabPals python package configuration.

Hasan Saeed <hsaeedx@umich.edu>
"""

from setuptools import setup

setup(
    name='labpals',
    version='0.0.1',
    packages=['labpals'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
    ],
    python_requires='>=3.6',
)
