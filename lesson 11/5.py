def pechat(a,b):
    while listmodel:
        raspech = a.pop()
        print(f'{raspech} распечатался')
        b.append(raspech)
        #print(userlist)
def gotovo(b):
    for i in b:
        print(f'{i} готово')
listmodel = ['Машина', 'Робот', 'Айфон', 'Чехол']
userlist = []
pechat(listmodel, userlist)
gotovo(userlist)
print(userlist)

