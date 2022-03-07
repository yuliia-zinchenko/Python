#1
#a = input('Введите свое имя: ')
#print(f'Вітаю, {a}')

#2
# def copy(a:str, n:int):
#     return a*n
#
# a = input('Введите строку ')
# n = int(input('Введите n '))
# t = copy(a, n)
# print(t)

#6
# def func(a, b):
#     if a>b:
#         print(f'{a} більше {b}')
#     elif b>a:
#         print(f'{b} більше {a}')
#     else:
#         print(equal)
#
# a = int(input('a = '))
# b = int(input('b = '))
# t = func(a, b)
# print(t1)

# #7
# def func(a, b ,c):
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     elif c>a and c>b:
#         print(c)
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# t = func(a, b, c)
# print(t)

# #8
# def func(a, b, c):
#     if (a+b)>c and (b+c)>a and (c+a)>b:
#         print('Такий трикутник існує')
#     else:
#         print('Такого трикутника не існує')
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# t = func(a, b, c)
# print(t)

# #9
# def func(a, b):
#     return (a+' '+b)
# a = input('a = ')
# b = input('b = ')
# t = func(a, b)
# print(t)

# #10
# def func(a, b, c):
#     if c == '+':
#         print(a+b)
#     elif c == '-':
#         print(a-b)
#     elif c == '*':
#         print(a*b)
#     elif c == '/':
#         d = round((a/b), 2)
#         print(d)
# a = int(input('a = '))
# b = int(input('b = '))
# c = (input('c = '))
# t = func(a, b, c)
# print(t)

# #11
# def func(a, b, c):
#     return (a + ' ' + b + ' ' + c)
# a = (input('a = '))
# b = (input('b = '))
# c = (input('c = '))
# t = func(a, b, c)
# print(t)

#12
# def func(a):
#     if a == (12 or 1 or 2):
#         print('Winter')
#     elif a == (3 or 4 or 5):
#         print('Spring')
#     elif a == (6 or 7 or 8):
#         print('Summer')
#     elif a == (9 or 10 or 11):
#         print("Autmn")
#     else:
#         print('Error')
# a = int(input('a = '))
# t = func(a)
# print(t)

#13
def func(a):
    b = '*'
    for i in a:
        c = b*i
        print(c)
d = int(input('a = '))
e = int(input('b = '))
f = int(input('c = '))
g = int(input('d = '))
h = int(input('e = '))
a = []
a.append(d)
a.append(e)
a.append(f)
a.append(g)
a.append(h)

t = func(a)
print(t)
