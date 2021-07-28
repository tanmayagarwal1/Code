from collections import defaultdict
def SplitIntoSubsequences(arr):
    if not arr : raise ValueError 
    d, end = {}, {}
    for num in arr : d[num] = d.get(num, 0) + 1
    for num in arr:
        if not d[num] : continue 
        d[num] -= 1
        if num in end and end[num] > 0 :
            end[num] -= 1
            end[num + 1] = end.get(num + 1, 0) + 1
        elif num + 1 in d and d[num + 1] and num + 2 in d and d[num + 2]:
            d[num + 1] -= 1
            d[num + 2] -= 1
            end[num + 3] = end.get(num + 3, 0) + 1
        else:
            return False 
    return True
arr = [1,2,3,3,4,4,5,5]
print(SplitIntoSubsequences(arr))