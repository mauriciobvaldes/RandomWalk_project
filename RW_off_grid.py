import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import itertools

radius_of_spheres_around_previously_visted_points = 1  
l = 1 #length of monomer (length of step)
number_of_bonds = 10 #number of steps in random walk

def point_picker():

    """ Generates three numbers from Gaussian distribution and returns a vector with magnitude l """

    global l

    xyz = np.random.normal(size=3)
    point = l*(xyz / np.linalg.norm(xyz))
    return point

def freely_jointed_chain(n):

    """ #TODO """

    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)

    for i in range(1, n + 1):
        val = point_picker()
        x[i] = x[i - 1] + val[0]
        y[i] = y[i - 1] + val[1]
        z[i] = z[i - 1] + val[2]

    # plots result

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, color='k')
    #plt.axis('off')
    plt.grid(b=None)
    ax.scatter(0, 0, 0, s=30, color='g')
    ax.scatter(x[n], y[n], z[n], s=30, color='r')
    plt.show()

def self_avoiding_freely_jointed_chain(n):

    """ #TODO """

    global end_to_end_distance

    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    z = np.zeros(n + 1)

    previous_positions = [] 

    for i in range(1, n + 1):

        val = point_picker()
        previous_position = np.array([x[i - 1], y[i - 1], z[i - 1]])
        previous_positions.append(previous_position)  # Storing previously visited positions
        current_position = np.add(previous_position, val)

        if i > 1:
            while not distance_check(current_position, previous_positions):
                # Updates current position until an accepted point is generated
                val = point_picker()
                current_position = np.add(previous_position, val)
                x[i], y[i], z[i] = current_position

        [x[i], y[i], z[i]] = current_position

    # Plots result

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(x, y, z, color='k')
    #plt.axis('off')
    plt.grid(b=None)
    ax.scatter(0, 0, 0, s=30, color='g')
    ax.scatter(current_position[0], current_position[1], current_position[2], s=30, color='r')
    plt.show()


def distance_check(p, list_of_interest):

    """ Returns True if point p i sufficiently far away from all the points in the list list_of_interest """
  
    counter = 0

    for i in range(len(list_of_interest)):
        distance = np.sqrt((p[0] - list_of_interest[i][0]) ** 2 + (p[1] - list_of_interest[i][1]) ** 2 + (
                    p[2] - list_of_interest[i][2]) ** 2)
        if distance < radius_of_spheres_around_previously_visted_points:
            counter = counter + 1
    if counter == 0:
        return True
    else:
        return False

#self_avoiding_freely_jointed_chain(number_of_bonds)
#freely_jointed_chain(number_of_bonds)