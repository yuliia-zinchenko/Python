def gen(n):
    print('I перебор: ')
    yield n
    print('II перебор: ')
    yield n+1
    print('III перебор: ')
    yield n*3

n = int(input('Введите число: '))
t = gen(n)
for i in t:
    print(i)
