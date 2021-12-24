import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
class Area:
    def __init__ (self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def area_triangle(self):
        p = (self.side_1+self.side_2+self.side_3)/2
        return math.sqrt(p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3))

area = Area(a,b,c)
t = area.area_triangle()
print(t)
