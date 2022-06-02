#!/usr/bin/env python3

# Copyright (c) 2022 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

import codecs
import os
import re
from setuptools import setup


PKG_NAME = "cornerstone"

# Extract module docstring and version from package root __init__.py
with codecs.open("{}/__init__.py".format(PKG_NAME), encoding="utf-8") as fd:
    metadata = fd.read()
    VERSION = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', metadata, re.MULTILINE
    ).group(1)
    DESCRIPTION = metadata.split('"""')[1].strip()


def read_rsrc(filename, pypi_compat=False):
    """Return content of given text file.
    If `.. pypi` comment if present then remove emojis in whole text and
    anything preceding the comment so that the .rst can be properly displayed
    on pypi.
    """
    with codecs.open(filename, encoding="utf-8") as _file:
        data = _file.read().strip()
        if pypi_compat or filename == "README.rst":
            if ".. pypi" in data:
                data = re.sub(r":(\w+\\?)+:", "", data[data.find(".. pypi") :] or data)
    return data


# Deploy: python3 setup.py sdist bdist_wheel; twine upload --verbose dist/*
setup(
    name=PKG_NAME,
    version=VERSION,
    description="",
    long_description=read_rsrc("README.rst"),
    author="Fabrice Laporte",
    author_email="kraymer@gmail.com",
    url=f"https://github.com/KraYmer/{PKG_NAME}",
    license="MIT",
    platforms="ALL",
    packages=[PKG_NAME],
    install_requires=read_rsrc("requirements.txt").split("\n"),
    python_requires=">=3.6",
    extras_require={
        "test": [
            "coverage>5",
            "pytest>=6",
            "tox>=3",
        ]
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="",
)
