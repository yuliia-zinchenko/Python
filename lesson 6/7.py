k =[2.3, 4.5, 3.5, 10.3, 5]
b=0
x=k[0]
for i in k:
    b=i+b
print(b)
for i in k:
    if x<i:
        x = i
print(x)
    
