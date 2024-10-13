class Rectangle:
    def __init__(self, length=1.0, width=1.0):
        self.length = length
        self.width = width

    def Area(self):
        return self.length * self.width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Rectangle[length={self.length}, width={self.width}]"


rect = Rectangle(2.0, 3.0)
print(rect)
print("Area:", rect.Area())
print("Perimeter:", rect.Perimeter())