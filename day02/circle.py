import numpy as np

print("This program will calculate the area and circumference of a circle having a user-specified radius.")
radius = float(input("Enter the desired radius of the circle: "))
area = np.pi * radius**2
circ = 2 * np.pi * radius

print(f"Area is {"{:.4f}".format(area)} sq units, circumference is {"{:.4f}".format(circ)} units")
