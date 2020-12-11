# iBrus fuzzy front end
This repository hosts all the code examples generated while exploring different mesh libraries for fast implementation of boolean operations, collisions, etc. The focus is to find an efficient gemoetric calculation library based on C/C++/C*, that solves the iBurs problems efficiently.

## List of library explored:
1. [Trimesh](https://github.com/mikedh/trimesh)
2. [Vedo](https://github.com/marcomusy/vedo)
3. [Pymesh](https://github.com/PyMesh/PyMesh)




## Notes, Tips, tricks and helpful links to check out for different packges
### Pymesh

### Trimesh
1. Trimesh user [suggestions](https://github.com/mikedh/trimesh/blob/master/trimesh/exchange/README.md) on mesh operations. 
2. Boolean operation issue on Trimesh suggest boolean is not very fast on trimesh and operation engine is [unreliable](https://github.com/mikedh/trimesh/issues/519#issuecomment-517552680) and [slow](https://github.com/mikedh/trimesh/issues/401#issuecomment-486904909).

## Package Installation Guide
### Pymesh
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


### Vedo
`pip install vedo`

### fcl & python-fcl
1. Since python-fcl doesn't support fcl 0.6.0 yet, which is the newset version of fcl. You need to install the fcl version 0.5.0 from source code (https://github.com/flexible-collision-library/fcl/releases/tag/0.5.0)
2. Make sure you installed all the required dependencies in https://github.com/BerkeleyAutomation/python-fcl and https://github.com/flexible-collision-library/fcl.


### trimesh
1. `pip install trimesh`
2. `pip install Rtree`, this is a soft dependencies neeeded.
3. When you need the boolean engine, you need to install `blender` or `openscad` using your system package manager. 
