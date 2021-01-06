# Summary of progress in the literature search

The problem we are facing at iBurs is to find an efficient, fast and robust way to generate the work piece representation, which is cut by grains iteratively. Our target resolution is to model a 100 mm * 100 mm workpiece, with resolution of 0.1 mm. and the computation should be done on the scale of micro second. However, at the moment we haven't find a efficient library which meets our needs.

So it's necessary to do some research and understand how things are being down in the field of solid geometry processing. 

## Typical data structure and their application area. 

1. BVH: bounding volume hierarchy, which divides a 3D volume in small parts until its primitive(?). BVH is widely used in collision detection, by traversal through notes/leafs of hierarchy to extract exact notes that’s in collision with each other.

2. BSP: binary space partition: another way of dividing 3D geometry, but different from BVH. There is a discussion on stack overflow talking about this. It looks like BSP is more applied in mesh Boolean operations. For example, Libigl paper was using BSP as well.

On top of these basic principle, there is also CSG tree and Octree 

1. CSGtree: constructive soils geometry is widely used in CAD programming to construct complicated geometry shape by doing several Boolean operations with primitive shape. It’s optimized for generating complex shape while doing lots of Boolean operations, an example literature in this is: QuickCSG tree.
 
CSGtree is generally faster on a series of Boolean operations, compared to meshes. There is also a field focusing on generating CSGtree from 3D meshes called inverse CSGtree. MIT has a paper on this topic.

3. Octree is another data structure that is similar to BVH. I am not sure yet if it’s exactly a variant of BVH. Octree seems widely applied in lots of optimized algorithms for speed and robust purposes: Libigl is using it, GPU-Voxel is using it as well.

## Triangle or Voxel: which is faster 

Since the library we explored in 2020 all used the above mentioned algorithms and library, yet they are not fast enough on the calculation we need. We start to think in other 2 directions: choice of geometry representation and choice of processing unit.

Regarding geometry representations, there are different one to choose: triangles(mesh), voxel, Dexel, point cloud, etc. But we don’t have enough understanding of pro and cons of each one. 

The sparse Octree voxel paper from Nvedia presented discussion comparing triangles and voxels. It appears voxel takes more memory than triangle. Giving the same color, texture and normal data, voxel takes 3.33 times more memory than Triangel mesh. 

## GPU vs CPU 

GPU is largely popular in gaming community because of its powerful procedure to compute the graphics effects, ray casting etc. GPU is also favored for its parallelisation of computation.

The two major GPU framework to use are CUDA and OpenGL. The comparison between these two is not explored yet. However, in this master thesis, the limitation of GPU is pointed out:

1. GPU cannot dynamically allocate memory, so before the calculation the memory space needed for storing the geometry should be predefined.
2. Apparently GPU is slow in read and write synchronization, which also limits the performance.

## Related topic to Boolean operation on solid geometry 

A similar field or technique that face similar computation problem is ray casting. It’s a technique in rendering to generate better and more authentic images. 

It’s similar calculation with boolean because when a beam of light meets the 3D geometry, depends on the light is inside or on or outside of geometry, the rendering image looks different.


