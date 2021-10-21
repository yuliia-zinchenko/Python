a='\nВведите quit для завершения программы '
a+='\nКакое дополнение к пицце вы выбираете? '
while True:
    message = input(a)
    if message == 'quit': break
    else:
        print(f'Дополнение {message} добавлено')

