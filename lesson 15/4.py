dict = {
    'user_0':{
            'name':'Alexey',
            'surname':"Kosenko",
            'location':14.5,
            'age':14
            },
    'user_1':{
            'name':'Illia',
            'surname':"Katerinich",
            'location':37.7,
            'age':14
            }
    }
for a,b in dict.items():
    print(f'{a}:')
    for i,k in b.items():
        print('\t',f'{i}: {k}')
        
