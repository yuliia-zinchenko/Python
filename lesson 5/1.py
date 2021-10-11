a = int(input('Введите ваш вклад: '))
p = float(input('Введите процент: '))
m = int(input('Введите месяц: '))
if m>12:
    s=a+a*(p/100)
    print(s)
else:
    print(a)
