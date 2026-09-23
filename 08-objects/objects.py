# module code (usually separate)
class Rectangle:
    pass

# runtime code
rect1 = Rectangle()
print(rect1)#<__main__.Rectangle object at 0x101072900>
print(rect1.__str__())#<__main__.Rectangle object at 0x1022b6900>

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
        pass

rect2 = Rectangle()
rect2.width = 2
rect2.height = 2
print(rect2.width)
print(rect2.height)
print(rect2)#<__main__.Rectangle object at 0x104bdaa50>

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    pass

rect3 = Rectangle(4,5)
print(rect3.width)
print(rect3.height)
print(rect3.area())
print(rect3)#<__main__.Rectangle object at 0x1000beba0>

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def __str__(self):
        return f"Rectangle width: {self.width} height: {self.height}"

rect4 = Rectangle(8,10)
print(rect4.width)#8
print(rect4.height)#10
print(rect4.area())#80
print(rect4)#Rectangle width: 8 height: 10
