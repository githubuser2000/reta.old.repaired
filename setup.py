#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="reta",
    version="0.5.0",
    description="Religions-Tabelle",
    author="Jupiter 3.0 alias trace",
    packages=find_packages(include=["reta.py"]),
    install_requires=[
        "html2text>=2020.1.16",
        "bbcode==1.1.0",
        "pyphen>=0.9.5",
        "PyHyphen>=3.0.1",
    ],
    package_data={".": ["*.txt", "*.csv",]},
)
