
import os
import numpy
import sys

def calculate_distance(coords1,coords2):
    """
    This function accepts coordinates of two atoms and calculates the distance between atoms.
    """
    x_distance = coords1[0]-coords2[0]
    y_distance = coords1[1]-coords2[1]
    z_distance = coords1[2]-coords2[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12

def bond_check(distance_12, minimum=0, maximum=1.5):
    """
    checks bond values with default max of 1.5 and defaul min of 0 if not specified and gives values of true or false
    """
    if distance_12>maximum or distance_12<minimum:
        return('False')
    else:
        return('True')

file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, dtype='unicode', skip_header=2)
symbols=xyz_file[:,0]
coordinate=xyz_file[:,1:]
coordinate = coordinate.astype(numpy.float)
num_atoms = len(symbols)
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1>num2:
            distance_12=calculate_distance(coordinate[num1],coordinate[num2])
            if bond_check(distance_12, 0, 1.5)is ('True'):
                print(F'{symbols[num1]} to {symbols[num2]}:{distance_12:.3f}')
