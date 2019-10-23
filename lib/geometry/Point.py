import math


class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def distance(x1, y1, z1, x2, y2, z2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def distance(self, point2):
        return Point.distance(self.x, self.y, self.z, point2.x, point2.y, point2.z)
