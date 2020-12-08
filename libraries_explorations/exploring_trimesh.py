"""Python script of the trimesh exploration jupyter notebook"""

import numpy as np
import trimesh

trimesh_box_1 = trimesh.creation.box()
trimesh_box_2 = trimesh.creation.box()

# color the 2 boxes
trimesh_box_1.visual.vertex_colors = trimesh.visual.random_color()
trimesh_box_2.visual.vertex_colors = trimesh.visual.random_color()

#Move one of the box a little bit and show it
trimesh_box_2.apply_translation([0.5,0.5,0])
two_box_scene = trimesh.Scene([trimesh_box_1, trimesh_box_2])
two_box_scene.show() 


print(trimesh.interfaces.blender.exists)
print(trimesh.interfaces.scad.exists)
intersected_area = trimesh.boolean.intersection([trimesh_box_1,trimesh_box_2], engine="blender")
print(type(intersected_area))

intersected_area.show()

diff_box_1_intersection = trimesh.boolean.difference([trimesh_box_1, intersected_area], engine="blender")
diff_box_2_intersection = trimesh.boolean.difference([trimesh_box_2, intersected_area], engine="blender")

two_residual_box_scene = trimesh.Scene([diff_box_1_intersection, diff_box_2_intersection])
two_residual_box_scene.show()

# The relationship between spatial points and trimesh

print(trimesh.proximity.close
.proximity.closest_point(trimesh_box_1,[[0, 0, 0], [10, 10, 10], [5, 4, 3]]))