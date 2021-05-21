def MinSwapsPalindrome(sti):
    if not IsValid(sti):
        return -1 
    sti = [i for i in sti]
    f, b = 0, len(sti) - 1
    Num_swaps = 0 
    while f < b:
        if sti[f] == sti[b]:
            f += 1
            b -= 1
        else:
            temp = b 
            while temp > f and sti[f] != sti[temp]:
                temp -= 1
            if temp == f :
                sti[temp], sti[temp+1] = sti[temp+1], sti[temp]
                Num_swaps += 1
                continue 
            for i in range(temp, b):
                sti[i], sti[i+1] = sti[i+1], sti[i]
                Num_swaps += 1
            f += 1
            b -= 1
    return Num_swaps

def IsValid(sti):
    dic = dict()
    for i in sti:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    x = [i for i, j in dic.items() if j % 2 != 0 ]
    return len(x) <= 1 

print(MinSwapsPalindrome('ntiin'))