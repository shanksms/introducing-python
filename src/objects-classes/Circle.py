class Circle:
    def __init__(self, radius):
        self.__radius = radius
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, radius):
        self.__radius = radius
    @property
    def diameter(self):
        return 2 * self.__radius

if __name__ == '__main__':
    circle = Circle(2)
    print(circle.diameter)
    circle.radius = 4
    print(circle.diameter)
