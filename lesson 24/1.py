def f_1():
    print("Началась загрузка 1%")
def f_2():
    n=1
    while n<100:
        print("Загрузка...")

        i=f"{n}%"
        yield i
        n+=5
        
     
def f_3():
    print("Загрузка закончена 100%")
f_1()
for i in f_2():
    print(i)
f_3()
