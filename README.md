# iBrus fuzzy front end
This repository hosts all the code examples generated while exploring different mesh libraries for fast implementation of boolean operations, collisions, etc. The focus is to find an efficient gemoetric calculation library based on C/C++/C*, that solves the iBurs problems efficiently.

## List of library explored:
1. [Trimesh](https://github.com/mikedh/trimesh)
2. [Vedo](https://github.com/marcomusy/vedo)
3. [Pymesh](https://github.com/PyMesh/PyMesh)

## The criterion to compare different libraries:

1. Possibility of using GPU or CPU, potentially their performance
2. Computational efficiency
3. Interface: if this package have a clear API or not
4. Flexibility: what's the effort to integrate them in iBrus.
5. Representing grains using point cloud vs meshes.
6. Integration easiness with iBrus.

## Mesh libraries compared against current iBrus implementation

| Simulation Scenario | iBrus | Pymesh | Trimesh |
| --- | --- | --- | --- |
| 1 grain cut 1 plane/1 grain intersect with 1 box | 10 ms | 0.004 ms | 4.49 ms |

| 25 grains cut 1 plane/25 grains difference with 1 box diff | 11.55 ms | 4.09 s | 71 s |

## Boolean operations performance comparison between libraries

To compare the boolean operation speed of different libraries, we designed an experiement, where a sqaure grid of n * n number of grain is generated to intersect 
with a primitive box that sits just beneath the grid. The size of the box is dependent on the size of the grid. The boolean opeartions taken place are:
1. Calculate the union of the grid of grains
2. Calculate the difference between the grid and the box. 

This test was run on different number of grains([Trimesh test script](libraries_explorations/trimesh_efficiency_test.py), [Pymesh test script](libraries_explorations/Pymesh_efficiency_test.py) and the runtime scaling effect is plotted in the following 2 plots:

[Trimesh_boolan operations runtime](libraries_explorations/Trimesh_grain_grid_runtime_scaling_bup.png)
[Pymesh boolean operations runtime](libraries_explorations/pymesh_grain_grid_runtime_scaling.png)

The detailed breakdown of the runtime can be find in [Trimesh runtime breakdown](libraries_exploratoins/trimesh_efficiency_test_output_time_bup.txt) and 
[Pymesh runtime breakdown](libraries_explorations/pymesh_efficiency_test_output_time.txt). Those files display in detail which functions consisted the most of runtime.


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
