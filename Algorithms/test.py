def Test(x):
  x = [int(i) for i in str(x)]
  mid = len(x)//2
  if len(x) & 1 :
    a = sum(x[:mid])
    b = sum(x[mid + 1:])
    return a == b 
  else:
    a = sum(x[:mid])
    b = sum(x[mid :])
    return a == b 

x = 123456 
print(Test(x))

print(len(str(289244572324525244444445)))