a = float(input('Введите суму: '))
p = float(input('Введите процент: '))
d = int(input('Введите кол-во месяцов: '))
if d>12:
    k = d//12
    for i in range(k):
        a=a+a*(p/100)
        print(a)
else:
    print(a)

