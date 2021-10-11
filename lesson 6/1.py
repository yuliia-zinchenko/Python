import math
x = int(input('x = '))
b = int(input('b = '))
if x<= -2:
    if b>=0:
        y = x*x*3 - 8*b
    else:
        y = -9*x*x - 12*b
else:
    y = x + 32
print(y)
