import random
n = 4
m = 4
mat = [[random.randint(1,9)for j in range(m)] for i in range(n)]
print('mat', '=>')
#print(mat)
for i in mat:
    print(f'\t{i}')
diagonal = []
for k in range(len(mat)):
    c = len(mat) - k - 1
    diagonal.append(mat[k][c])
print(diagonal)

