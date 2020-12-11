# Here stores the developer's note while exploring the mesh libraries.

## Nov. 30 - Dec 4th
1. rtree is needed for using blender engine and boolean operations in trimesh.
2. 


## Dec. 7th, searching for mesh libraries that is related to trimesh or more efficient on boolean calculations
Candidate:

1. Vedo,  https://github.com/marcomusy/vedo/tree/af7553dc04283e001cb03f910cfaf00f4682eb86
boolean based on VTK. [! VTK]:https://vtk.org/doc/nightly/html/classvtkBooleanOperationPolyDataFilter.html

2. Libigl: https://github.com/libigl
https://libigl.github.io/tutorial/

3. CGAL  https://www.cgal.org/  The problem is this might be too heavy
https://doc.cgal.org/latest/Mesh_3/Mesh_3_2mesh_3D_image_8cpp-example.html


4. Meshlab: https://www.meshlab.net/#references
https://github.com/cnr-isti-vclab/PyMeshLab



## Dec. 10
## To complete the library comparison, more test scenario should be done both in Trimesh and pymesh

By far we explored mainly mesh to mesh intersection and both were very slow. 
However, there are alternative ways to represents the grains and workpiece.

1. Trimesh: do a test with a grain mesh intersecting with a plane representing workpiece.

2. Trimesh: try representing the grain with point cloud and do a intersection with mesh plane. 

3. Pymesh: try intersecting the grain with a polygon


