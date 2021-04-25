def encoding(newmap,sti):
    ogmap='abcdefghijklmnopqrstuvwxyz'
    q=[]
    d=dict(zip(newmap,ogmap))
    for i in sti: 
        q.append(d[i])
    s=''.join(q)
    return s 

sti='{()}'
mymap='qwertyuiopasdfghjklzxcvbnm'
print(encoding(mymap,'tanmay'))
