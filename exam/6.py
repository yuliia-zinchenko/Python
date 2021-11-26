food = ['pizza', 'falafel', 'carrot cake']
food2 = food[:]
a = input('Введите вкус мороженого: ')
food2.append(a)
print('Мои любимые блюда: ')
for i in food:
    print(f'\t{i}')
print('Любимые блюда моего друга: ')
for k in food2:
    print(f'\t{k}')
