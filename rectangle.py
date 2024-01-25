class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length * self.breadth
        print(f"The area of Rectangle of length {self.length} and breadth {self.breadth} is {area}.")

    def perimeter(self):
        peri = 2*(self.length + self.breadth)
        print(f"The Perimeter of Rectangle of length {self.length} and breadth {self.breadth} is {peri}.")

r1 = rectangle(10,20)
r1.area()
r1.perimeter()