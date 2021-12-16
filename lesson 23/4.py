list = ['Python', 'Java', 'C++', 'C', 'C#']
def gen(list):
    for i in list:  
        yield i

for k in gen(list):
    print(k)
    
