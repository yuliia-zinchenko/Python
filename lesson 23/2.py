def gen(n):
    print('I перебор: ')
    yield n
    print('II перебор: ')
    yield n+1
    print('III перебор: ')
    yield n*1

n = int(input('Введите число: '))
t = gen(n)
print(next(t))
print(next(t))
print(next(t))

