def gen(n):
    a, b = 1,1
    for i in range(n):
        yield a
        a, b = b, a+b
        
n = int(input('Введите число: '))
t = gen(n)
for k in t:
    print(k)
