def pizza(size, *type):
    print(f'Вы заказали такие пиццы с размером {size}:')
    for i in type:
        print(f'- {i}')

size = input('Размер: ')
pizza(size, '4 cheese')
size = input('Размер: ')
pizza(size, 'diablo', 'Hawaii', '4 meat', 'Peperoni', 'Ukranian')
size = input('Размер: ')
pizza(size, '4 cheese', '4 meat')
