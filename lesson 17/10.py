c = {i:i**2 for i in range(20) if i>=5}
m = {g:l for g,l in c.items() if l<=100}
j = {key:('true2' if val%2==0 else 'false') for key,val in m.items()}
for k,v in j.items():
    print(k,v)
