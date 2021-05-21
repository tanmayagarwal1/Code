def MinSwaps(sti):
    if not IsValid(sti):
        return -1 
    i, j, swaps = 0, len(sti) - 1, 0 
    sti = [i for i in sti]
    while j > i :
        if sti[i] == sti[j]:
            i += 1
            j -= 1
        else:
            temp = j 
            while temp >=i and sti[temp] != sti[i]:
                temp -= 1
            if temp == i:
                sti[temp], sti[temp+1] = sti[temp+1], sti[temp]
                swaps += 1
                continue 
            for x in range(temp, j):
                sti[x], sti[x+1] = sti[x+1], sti[x]
                swaps += 1
            i += 1
            j -= 1
    return swaps 


def IsValid(sti):
    d = dict()
    for char in sti:
        d[char] = d.get(char, 0) + 1
    return len([i for i, j in d.items() if j%2 != 0]) <= 1

print(MinSwaps('ntiin'))