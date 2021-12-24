import math
x = float(input('X = '))
y = float(input('y = '))
if (math.abs(x*y)<1) and x<0:
    z = ((x+y)/math.e**(x*y)) 
elif x>2 and y<=0:
    z = (-math.log(x))**2
#elif y>0 and 0<=x<=2:
#    z = (math.log()
print(z)
