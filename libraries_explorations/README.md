# Here are necessary infos to install the package properly and run it

## Pymesh
1. Doownload source code and record the repository of pymesh to the environment variable $PYMESH
`git clone https://github.com/PyMesh/PyMesh.git
cd PyMesh
git submodule update --init
export PYMESH_PATH=`pwd`
`

2. Install the *system dependencies*: https://pymesh.readthedocs.io/en/latest/installation.html. 
3. Navigate to the pymesh folder and build the package with the command 
`./setup.py build`
4. **After build, install it using setup.** : 
`./setup.up Install`

After this, try `import pymesh` in the python console. If it doesn't work:
1. Check if you run `setup.py install`
2. Check if you set the $PYMESH variable correctly.
3. Check if system dependencies and python dependencies are all installed.

It takes quite sometime to install all the system dependencies packages made in C++. So be patient


## Vedo
`pip install vedo`

## fcl & python-fcl
1. Since python-fcl doesn't support fcl 0.6.0 yet, which is the newset version of fcl. You need to install the fcl version 0.5.0 from source code (https://github.com/flexible-collision-library/fcl/releases/tag/0.5.0)
2. Make sure you installed all the required dependencies in https://github.com/BerkeleyAutomation/python-fcl and https://github.com/flexible-collision-library/fcl.

