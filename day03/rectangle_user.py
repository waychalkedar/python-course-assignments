import sys

height = float(sys.argv[1])
width = float(sys.argv[2])
area = height * width
perim = 2 * (height + width)

print(f"Area is {"{:.4f}".format(area)} sq units, perimeter is {"{:.4f}".format(perim)} units")