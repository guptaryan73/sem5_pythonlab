class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)


temp = Circle(3)
result = temp.calculate_area()
print(f"The area of a circle with radius {temp.radius} is {result}")
