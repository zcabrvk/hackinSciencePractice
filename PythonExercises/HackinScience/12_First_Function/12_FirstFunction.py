from math import pi

def circle_perimeter(radius):
    return 2 * pi * radius


for i in [1, 10, 100]:
    print("The permiter of circle with radius " + str(i) + " is " + str(circle_perimeter(i)))