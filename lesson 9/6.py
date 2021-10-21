a ='\nПривет! я хочу узнать о тебе информацию'
a+='\nВведите out для завершения программы '
active = True
while active:
    message = input(a)
    if message == 'out':
        active = False
    else:
        print(message)
