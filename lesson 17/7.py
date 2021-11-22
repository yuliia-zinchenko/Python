case1 = ['key1','key2', 'key3']
case2 = ['value1', 'value2', 'value3']
c = {i:g for i in case1 for g in case2}
print(c)
for k,f in c.items():
    print(k,f)
