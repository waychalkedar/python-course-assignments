print("This program will calculate the area and perimeter of a rectangle having a user-specified height and width.")
height = float(input("Enter the desired height of the rectangle: "))
width = float(input("Enter the desired width: "))
area = height * width
perim = 2 * (height + width)

print(f"Area is {"{:.4f}".format(area)} sq units, perimeter is {"{:.4f}".format(perim)} units")