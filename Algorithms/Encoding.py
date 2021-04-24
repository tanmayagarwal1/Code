def my_char(myset,sti):
    ogset='abcdefghijklmnopqrstuvwxyz'
    dic=dict(zip(myset,ogset))
    q=[]
    for i in sti:
        q.append(dic[i])
    return q 
charSet = 'qwertyuiopasdfghjklzxcvbnm'
a=my_char(charSet,'utta')
print(''.join(a))