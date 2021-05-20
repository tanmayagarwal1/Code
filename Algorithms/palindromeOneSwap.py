def IsValidAfterSwap(sti):
    n = len(sti)
    f, b = 0, n-1 
    while f < b:
        if sti[f] != sti[b]:
            one, two = sti[f:b], sti[f+1 : b+1]
            return one == one[::-1] or two == two[::-1]
        f += 1
        b -= 1
    return True 
print(IsValidAfterSwap('abc'))
