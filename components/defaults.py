import numpy as np
import math

# Global variables for customization

WIND_COMPASS_DEVIATION = 180 # subsequent points will vary randomly between compass +dev and compass -dev
TICK_TIME_SCALE = 1 # in seconds
SPEED_OF_LIGHT = 2.99e8 # in meters/second

# Utility functions
def round_threshold(a, MinClip): # thanks https://stackoverflow.com/questions/7859147/round-in-numpy-to-nearest-step
    return round(float(a) / MinClip) * MinClip

def point_to_matrix_coord(x, y, mat, step):
    # take non-perfect points and map it to the nearest coordinate in a given matrix
    mx_lim = -len(mat)*step/2
    x_lim = len(mat)*step/2
    my_lim = -len(mat[0])*step/2
    y_lim = len(mat[0])*step/2

    if x < mx_lim or x > x_lim or y < my_lim or y > y_lim:
        return 0, 0
    else:
        l_offset = int(np.floor(x - mx_lim))
        t_offset = int(np.floor(y - my_lim))

        return l_offset, t_offset

def after_pop_velocity(t, t_pop):
    # function mapped to NEBP data after pop
    return -15 * (1 + np.exp(-0.000001*(t-t_pop))) + 10

def spherical_to_vector(spherical):
    theta = math.radians(spherical[1])
    phi = math.radians(spherical[0])
    return [
         math.sin(theta) * math.cos(phi),
         math.sin(theta) * math.sin(phi),
         math.cos(theta)
    ]