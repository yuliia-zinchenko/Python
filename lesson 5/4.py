a = float(input('a = '))
b = float(input('b = '))
if a>b:
    a = 1
    b = 0
    print(a, b)
elif b>a:
    b = 1
    a = 0
    print(a, b)
else:
    print('Вони дорівнюють')
