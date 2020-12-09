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


def getsetup(number :int, distance: int, scale: int):
    list_of_grain_dict = []

    for element in range(number):
        for iterator in range(number ** 2):
            reminder = iterator % number
            if reminder == 0:
                position = iterator // number
            else:
                position = reminder 
            new_grain =  pymesh.generate_box_mesh(
            box_min = np.array([element * distance, position * distance, number * distance]), 
            box_max = np.array([element * distance + scale, position * distance + scale, number * distance + scale]))
            new_grain_dict = {"mesh": new_grain}
            list_of_grain_dict.append(new_grain_dict)

    cube_block = pymesh.generate_box_mesh(box_min = [0, 0, 0], 
                                          box_max = [number * distance + 1, 
                                                     number * distance + scale + 1, 
                                                     number * distance + scale])
    cube_block_dict = {"mesh": cube_block}
    
    return list_of_grain_dict, cube_block_dict



def for_loop_calculation(number_of_grains: int, distance: int, scale: int):
    run_time_collection = []
    for number_of_grains in number:
        start_time = time.time()
        list_of_grain_dict, cube_block_dict= getsetup(number_of_grains,distance, scale)
        # Boolean calculation 
        CSG_grid_generation = pymesh.CSGTree({'union': list_of_grain_dict})
        CSG_entire_tree = pymesh.CSGTree({'difference': [cube_block_dict, CSG_grid_generation]})
        # residual_box_block.show() # Actually I don't need to show it. As long as calculation is done, it's fine.
        end_time = time.time()
        this_process_time = end_time-start_time
        run_time_collection.append(this_process_time)
        print(run_time_collection)

    plt.figure()
    plt.plot(number, run_time_collection)
    plt.show()
    plt.savefig("runtime_scaling.png")
    
    return run_time_collection


if __name__ == "__main__": 
    import cProfile
    number = [5, 10]
    distance = 4
    scale = 1 # the size of cube
    # grain_mesh = pymesh.load_mesh("Cuboctahedron.stl")
    # runtime_list = for_loop_calculation(, distance,scale)

    cProfile.run('for_loop_calculation(number, distance, scale)', "output.dat")

    import pstats
    from pstats import SortKey

    # Generate report sorted on the function that took most time to run it
    with open("pymesh_efficiency_test_output_time.txt","w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
    
    # Generate report sorted by function that is called the most number of times

    with open("pymesh_efficiency_test_output_call.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()



