# cornerstone

> **/kɔrˈneːrston/**
>    
>    *n.* an indispensable and fundamental basis

``cornerstone`` is a state-of-the-art repository setup to start a python project hosted on Github.



## Install

~~~
git clone git@github.com:Kraymer/cornerstone.git YOUR_PROJECT
sed -i 's/cornerstone/YOUR_PROJECT/g' **/*setup*
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
This allows us to use the content of README.md as-is for the Pypi description, except for images that have `ǹopypi` as _Alt text_ and will be discarded (eg see how [cornerstore pypi homepage](https://pypi.org/project/cornerstone/) has only two badges from the [six original ones](https://github.com/Kraymer/cornerstone)).
