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
# os.chdir("/Users/shirzart/Desktop/iBrus-fuzzy-front-end/libraries_explorations")


def grid_type_generation(grid_type: str, x_position: float, y_position: float,
 z_position: float):
    if grid_type == "cube":
        Box = trimesh.primitives.Box()
        return Box.apply_translation(np.array([x_position, y_position,z_position]))
    elif grid_type == "grain":
        os.chdir("/Users/shirzart/Desktop/iBrus-fuzzy-front-end/libraries_explorations")
        grain_raw_mesh = trimesh.load_mesh("grains/Cuboctahedron.stl")
        new_grain = trimesh.Trimesh.copy(grain_raw_mesh)
        return new_grain.apply_translation(np.array([x_position, y_position,z_position]))
            




def getsetup(number :int, distance: int, grid_type: str):
    list_of_grain = []

    for element in range(number):
        for iterator in range(number ** 2):
            reminder = iterator % number
            if reminder == 0:
                position = iterator // number
            else:
                position = reminder 
            new_grain = grid_type_generation(grid_type, element * distance, position * distance, number * distance)
            list_of_grain.append(new_grain)


    cube_block = trimesh.primitives.Box()
    cube_block.apply_translation(-cube_block.vertices[0])
    cube_block.apply_scale(number * distance)
    cube_block.apply_translation([-distance/2, -distance/2, 0])
    
    return list_of_grain, cube_block


def for_loop_trimesh(number_of_grains: int, distance: int, grid_type):
    run_time_collection = []
    for each_element in number_of_grains:
        start_time = time.time()
        list_of_grain, Block= getsetup(each_element,distance, grid_type)
        # Boolean calculation
        union_list_of_balls = trimesh.boolean.union(list_of_grain, engine="blender")
        residual_box_block = trimesh.boolean.difference([Block, union_list_of_balls], engine="blender")
        # residual_box_block.show() # Actually I don't need to show it. As long as calculation is done, it's fine.
        end_time = time.time()
        this_process_time = end_time-start_time
        run_time_collection.append(this_process_time)
        print(run_time_collection)

    grain_numbers = [element ** 2 for element in number_of_grains]
    plt.figure()
    plt.plot(grain_numbers, run_time_collection,'bs')
    plt.xlabel("number of grains/cubes in the grid")
    plt.ylabel("run time in seconds")
    plt.title("Trimesh Run time profiling for a square grid intersecting with a cube")
    plt.show()
    plt.savefig("Trimesh_grain_grid_runtime_scaling_bup.png")
    return run_time_collection

if __name__ == "__main__": 
    import cProfile
    number = [1,2,3,4,5,6,7,8,9,10]
    distance = 4

    cProfile.run('for_loop_trimesh(number, distance, "grain")', "output.dat")

    import pstats
    from pstats import SortKey

    # Generate report sorted on the function that took most time to run it
    with open("trimesh_efficiency_test_output_time_bup.txt","w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
    
    # Generate report sorted by function that is called the most number of times

    with open("trimesh_efficiency_test_output_call_bup.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()
