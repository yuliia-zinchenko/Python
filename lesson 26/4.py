import math
r = float(input('r = '))
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def len_circle(self):
        return 2*(math.pi)*self.radius
    def area_circle(self):
        return (math.pi)*self.radius**2

c1 = Circle(r)
t= c1.len_circle()
print(t)    
