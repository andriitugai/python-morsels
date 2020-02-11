import math

class Circle(object):
    def __init__(self, radius = 1):
        self.radius = radius
        self.diameter = radius * 2
        self.area = math.pi * radius ** 2

    def 


def main():
    c1 = Circle(5)
    print(f'Circle 1: Radius = {c1.radius}, Diameter = {c1.diameter}, Area = {c1.area}')

    c0 = Circle()
    print(f'Circle 0: Radius = {c0.radius}, Diameter = {c0.diameter}, Area = {c0.area}')


if __name__ == '__main__':
    main()

