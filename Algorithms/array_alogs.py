
#################REVERSE SPECIAL#######
def revspecialutil(arr):
    n=len(arr)
    index=-1
    for i in range(n-1,n//2,-1):
        if arr[i].isalpha():
            temp = arr[i]
            while True:
                index+=1
                if arr[index].isalpha():
                    arr[index],temp=temp,arr[index]
                    break
    return arr
def revspecial(str):
    x=revspecialutil(list(str))
    print("{}".format(''.join(x)))

###############TRIPLETS################    
def tripletsutil(arr):
    n=len(arr)
    for i in range(n):
        arr[i]=arr[i]**2
    arr.sort()
    for i in range(n-1,1,-1):
        j=0
        k=i-1
        while j<k:
            if arr[j]+arr[k]==arr[i]:
                print("found {} {} {}".format(math.sqrt(arr[k]),math.sqrt(arr[j]),math.sqrt(arr[i])))
                return True
            else:
                if arr[j]+arr[k]<arr[i]:
                    j+=1
                else:
                    k-=1
        return False
def triplets(arr):
    x=tripletsutil(arr)
    if x==False:
        print("NO solution found")
    else:
        return

#######SPECIAL REV#########
def rev(arr):
    n=len(arr)
    j=0
    for i in range(n-1,0,-1):
        if arr[i].isalpha():
            while j<i:
                if arr[j].isalpha():
                    arr[j],arr[i]=arr[i],arr[j]
                    j+=1
                    break 
                else:
                    j+=1
    return arr 
revspecial('tan$&may')




