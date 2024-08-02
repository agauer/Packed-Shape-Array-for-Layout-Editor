import numpy as np
import random as rand

# all dimensions are in micrometers

# box size
x_maxDimension = 149.5
y_maxDimension = 149

# shape parameters
radius = 0.3
domain_spacing = 1                                  # center to center distance between structures

# Layout Editor layer number
layer = 1

# Output file
dataFile = open("hex_packed_array.txt","w")

# generate offsets
def deviation_center(r,D):
    max_dev = 0.2                                   # maximum deviation (should not exceed 50% or 0.5)
    dD = max_dev*(D-r)*rand.random()                # offset distance
    theta = rand.randint(0,359)                     # offset direction
    dx = dD*np.cos(theta*np.pi/180)                 # x offset
    dy = dD*np.sin(theta*np.pi/180)                 # y offset
    return dx,dy

# generate radius deviation
def deviation_radius(r):
    max_dev = 0.1                                   # maximum deviation (should not exceed 100% or 1)
    dr = r*max_dev*rand.uniform(-1,1)               # change in radius
    return dr

# coordinates to keep track of current shape being placed
x_current = radius
y_current = radius

# counters
row_number = 0
n_shapes = 0

# generate shape array and save to data file
while y_current+radius < y_maxDimension:
    while x_current+radius < x_maxDimension:
        # generate deviations
        dx,dy = deviation_center(radius,domain_spacing)
        dr = deviation_radius(radius)
        # write to file
        dataFile.write(str(x_current+dx)+","+str(y_current+dy)+","+str(radius+dr)+","+str(layer)+"\n")
        # iterate for next shape
        x_current += domain_spacing
        n_shapes += 1
    row_number += 1
    # create row offsets for hexagonal packing
    if row_number%2 == 0:
        x_current = radius
    else:
        x_current = radius+domain_spacing/2
    y_current += np.sqrt(3)/2*domain_spacing