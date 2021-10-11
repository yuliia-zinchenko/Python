a = float(input('Введите суму: '))
p = float(input('Введите процент: '))
for i in range(5):
    a = a+a*(p/100)
    print(a)

