import matplotlib.pyplot as plt
from rw_visual import RandomWalk

rw = RandomWalk()
rw.num_points = 5000000
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=0.00001)
plt.show()
