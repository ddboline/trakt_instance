#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:29:26 2015

@author: ddboline
"""
import sys
from setuptools import setup

v = sys.version_info.major

setup(
    name='trakt_instance',
    version='0.0.3',
    author='Daniel Boline',
    author_email='ddboline@gmail.com',
    description='Wrapper around trakt.py',
    long_description='Trakt Instance',
    license='MIT',
    install_requires=['trakt.py'],
    packages=['trakt_instance'],
    package_dir={'trakt_instance': 'trakt_instance'},
    # package_data={'sync_app': ['templates/*.html']},
    # entry_points={
    #     'console_scripts': console_scripts
    # }
)
