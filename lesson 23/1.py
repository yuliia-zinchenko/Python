def name(x):
    x*=2
    yield x
t = name(5)
print(next(t))
