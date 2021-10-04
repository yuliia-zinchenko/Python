#алгоритм ветвления(да/нет)
a = 5000
data = int(input('Дата: '))
if data > 365:
    s = a+a*0.2
    print('Баланс:', s)
else:
    print('Баланс:', a)
