"""
Program solves the slope and distance equations for the Line
class
"""
import math


# Problem 1: Calculate the slope and distance of a line using two given coordinates
class Line:
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        the_distance = math.sqrt((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2)
        return the_distance

    def slope(self):
        the_slope = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        return the_slope


x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))
l1 = Line((x1, y1), (x2, y2))
print("The distance of the line is: ", l1.distance())
print("The slope of the line is: %.4f" % l1.slope())


# Problem 2: Calculate the volume and surface area of a cylinder
class Cylinder:
    Pi = 3.14

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def volume(self):
        the_volume = self.Pi * self.radius ** 2 * self.height
        return the_volume

    def surface_area(self):
        the_surf_area = 2 * self.Pi * self.radius ** 2 + 2 * self.Pi * self.radius * self.height
        return the_surf_area


C1 = Cylinder(2, 3)
print("The volume of the Cylinder is: %.2f" % C1.volume())
print("The surface area of the Cylinder is: %.2f" % C1.surface_area())
