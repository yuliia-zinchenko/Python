import math
a = int(input('a = '))
if a>0:
    x_1 = math.sqrt(a) 
    x_2 = math.sqrt(a)*(-1)
    print(x_1, x_2)
elif a==0:
    x = 0
    print(x)
else:
    print('Обчислення неможливе')
