import random

k = int(input('Строки: '))
p = int(input('Столбцы:'))

mat = [[random.randint(1,9)for j in range(p)] for i in range(k)]
print('mat', '=>')
for i in mat:
    print(f'\t{i}')
diagonal = [mat[i][j] for i in range(k) for j in range(p) if i==j]
print('Diagonal ',diagonal)
n = int(input('Введите строку: '))
row = [mat[i][j] for i in range(k) for j in range(p) if i==n-1]
print(row)
m = int(input('Введите столбец: '))
col = [mat[i][j] for i in range(k) for j in range(p) if j==m-1]
print(col)
