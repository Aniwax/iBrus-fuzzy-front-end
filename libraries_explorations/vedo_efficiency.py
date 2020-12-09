"""This script is generated for vedo efficiency test."""
from vedo import *
import time
# declare the instance of the class
vp = Plotter(shape=(2, 2), interactive=0, axes=3)

# build to sphere meshes
s1 = Sphere(pos=[-0.7, 0, 0], c="r", alpha=0.5)
s2 = Sphere(pos=[0.7, 0, 0], c="g", alpha=0.5)


box_1 = Cube(pos =[1, 0, 0], side = 1, c='b',alpha=1)


# vp.show(Grid_1)
# vp.show(Grid_1, box_1,__doc__, at=0)



# make 3 different possible operations:
start_time_intersect = time.time()
b1 = s1.boolean("intersect", s2).c('m').legend("intersect")

end_time_intersect = time.time()
process_time_intersect = end_time_intersect - start_time_intersect
print(f"Boolean operations time for intersections is {process_time_intersect}")
vp.show(b1, at=1, resetcam=False)


b2 = s1.boolean("plus", s2).c("b").wireframe(True).legend("plus")
vp.show(b2, at=2, resetcam=False)

# b3 = s1.boolean("minus", s2).legend("minus").addScalarBar(c='w')
# vp.show(b3, at=3, resetcam=False)
b4 = b2.boolean("plus", box_1).c("g").wireframe(True).legend("plus")
vp.show(b4, at=3, resetcam=False)
interactive()


# # Efficiency starts from below:
# vp_2 = Plotter(shape=(1, 2), interactive=0, axes=3)
# number = 5
# distance = 4 
# list_of_ball = []

# for element in range(number):
#     for iterator in range(number ** 2):
#         reminder = iterator % number
#         if reminder == 0:
#             position = iterator // number
#         else:
#             position = reminder 
#         new_grain_ball = Cube(pos=[element * distance, position * distance, number * distance],c='b', alpha =1)
#         list_of_ball.append(new_grain_ball)


# cube_block = Cube(pos=[number*distance/2-distance/2, number*distance/2-distance/2, 0], side=number*distance, c='b', alpha = 1)
# # vp_2.show(list_of_ball, cube_block, at =0)

# # c1 = cube_block.boolean("intersect", list_of_ball).c('m').legend("intersect")


# for i in range(1, len(list_of_ball)):
#     list_of_ball[i] = list_of_ball[i].boolean("plus", list_of_ball[i-1]).c("b").wireframe(True).legend("plus")


# x1 = Sphere(pos=[-5, 0, 0], c="r", alpha=0.5)
# x2 = Sphere(pos=[5, 0, 0], c="g", alpha=0.5)
# x3 = x1.boolean("plus", x2).c("g")

# # s3 = s1.clone().cutWithMesh(s2, invert = True)
# vp_2.show(x3, at =0)
# interactive()

# # S4 = box_1.boolean('')


# # vp_3.show()
