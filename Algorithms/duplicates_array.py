
#############USING SET 
def dup(arr):
  n=len(arr)
  v=set()
  for i in range(n):
    if arr[i] not in v:
      v.add(arr[i])
    else:
      print(f"{arr[i]} is a duplicate")


###USING NORMAL INDEXING 
def dup2(arr):
  n=len(arr)
  for i in range(n-1,0,-1):
    j=0 
    while j<i:
      if arr[i]==arr[j]:
        print(f"{arr[i]} is a duplicate")
        break
      else:
        j+=1
a=[1,2,3,4,2,4,6,7,1]
dup2(a)
