import math

from lib.geometry.Point import Point


class Circle:

    def __init__(self, radius=0, point=Point(0, 0, 0)):
        self.point = point
        self.radius = radius

    def getArea(self):
        return self.radius * self.radius * math.pi

    def getPerimeter(self):
        return 2 * self.radius * math.pi
