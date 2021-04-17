def sqare(num,guess,pow):
    c=num
    x=[0]*200
    y=pow
    x[0]=guess
    for i in range(100):
        x[i+1]=(1/y)*((y-1)*x[i]+(c/x[i]**(y-1)))
    return x
res=sqare(3.145,20,4)
for i in range(90,101):
    print(res[i])