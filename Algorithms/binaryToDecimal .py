def deci(binary):
    temp=0 
    res=0 
    i=0 
    while binary>0:
        temp=binary%10 
        res=res+temp *(2**i)
        binary=binary//10
        i+=1
    return res 

print(deci(111))