"""This script is written to test the efficiency of boolean operations of Pymesh"""

from typing import Dict, List, Tuple
import pymesh
from vedo import *
import numpy as np
import time
import os
import cProfile
import matplotlib.pyplot as plt
import timeit 
# This direcotry needs to be changed before running
# os.chdir("/Users/shirzart/Desktop/Introdctory_iBrus_Materials/Mesh_libraries_Exploration/grains")

def grid_type_generation(grid_type: str, x_position: float, y_position: float,
 z_position: float, scale: float):
    if grid_type == "cube":
        return pymesh.generate_box_mesh(pymesh.generate_box_mesh(
            box_min = np.array([x_position, y_position, z_position]), 
            box_max = np.array([x_position + scale, y_position + scale, z_position+ scale])))
    elif grid_type == "grain":
        os.chdir("/Users/shirzart/Desktop/iBrus-fuzzy-front-end/libraries_explorations")
        grain_raw_mesh = pymesh.load_mesh("grains/Cuboctahedron.stl")
        return pymesh.form_mesh(grain_raw_mesh.vertices + 
        [x_position+ scale,  y_position + scale, z_position + scale], grain_raw_mesh.faces)



def getsetup(number :int, distance: int, scale: int, grid_type: str):
    list_of_grain_dict = []

    for element in range(number):
        for iterator in range(number ** 2):
            reminder = iterator % number
            if reminder == 0:
                position = iterator // number
            else:
                position = reminder 
            new_grain =  grid_type_generation(grid_type, element * distance, position * distance, number * distance, scale)
            new_grain_dict = {"mesh": new_grain}
            list_of_grain_dict.append(new_grain_dict)

    cube_block = pymesh.generate_box_mesh(box_min = [0, 0, 0], 
                                          box_max = [number * distance + 1, 
                                                     number * distance + scale + 1, 
                                                     number * distance + scale])
    cube_block_dict = {"mesh": cube_block}
    
    return list_of_grain_dict, cube_block_dict



def for_loop_calculation(number_of_grains: int, distance: int, scale: int, grid_type: str):
    run_time_collection = []
    for each_element in number_of_grains:
        start_time = time.time()
        list_of_grain_dict, cube_block_dict= getsetup(each_element,distance, scale, grid_type)
        # Boolean calculation 
        CSG_grid_generation = pymesh.CSGTree({'union': list_of_grain_dict})
        CSG_entire_tree = pymesh.CSGTree({'difference': [cube_block_dict, CSG_grid_generation]})
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
    plt.title("Pymesh Run time profiling for a square grid intersecting with a cube")
    plt.show()
    plt.savefig("pymesh_runtime_scaling.png")


if __name__ == "__main__": 
    import cProfile
    number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    distance = 4
    scale = 1 # the size of cube
    # grain_mesh = pymesh.load_mesh("Cuboctahedron.stl")
    # runtime_list = for_loop_calculation(, distance,scale)

    cProfile.run('for_loop_calculation(number, distance, scale, 5)', "output.dat")

    import pstats
    from pstats import SortKey

    # Generate report sorted on the function that took most time to run it
    with open("pymesh_efficiency_test_grain_grid_output_time.txt","w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
    
    # Generate report sorted by function that is called the most number of times

    with open("pymesh_efficiency_test_grain_grid_output_call.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()



