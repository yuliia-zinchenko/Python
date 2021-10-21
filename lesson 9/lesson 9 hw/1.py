a='\nВведите quit для завершения программы '
a+='\nКакое дополнение к пицце вы выбираете? '
active = True
while active:
    message = input(a)
    if message == 'quit':
        active = False
    else:
        print(f'Дополнение {message} добавлено')
