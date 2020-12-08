"""This script is generated for testing the efficiency of trimesh intersections

We test the efficiency of boolean operations by creating a square grid of grains and 
then perform an intersection with a big cube that always lies beneath the grid, whose
dimension is determined by the length of the grid. Then check the run time for 
different dimension of the grid.
"""

from typing import List
import trimesh
import numpy as np
import random
import os
from trimesh.base import Trimesh 
import time 
import matplotlib.pyplot as plt

# This direcotry needs to be changed before running
os.chdir("/Users/shirzart/Desktop/Introdctory_iBrus_Materials/Mesh_libraries_Exploration/grains")
number = [5]
distance = 4
grain_mesh = trimesh.load_mesh("Cuboctahedron.stl",'stl')
run_time_collection = []

def getsetup(number :int, distance: int):
    list_of_grain = []

    for element in range(number):
        for iterator in range(number ** 2):
            reminder = iterator % number
            if reminder == 0:
                position = iterator // number
            else:
                position = reminder 
            new_grain = trimesh.Trimesh.copy(grain_mesh)
            new_grain.apply_translation(np.array([element * distance, position * distance, number * distance]))
            list_of_grain.append(new_grain)


    cube_block = trimesh.primitives.Box()
    cube_block.apply_translation(-cube_block.vertices[0])
    cube_block.apply_scale(number * distance)
    cube_block.apply_translation([-distance/2, -distance/2, 0])
    
    return list_of_grain, cube_block



for number_of_grains in number:
    start_time = time.time()
    list_of_grain, Block= getsetup(number_of_grains,distance)
    # Show the plot 

    # the_whole_scene = trimesh.Scene([Block, list_of_grain])
    # the_whole_scene.show()
    # Boolean calculation 
    union_list_of_balls = trimesh.boolean.union(list_of_grain, engine="blender")
    residual_box_block = trimesh.boolean.difference([Block, union_list_of_balls], engine="blender")
    # residual_box_block.show() # Actually I don't need to show it. As long as calculation is done, it's fine.
    end_time = time.time()
    this_process_time = end_time-start_time
    run_time_collection.append(this_process_time)


plt.figure()
plt.plot(number, run_time_collection)
plt.show()