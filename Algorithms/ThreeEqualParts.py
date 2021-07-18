def SplitIntoThreeParts(arr):
    if not arr : raise ValueError 
    idx = [i for i in range(len(arr)) if arr[i] == 1]
    m = len(idx)
    if m == 0 : return [0, len(arr) - 1]
    if m % 3 != 0 : return [-1, -1]
    p1, p2 = idx[0], idx[m//3 - 1]
    p3, p4 = idx[m//3], idx[2* m//3 - 1] 
    p5, p6 = idx[2 *m//3], idx[-1]
    part1, part2, part3 = arr[p1 : p2 + 1], arr[p3 : p4 + 1], arr[p5 : p6 + 1]
    if part1 != part2 or part2 != part3 : return [-1, -1]
    l1 = p3 - p2 - 1
    l2 = p5 - p4 - 1
    l3 = len(arr) - p6 - 1
    if l3 > l2 or l3 > l1 : return [-1, -1]
    return [p2 + l3, p4 + l3 + 1]

arr = [1,1,0,0,1]
print(SplitIntoThreeParts(arr))

'''

For detailed problem desciption please checkout leetocde question number : 927, three equal parts 

'''