a ='\nПривет! я хочу узнать о тебе информацию'
a+='\nВведите out для завершения программы '
a+='\nВведите ваше имя '
message = ''
while message !='out':
    message = input(a)
    print(f'Привет, {message}')
