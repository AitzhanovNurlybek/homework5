class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def Area(self):
        return 3.1416 * (self.radius ** 2)

    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"


circle = Circle(5.0, "blue")
print(circle)
print("Radius:", circle.radius)
print("Area:", circle.Area())