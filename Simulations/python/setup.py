#!/usr/bin/python
"""
"""
import setuptools

setuptools.setup(
    name="phd",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'tables',
        'tabulate'
    ]
)
