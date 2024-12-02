#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='seqtop',
    version='0.1',
    author='Adam Ewing',
    author_email='adam.ewing@gmail.com',
    description=("monitor sequencing from the command line because GUIs have too many pixels"),
    license='MIT',
    url='https://github.com/adamewing/seqtop',
    download_url='https://github.com/adamewing/seqtop/archive/refs/tags/0.1.tar.gz',
    scripts=['seqtop'],
    packages=find_packages(),
    install_requires = [
        'minknow-api',
        'plotext',
        'numpy',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

)
