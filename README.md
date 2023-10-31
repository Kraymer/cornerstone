<p align="center">
   <img align="center" src="https://github.com/Kraymer/__pub/raw/master/logo_cornerstone.png" width="200" >

[![nopypi](http://github.com/kraymer/cornerstone/workflows/build/badge.svg)](https://github.com/Kraymer/cornerstone/actions/workflows/python-build.yml)
[![](https://readthedocs.org/projects/cornerstone/badge/?version=latest)](http://cornerstone.readthedocs.org/en/latest/?badge=latest)
[![nopypi](https://codecov.io/gh/Kraymer/cornerstone/branch/main/graph/badge.svg?token=EPMJ5EZGIK)](https://codecov.io/gh/Kraymer/cornerstone)
[![nopypi](http://img.shields.io/pypi/v/cornerstone.svg)](https://pypi.python.org/pypi/cornerstone)
[![](https://pepy.tech/badge/cornerstone)](https://pepy.tech/project/cornerstone)
[![nopypi](https://img.shields.io/badge/releases-atom-orange.svg)](https://github.com/Kraymer/cornerstone/releases.atom)

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

## Getting started

Create a new repository using <kbd><br>**Use this template**<br><br></kbd> button then fork it and perform following edits locally :

~~~
mv cornerstone YOUR_PROJECT
sed -i 's/cornerstone/YOUR_PROJECT/g' **/*setup*
sed -i 's/cornerstone/YOUR_PROJECT/g' .github/workflows/*
truncate -s 0 CHANGELOG.md README.md
~~~

Please read [documentation](https://cornerstone.readthedocs.io/en/latest/) for further instructions.
