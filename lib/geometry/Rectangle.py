from lib.geometry.Point import Point


class Rectangle:

    def __init__(self, width=0, height=0, point=Point(0, 0, 0)):
        self.width = width
        self.height = height
        self.point = point

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getArea(self):
        return self.width * self.height
