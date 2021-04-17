def reverse(str):
    index=-1
    for i in range(len(str)-1,len(str)//2,-1):
        if str[i].isalpha():
            temp=str[i]
            while True:
                index+=1
                if str[index].isalpha():
                    str[index],temp=temp,str[index]
                    break
    return str
x=''
str='tan,may'
y=reverse(list(str))
x.join(y)
print(x)