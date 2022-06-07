<p align="center">
   <img align="center" src="https://github.com/Kraymer/__pub/raw/master/logo_cornerstone.png" width="200" >

[![nopypi](http://github.com/kraymer/cornerstone/workflows/build/badge.svg)](https://github.com/Kraymer/cornerstone/actions/workflows/python-build.yml)
[![nopypi](http://img.shields.io/pypi/v/cornerstone.svg)](https://pypi.python.org/pypi/cornerstone)
[![nopypi](https://codecov.io/gh/Kraymer/cornerstone/branch/main/graph/badge.svg?token=EPMJ5EZGIK)](https://codecov.io/gh/Kraymer/cornerstone)
[![](https://pepy.tech/badge/cornerstone)](https://pepy.tech/project/cornerstone)
[![nopypi](https://img.shields.io/badge/releases-atom-orange.svg)](https://github.com/Kraymer/cornerstone/releases.atom)
[![](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Kraymer/cornerstone/blob/master/LICENSE)
</p>


# cornerstone

> **/kɔrˈneːrston/**
>    
>    *n.* an indispensable and fundamental basis

``cornerstone`` is a state-of-the-art repository setup to start a python project hosted on Github.

## Features

- Markdown `README.md` file used for both pypi and github project homepages
- Markdown documentation hosted by readthedocs
- CI/CD automation using Github action :
   - `codecov.yml` upload coverage to Codecov
   - `python-build` lint and run unit tests
   - `python-semantic-release.yml` automatic changelog generation and versioning via Python Semantic Release and one click deployment to Pypi

## Install

~~~
git clone git@github.com:Kraymer/cornerstone.git YOUR_PROJECT
sed -i 's/cornerstone/YOUR_PROJECT/g' **/*setup*
~~~

Please read documentation for further instructions