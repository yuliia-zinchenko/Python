#spisok_model = ['Машина', 'Робот','Айфон','Чехол']
#spisok_usera = []
def pechat(spisok_model, spisok_usera):
    while spisok_model:
        raspec = spisok_model.pop()
        spisok_usera.append(raspec)
        print(spisok_usera)
def gotovo(b):
    for i in b:
        print(f'{i} Ready')
