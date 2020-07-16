#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="reta",
    version="0.5.0",
    packages=find_packages(include=["readme.txt", "setup.py", "reta.py", ".csv"]),
    install_requires=["html2text>=2020.1.16", "bbcode==1.1.0", "pyphen>=0.9.5",],
)
