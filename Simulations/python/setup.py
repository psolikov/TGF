#!/usr/bin/python
"""
"""
import setuptools

setuptools.setup(
    name="chibis",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'tables',
        'tabulate',
        'protobuf<=3.20'
    ]
)
