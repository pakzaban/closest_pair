"""
creates point objects
"""
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

def make_random_points(num):
    """ returns a list of length num of random points with coordinates <1000"""
    return [Point(random.randrange(1000), (random.randrange(1000))) for
            dummy in range(num)]



