# suuretähega on objekt või klass
from math import pi


class Circle:

    def __init__(self, radius):
        """ Loo klass koos raadiusega """
        # print('Object created')
        # ei ole vajalik
        self.radius = radius

    def get_radius(self):
        # print('Return radius')
        return self.radius

    def diameter(self):
        return 2 * self.radius

    def area(self):
        # pi * pow(self.radius, 2)  # imporditud pow
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def show_circle_data(self):
        print('Radius: ', self.radius)
        print('Diameter: ', self.diameter())
        print('Area:', self.area())
        print('Perimeter:', self.perimeter())
