def License(sti, k):
    sti = sti.upper()
    sti = sti.split('-')
    sti = ''.join(sti)
    n, res = len(sti), []
    i, j = 0, n
    while j>i:
        if sti[j-k:j] : res.append(sti[j-k:j])
        else: res.append(sti[:j])
        j -= k
    return '-'.join(res[::-1])

#print(License("2-4A0r7-4k", 3))
print(License("3R-34213-3213D", 5))
