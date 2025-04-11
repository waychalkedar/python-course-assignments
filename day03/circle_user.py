import numpy as np
import sys

radius = float(sys.argv[1])
area = np.pi * radius**2
circ = 2 * np.pi * radius

print(f"Area is {"{:.4f}".format(area)} sq units, circumference is {"{:.4f}".format(circ)} units")
