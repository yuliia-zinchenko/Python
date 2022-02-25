# #1
# import math
# a = int(input('Введите радиус окружности: '))
# b = int(input('Введите 1, если хотите рассчиать плoщадь круга, и 2, если длину окружности: '))
# if b == 1:
#     c = round((math.pi*2*a), 2)
#     print(f"Длина окружности: {c}")
# elif b == 2:
#     d = round((math.pi*a*a), 2)
#     print(f"Площадь круга: {d}")
# else:
#     print('Error')

 #2
# a = input('Введите ваш пароль: ')
# b = input('Повторите пароль: ')
# if len(a) < 4:
#     print("Пароль слишком короткий")
# if a == b:
#     print('Пароль подтвержден')
# else:
#     print('Что-то не так, попробуйте снова')

# #3
# a = int(input('Введите ваш возраст: '))
# b = int(input('На какую сумму вы хоте ли бы оформить кредит: '))
# print('Ваш месячный доход должен составлять минимум 30% от желаемой суммы')
# c = int(input('Введите ваш месячный доход: '))
# if (a>=18) and (b*0.3>=c):
#     print('Кредит будет одобрен')
# elif (a>18) and (b*0.3<=c):
#     print('Ваш месячный доход составляет менее 30% от желаемой суммы кредита')
# elif (a<18) and (b*0.3>=c):
#     print('Для оформления кредита вы должны достигнуть 18 лет')

# #4
# b = int(input('Введите ваши баллы: '))
# if b>9:
#     print('Отлично!')
# elif 7<b<9:
#     print('Хорошо!')
# elif 3<b<8:
#     print('Ты можешь лучше!')
# elif b<4:
#     print('Старайся больше')

# #5
# import math
# x = int(input('x = '))
# y = int(input('y = '))
# if x>y:
#     a = round(math.sqrt(x*y), 2)
#     print(f'z = {a}')
# else:
#     b = round(math.log((x+y), 10), 2)
#     print(f'z = {b}')

# #6
# b = int(input('Введите температуру: '))
# if b>=20:
#     print('On')
# else:
#     print('Off')

# #7
# b = int(input('Какой у вас номер: '))
# if b%2 == 0:
#     print('Второй')
# else:
#     print('Первый')

#8
# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))
# if (a+b)>c and (b+c)>a and (c+a)>b:
#         print('Такий трикутник існує')
# else:
#         print('Такого трикутника не існує')

#9
# x = int(input('x = '))
# y = int(input('y = '))
# if x<0 and y<0:
#     print('ІII четверть')
# elif x<0 and y>0:
#     print('ІI четверть')
# elif x>0 and y>0:
#     print('I четверть')
# elif x>0 and y<0:
#     print('ІV четверть')

# #10
# # x = int(input('x = '))
# # if x>0:
# #     y = (2*x - 10)
# #     print(y)
# # elif x == 0:
# #     y = 0
# #     print(y)
# # else:
# #     y = (abs(x)*2 - 1)

#1
# import math
# x = int(input('x = '))
# if x>=-5:
#     y = math.sqrt(x+5)
#     print(y)

#2
# import math
# x = int(input('x = '))
# if x != 7:
#     y = 1/(x+7)
#     print(y)

# #3
# import math
# x = int(input('x = '))
# if x>-5:
#     y = 1/(math.sqrt(x+5))
#     print(y)

#4
# import math
# x = int(input('x = '))
# if x != -5:
#     y = 1/(abs(x+5))
#     print(y)

#5
# import math
# x = int(input('x = '))
# if x != 0:
#     y = 1/(x**7)
#     print(y)

#6
# import math
# x = int(input('x = '))
# if x>=7:
#     y = math.sqrt(x+5) + math.sqrt(x+7)
#     print(y)

#7
# import math
# x = int(input('x = '))
# if x>=7:
#     y = math.sqrt(x+5) + (1/(math.sqrt(x+7)))
#     print(y)

#8
# import math
# x = int(input('x = '))
# if x>-5 and x != 7:
#     y = (1/(math.sqrt(x+5))) + (1/(x-7))
#     print(y)

#1
# import math
# x = int(input('x = '))
# if x>0:
#     y = x
#     print(y)
# else:
#     y = x*x
#     print(y)

#2
# import math
# x = int(input('x = '))
# if -10<x<5:
#     y = x
#     print(y)
# else:
#     y = x*x
#     print(y)

#3
# import math
# x = int(input('x = '))
# if 1<=x<=5 or x>10:
#     y = x
#     print(y)
# else:
#     y = x*x
#     print(y)

#4
# import math
# x = int(input('x = '))
# if x<=0:
#     y = x
#     print(y)
# elif 0<x<=5:
#     y = x*x
#     print(y)
# else:
#     y = 25
#     print(y)