def fullname(name, surname):
         c = f'{name.title()} {surname.title()}'
         return c
while True:
    print('Укажите имя и фамилию')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    if name == 'break' or surname == "break":
        break
    else:
        surname = input('Фамилия: ')
        k = fullname(name, surname)
        print(k)
