#t=list(filter(lambda x:x%2==0,arr))
#print(t)
def even_n(i):
    if i%2==0:
        return True
    else:
        return False
arr=[1,2,3,4,5,6,7,8,9,10]
t=list(filter(even_n,arr))
print(t)
