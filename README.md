<p align="center">
   <img align="center" src="https://github.com/Kraymer/__pub/raw/master/logo_cornerstone.png" width="200" >

[![](http://github.com/kraymer/cornerstone/workflows/build/badge.svg)](https://github.com/Kraymer/cornerstone/actions/workflows/python-build.yml)
[![](http://img.shields.io/pypi/v/cornerstone.svg)](https://pypi.python.org/pypi/cornerstone)
[![](https://codecov.io/gh/Kraymer/cornerstone/branch/main/graph/badge.svg?token=EPMJ5EZGIK)](https://codecov.io/gh/Kraymer/cornerstone)
[![](https://pepy.tech/badge/cornerstone)](https://pepy.tech/project/cornerstone)
[![](https://img.shields.io/badge/releases-atom-orange.svg)](https://github.com/Kraymer/cornerstone/releases.atom)
[![](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Kraymer/cornerstone/blob/master/LICENSE)
</p>


# cornerstone

> **/kɔrˈneːrston/**
>    
>    *n.* an indispensable and fundamental basis

``cornerstone`` is a basic repository setup to start your python project.

## Features

- `README.rst` processing to make it compatible with pypi strict formatting rules
- `setup.py` fetches package infos dynamically
- CI/CD automation using Github action :
   - `codecov.yml` upload coverage to Codecov
   - `python-build` lint and run unit tests
   - `python-semantic-release.yml` automatic changelog generation and versioning via Python Semantic Release and one click deployment to Pypi
