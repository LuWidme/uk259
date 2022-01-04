## Install anaconda package manager

**(Important! Install anaconda in a path without spaces (« »))**

https://docs.anaconda.com/anaconda/install/

Help: https://medium.com/@GalarnykMichael/install-python-anaconda-on-windows-2020-f8e188f9a63d

_Be sure to select the option "Add Anaconda to my PATH environment variable" during installation_

Test your installation by running `conda -V`

## Clone GitHub-Repo

[GitHub Repo](https://github.com/LuWidme/uk259)

Navigate into the cloned directory.

## Install dependencies in an environment

Navigate to the cloned directory and run:

`conda env create --file environment.yml`

Activate environment:

`conda activate uk259`

The command prompt should have changed to something like this:

`(uk259) C:\Work\ÜKs\259>`

run:
`ipython kernel install --user --name=uk259_kernel`

Start **Visual Studio** in the current directory:

`code .`
