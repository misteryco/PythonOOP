class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int):
        self.x = new_x

    def set_y(self, new_y: int):
        self.y = new_y

    def __repr__(self):
        return f"The point has coordinates ({self.x},{self.y})"
    """ 
    Instead of using __str__ we use __repr__ it gives better output on command line
    when we call "__str__", but "__str__" is not defined, class returns result from the "__repr__"
    """


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
