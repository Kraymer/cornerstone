# cornerstone

> **/kɔrˈneːrston/**
>    
>    *n.* an indispensable and fundamental basis

``cornerstone`` is a state-of-the-art repository setup to start a python project hosted on Github.


## Install

~~~
git clone git@github.com:Kraymer/cornerstone.git YOUR_PROJECT
# git checkout docs
sed -i 's/cornerstone/YOUR_PROJECT/g' **/*py  
~~~

## Features

- Markdown `README.md` file used for both pypi and github project homepages
- Markdown documentation hosted by readthedocs
- CI/CD automation using Github action :
   - `codecov.yml` upload coverage to Codecov
   - `python-build` lint and run unit tests
   - `python-semantic-release.yml` automatic changelog generation and versioning via Python Semantic Release and one click deployment to Pypi
   
### README.md

PyPI.org supports Markdown in long descriptions in place of restructured text since April 2018.
This allows us to use the content of README.md as-is for the Pypi description, except for images having `ǹopypi` as _Alt text_ that will be discarded (eg see how [cornerstore pypi homepage](https://pypi.org/project/cornerstone/) has only two badges from the [six original ones](https://github.com/Kraymer/cornerstone)).

## Configuration

### Readthedocs alabaster theme

Import your project to your readthedocs account and set `docs` as default branch.  

### Github CI/CD workflows

- `codecov.yml`: import your project to your app.codecov.io/ account
- `python-buid.yml`: edit python versions and targeted platforms
- `python-semantic-release.yml`: add a PYPI_TOKEN secret token to your repository settings as described on [packaging.python.org](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/#saving-credentials-on-github). Configure behaviour by editing [`setup.cfg`](https://raw.githubusercontent.com/Kraymer/cornerstone/main/setup.cfg).



