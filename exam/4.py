a = int(input('Введите свой возраст: '))
if a<2:
    print('Младенец')
elif 2<=a<4:
    print('Малыш')
elif 4<=a<13:
    print('Ребенок')
elif 13<=a<20:
    print('Подросток')
elif 20<=a<65:
    print('Взрослый')
else:
    print('Пожилой человек')
    
